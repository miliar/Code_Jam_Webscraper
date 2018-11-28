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

int64 power(int64 base, int64 p)
{
    int64 ret = 1;
    while (p)
    {
        if (p & 1)
            ret *= base;
        base *= base;
        p >>= 1;
    }
    return ret;
}

void solve()
{
    int64 k, c, s;
    cin >> k >> c >> s;

    if (s < k)
    {
        cout << "IMPOSSIBLE\n";
        return;
    }

    int64 stride = (c == 1 ? 1 : power(k, c - 1) + 1);
    for (int64 i = 0, p = 1; i < s; ++i, p += stride)
        cout << p << ' ';
    cout << '\n';
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

