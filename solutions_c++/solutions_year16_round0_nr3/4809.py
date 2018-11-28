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

const int primesCount = 10005;
int64 primes[primesCount];
int psz = 0;

int64 getFactor(int64 v)
{
    for (int i = 0; i < psz && primes[i] * primes[i] <= v; ++i)
        if (v % primes[i] == 0)
            return primes[i];
    return 0;
}

struct _PrimesInitializer
{
    _PrimesInitializer()
    {
        primes[psz++] = 2;
        int64 p = 2;
        while (psz < primesCount)
        {
            ++p;
            while (getFactor(p))
                ++p;
            primes[psz++] = p;
        }
    }
} _primesInitializer;


string to_string(int64 x, int base)
{
    assert(2 <= base && base <= 16);
    string ret;
    while (x)
    {
        ret += "0123456789ABCDEF"[x % base];
        x /= base;
    }
    reverse(WHOLE(ret));
    return ret;
}

vector<int64> getFactors(int mask)
{
    vector<int64> ret;
    ret.reserve(10 - 2 + 1);

    string s = to_string(mask, 2);

    for (int base = 2; base <= 10; ++base)
    {
        int64 v = stoll(s, 0, base);
        int64 f = getFactor(v);
        if (f == 0)
            return {};
        ret.push_back(f);
    }
    return ret;
}


void solve()
{
    int n, J;
    cin >> n >> J;

    cout << '\n';
    for (int submask = 0; submask < (1<<(n-2)) && J; ++submask)
    {
        int mask = (1 << (n-1)) | 1 | (submask << 1);
        // debug("%s\n", to_string(mask, 2).c_str());
        vector<int64> factors = getFactors(mask);
        if (!factors.empty())
        {
            assert(factors.size() == (10 - 2 + 1));
            cout << to_string(mask, 2);
            for (int64 f : factors)
                cout << ' ' << f;
            cout << '\n';
            --J;
        }
    }
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

