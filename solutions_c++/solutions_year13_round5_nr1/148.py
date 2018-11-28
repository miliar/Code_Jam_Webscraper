#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#include <numeric>
#include <functional>
#include <utility>
#include <bitset>
#include <iostream>
#include <cmath>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <stdint.h>
#include <cstdarg>
#include <cstdio>
#include <fcntl.h>

using namespace std;

long long a[100], s[100];

int main()
{
    freopen("A-large.in", "r", stdin);
//    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int _;
    cin >> _;
    for (int __= 1; __ <= _; __ ++)
    {
        long long B;
        int n;
        cin >> B >> n;
        memset(a, 0, sizeof(a));
        for (int i = 0; i < n; ++ i)
            cin >> a[i];
        n = 37;
        sort(a, a + n);
        s[0] = a[0];
        for (int i = 1; i < n; ++ i)
            s[i] = s[i - 1] + a[i];
        double best = 0;
        for (int i = 0; i < n; ++ i)
        for (int ii = 0; ii <= i; ++ ii)
        {
            if (ii == 34 && i == 35)
                int t = 3;
            // min is a[i] - a[i]+1
            if ((a[i] + 1) * (i + 1) - (ii + 1) - s[i] > B)
                continue;
            long long res = B - ((a[i] + 1) * (i + 1) - (ii + 1) - s[i]);
            long long delta = res / (i + 1);
            long long level = a[i] + 1 + delta;
            if (i != n - 1)
                level = min(level, a[i + 1]);
            
            if (level < a[i])
                continue;
            long long pay = level * (i + 1) - (ii + 1) - s[i];
            long long get = (level - 1) * (ii + 1) - s[ii];
            if (get / (ii + 1.0) * 36 - pay > best)
                best = get / (ii + 1.0) * 36 - pay;
        }
        printf("Case #%d: %.12llf\n", __, best);
    }
}

