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

int _, __;

int n, m;
long long p;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", & _);
    for (int __ = 1; __ <= _; ++ __)
    {
        scanf("%d%I64d", & n, & p);
        long long One = 1, x;
        x = (One << n) - p;                        // x is the worst record to win a prize
        int cnt1 = n, cnt2 = n;
        long long ans1, ans2;

        for (int i = 1; i <= n; ++ i)
            if ((x >> (n - i)) & 1)
            {
                cnt1 = i - 1;
                break;
            }
        if (cnt1 == n)
            ans1 = (One << n);
        else
            ans1 = (One << (cnt1 + 1)) - 1;
        
        bool f = 0;
        for (int i = 1; i <= n; ++ i)
            if (cnt2 == n)
            {
                if (((x >> (n - i)) & 1) == 0)
                   cnt2 = i - 1;
            }
            else
            {
                if ((x >> (n - i)) & 1)
                    f = 1;
            }
        
        if (f)
            cnt2 ++;

        ans2 = (One << n) - (One << cnt2) + 1;
        printf("Case #%d: %I64d %I64d\n", __, ans1 - 1, ans2 - 1);
    }
}


