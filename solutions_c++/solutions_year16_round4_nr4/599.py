#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
int n;


bool test(vector <vector <bool> > &mask)
{
    vector <int> ord(n), mch(n);
    for (int i = 0; i < n; ++i)
        ord[i] = mch[i] = i;
    bool flag = false;
    do
    {
        do
        {
            vector <bool> used(n, false);
            for (int q = 0; q < n; ++q)
            {
                int pr = ord[q];
                if (mask[pr][mch[pr]])
                {
                    used[mch[pr]] = true;
                    continue;
                }
                bool flag2 = false;
                for (int i = 0; i < n; ++i)
                    if (!used[i] && mask[pr][i])
                        flag2 = true;
                if (!flag2)
                    flag = true;
                else
                    break;
            }

        } while ((next_permutation(mch.begin(), mch.end()) && flag == false));

    } while ((next_permutation(ord.begin(), ord.end())) && flag == false);
    return !flag;
}


int ans(vector <vector <bool> > &st)
{
    int mans = 16;
    vector <vector <bool> > mask(n, vector <bool> (n));
    for (int i = 0; i < (1 << (4 * n)); ++i)
    {
        bool flag = true;
        int cnt = 0;
        for (int j = 0; j < n; ++j)
        {
            for (int k = 0; k < n; ++k)
            {
                mask[j][k] = ((i >> (j * n + k)) & 1);
                if (mask[j][k] == 0 && st[j][k] == 1)
                    flag = false;
                if (mask[j][k] == 1 && st[j][k] == 0)
                    cnt += 1;
            }
        }
        if (flag && test(mask) && cnt < mans)
        {
            mans = cnt;

        }

    }
    return mans;
}


int main()
{
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin >> t;
    for (int _ = 1; _ <= t; ++_)
    {
        cout << "Case #" << _ << ": ";
        cin >> n;
        vector <vector <bool> > st(n, vector <bool> (n));
        string s;
        for (int i = 0; i < n; ++i)
        {
            cin >> s;
            for (int j = 0; j < n; ++j)
                st[i][j] = (s[j] == '1');
        }
        cout << ans(st) << endl;
    }
}
