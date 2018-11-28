// License {{{
// Copyright © 2016 Fedor Alekseev <feodor.alexeev@gmail.com>
// This work is free. You can redistribute it and/or modify it under the
// terms of the Do What The Fuck You Want To Public License, Version 2,
// as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
// }}}

#include <bits/stdc++.h>
using namespace std;

#ifdef moskupols
    #define debug(...) fprintf(stderr, __VA_ARGS__)
#else
    #define debug(...) 42
#endif

#define timestamp(x) debug("["#x"]: %.3f\n", (double)clock() / CLOCKS_PER_SEC)

#define hot(x) (x)
#define sweet(value) (value)
#define faceless

#define WHOLE(v) (v).begin(),(v).end()
#define RWHOLE(v) (v).rbegin(),(v).rend()
#define UNIQUE(v) (v).erase(unique(WHOLE(v)),(v).end())

typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

const int maxn = 4;

int knows[maxn][maxn];
int init[maxn][maxn];
int n;

bool check(const vector<int> &perm, size_t step, int busy)
{
    if (step == perm.size())
        return true;
    int v = perm[step];
    bool ok = false;
    for (int i = 0; i < (int)perm.size(); ++i)
        if (!((busy>>i)&1) && knows[v][i])
        {
            ok = check(perm, step + 1, busy | (1<<i));
            if (!ok)
                return false;
        }
    return ok;
}

bool check()
{
    vector<int> perm(n);
    iota(WHOLE(perm), 0);

    do
    {
        if (!check(perm, 0, 0))
            return false;
    } while (next_permutation(WHOLE(perm)));
    return true;
}

void solve()
{
    memset(init, 0, sizeof init);

    cin >> n;

    int mask = 0;

    for (int i = 0; i < n; ++i)
    {
        string s;
        cin >> s;
        for (int j = 0; j < n; ++j)
        {
            init[i][j] = s[j] == '1';
            mask |= (s[j] == '1') << (n * i + j);
        }
    }

    int ans = 1<<30;
    for (int i = 0; i < (1<<(n*n)); ++i)
        if ((i & mask) == 0)
        {
            memcpy(knows, init, sizeof init);
            for (int j = 0; j < n*n; ++j)
                if ((i>>j)&1)
                    knows[j / n][j % n] = 1;
            if (check())
                ans = min(ans, __builtin_popcount(i));
        }
    cout << ans << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        solve();
        debug("%d ", i);
        timestamp(multi);
    }

    timestamp(end);
    return 0;
}

