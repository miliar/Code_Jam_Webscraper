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
typedef long double realz;

realz score(const vector<realz>& p)
{
    int k = p.size();
    vector<realz> dp(k + 1, 0.);
    dp[0] = 1;
    for (int i = 0; i < k; ++i)
    {
        vector<realz> ne(k+1, 0.);
        for (int j = 0; j < k; ++j)
        {
            ne[j] += dp[j] * (1. - p[i]);
            ne[j+1] += dp[j] * p[i];
        }
        ne.swap(dp);
    }
    return dp[k / 2];
}

void solve()
{
    int n, k;
    cin >> n >> k;

    vector<realz> p(n);
    for (realz& x : p)
        cin >> x;

    sort(WHOLE(p));

    realz ans = 0;
    vector<realz> subs(k);
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < k; ++j)
            subs[j] = p[(i+j)%n];
        ans = max(ans, score(subs));
    }

    cout.precision(10);
    cout << fixed << ans << '\n';
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

