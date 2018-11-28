#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <iostream>
#include <list>
#include <string>
#include <queue>
#include <numeric>
#include <algorithm>
#include <set>
#include <sstream>
#include <cmath>
#include <map>
#include <stack>
#include <ctime>
#include <cstring>
#include <cassert>

typedef signed char int8;
typedef unsigned char uint8;
typedef signed int int32;
typedef unsigned int uint32;
typedef signed long long int64;
typedef unsigned long long uint64;

#define mp(a, b) std::make_pair(a, b)
using namespace std;

int main()
{
    int CASES;
    cin >> CASES;

    const int64 q = 1000002013;

    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        uint64 n, m;
        cin >> n >> m;

        vector<uint64> r(n+1, 0), f(n+1, 0);
        vector<uint64> nastup(n+1, 0);
        vector<uint64> vystup(n+1, 0);

        for (int i = 0; i < m; ++i)
        {
            int a, b, c;
            scanf("%d %d %d", &a, &b, &c);
            nastup[a] += c;
            vystup[b] += c;

            f[b - a] += c;
            f[b-a] %= q;
        }

        vector<pair<uint64, int> > v;

        for (int i = 1; i <= n; ++i)
        {
            if (nastup[i])
                v.push_back(mp(nastup[i], i));

            uint64 todo = vystup[i];

            while (todo)
            {
                if (v.back().first > todo)
                {
                    v.back().first -= todo;
                    r[i - v.back().second] += todo;
                    r[i - v.back().second] %= q;
                    todo = 0;
                    break;
                }

                todo -= v.back().first;
                r[i - v.back().second] += v.back().first;
                r[i - v.back().second] %= q;
                v.pop_back();
            }
        }

        int64 res = 0;
        int64 beg = 0;
        

        for (int i = 0; i < n; ++i)
        {
            res += int64(f[i] - r[i]) * beg;
            res %= q;

            while (res < 0)
                res += q;

            beg += n - i;
        }

        printf("Case #%d: %lld\n", CASE, res);
    }

    return 0;
}
