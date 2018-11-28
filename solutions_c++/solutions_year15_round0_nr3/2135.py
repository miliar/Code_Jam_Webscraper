#include <bits/stdc++.h>

using namespace std;

string s;
int n, k;
int m[4][4], z[4][4];

int f(char c)
{
    if (c == '1')
        return 0;
    else if (c == 'i')
            return 1;
        else if (c == 'j')
            return 2;
        else return 3;
}

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    m[0][0] = 0;
    m[0][1] = 1;
    m[0][2] = 2;
    m[0][3] = 3;
    m[1][0] = 1;
    m[1][1] = 0;
    m[1][2] = 3;
    m[1][3] = 2;
    m[2][0] = 2;
    m[2][1] = 3;
    m[2][2] = 0;
    m[2][3] = 1;
    m[3][0] = 3;
    m[3][1] = 2;
    m[3][2] = 1;
    m[3][3] = 0;

    z[1][1] = 1;
    z[1][3] = 1;
    z[2][1] = 1;
    z[2][2] = 1;
    z[3][2] = 1;
    z[3][3] = 1;

    cin >> t;
    for (int jj = 0; jj < t; ++jj)
    {
        string ss;
        cin >> n >> k;
        cin >> s;
        ss = s;
        for (int i = 1; i < k; ++i)
            s = s + ss;
        cout << "Case #" << jj + 1 << ": ";
        int zz = f(s[0]), sum = 0;
        bool ff = false, f1 = false;
        zz = 0;
        sum = 0;
        for (int j = 0; j < s.size(); ++j)
        {
            sum = (sum + z[zz][f(s[j])]) % 2;
            zz = m[zz][f(s[j])];
            if (!f1 && ff && sum == 0 && zz == 2)
            {
                f1 = true;
                zz = 0;
                continue;
            }
            if (!ff && sum == 0 && zz == 1)
            {
                ff = true;
                sum = 0;
                zz = 0;
            }
        }
        if (ff && f1 && zz == 3 && sum == 0)
            cout << "YES" << '\n';
        else cout << "NO" << '\n';
    }
    return 0;
}
