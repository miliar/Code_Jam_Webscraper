#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wunused-result"
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}

inline int cntb(int t)
{
    int ans = 0;
    while (t > 0)
    {
        ++ans;
        t &= (t - 1);
    }
    return ans;
}

bool check(vector<string>& s)
{
    int n = s.size();

    vector<int> num1(n, 0);
    vector<int> num2(n, 0);

    for(int i = 0; i < n; ++i)
        num1[i] = i, num2[i] = i;

    do
    {
        do
        {
            vector<int> used(n, 0);
            for(int i = 0; i < n; ++i)
            {
                int u = num1[i];
                for(int j = 0; j < n; ++j)
                {
                    int v = num2[j];
                    if (s[u][v] == '1' && used[v] == 0)
                    {
                        used[v] = 1;
                        break;
                    }
                }
            }

            for(int i = 0; i < n; ++i)
                if (used[i] == 0)
                    return false;

        }while (next_permutation(num2.begin(), num2.end()));
    }while (next_permutation(num1.begin(), num1.end()));

    return true;
}

void solve(int numtest)
{

    int n;
    cin >> n;

    vector<string> s(n);
    for(int i = 0; i < n; ++i)
        cin >> s[i];

    int l = 1 << (n * n);

    int ans = 1000000;
    for(int i = 0; i < l; ++i)
    {
        vector<string> curs = s;
        int cur = cntb(i);
        for(int j = 0; j < n; ++j)
            for(int k = 0; k < n; ++k)
                if (i & (1 << (j * n + k)))
                    curs[j][k] = '1';
        if (cur < ans && check(curs))
        {
            ans = cur;
        }
    }

    cout << "Case #" << numtest << ": " << ans << '\n';
}


int main()
{
    freopen("D-small.in", "r", stdin);
    freopen("D-small.out", "w", stdout);

    //freopen("in.txt", "r", stdin);


    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        solve(i);
        cerr << "ok " << i << endl;
    }
}

