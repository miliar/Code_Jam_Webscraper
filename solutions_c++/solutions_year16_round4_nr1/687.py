#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wunused-result"
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}


int const maxn = 1 << 15;
char a[maxn];
char d[5] = "PRS";

map<pair<int,int>, string> rets;

void test(int cur, int index, int n)
{
    a[index] = d[cur];
    for(int i = 0; i < n;++i)
    {
        int mask = 1 << i;
        if ((mask & index) == 0)
            test( (cur + 1) % 3, mask | index, n);
    }
}

void solve(int numtest)
{
    int n,r,p,s;
    cin >> n >> r >> p >> s;

    string ans = "Z";

    for(int t = 0; t < 3; ++t)
    {
        for(int i = 0; i < maxn; ++i)
            a[i] = 0;

        test(t, 0, n);

        int cr = 0, cp = 0, cs = 0;
        for(int j = 0; j < (1 << n); ++j)
            if (a[j] == 'R')
                ++cr;
            else  if (a[j] == 'P')
                ++cp;
            else
                ++cs;
        if (cp == p && cs == s && cr == r)
        {
            string tmp = rets[{t, n}];
            if (tmp < ans)
                ans = tmp;
        }
    }
    if (ans == "Z")
        ans = "IMPOSSIBLE";
    cout << "Case #" << numtest << ": " << ans << '\n';
}

void pp(int cur, int n)
{
    if (n == 0)
        rets[{cur, n}] = string(1, d[cur]);
    else
    {
        int ncur = (cur + 1) % 3;
        pp(cur, n - 1);
        pp(ncur, n - 1);
        string s1 = rets[{ncur, n - 1}];
        string s2 = rets[{cur, n - 1}];
        string ans = s1 + s2 < s2 + s1? s1 + s2 : s2 + s1;
        rets[{cur, n}] = ans;
    }
}

void precalc()
{
    for(int i = 0; i < 3; ++i)
        pp(i, 12);
}

int main()
{
    precalc();
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
        solve(i);
}

