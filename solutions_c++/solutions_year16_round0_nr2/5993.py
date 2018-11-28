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

const int maxn = 11;
const int maxmask = 1<<maxn;

int flip(int mask, int len)
{
    int ret = mask & ~((1 << len) - 1);
    mask = ~mask;
    for (int i = 0; i < len; ++i)
        ret |= ((mask >> i) & 1) << (len - 1 - i);
    return ret;
}

int len;

int bfs(int start)
{
    static int range[maxmask];
    static int q[maxmask];
    int ql = 0, qr = 0;

    memset(range, -1, sizeof range);

    q[qr++] = start;
    range[start] = 0;

    while (range[0] == -1)
    {
        assert(ql < qr);
        int v = q[ql++];

        for (int i = 1; i <= len; ++i)
        {
            int u = flip(v, i);
            if (range[u] == -1)
            {
                range[u] = range[v] + 1;
                q[qr++] = u;
            }
        }
    }

    return range[0];
}

void solve()
{
    string s;
    cin >> s;
    len = s.size();

    int start = 0;
    for (char c : s)
        start = (start << 1) | (c == '+');
    start = flip(start, len);

    cout << bfs(start) << '\n';
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

