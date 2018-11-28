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

#define maxm 10000
#define mod 1000002013

int _, __;

int n, m;
int a[maxm], b[maxm], p[maxm], ha[maxm], hp[maxm];

long long solve(long long s, long long t)
{
    long long len = t - s;
    return ((n + n - len + 1) * len / 2) % mod;
}

bool cmp(int i, int j)
{
    if (a[i] != a[j])
        return a[i] < a[j];
    else
        return i < j;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", & _);
    for (int __ = 1; __ <= _; ++ __)
    {
        scanf("%d%d", & n, & m);
        for (int i = 0; i < m; ++ i)
            scanf("%d %d %d", a + i, a+ m + i, p + i);
        long long ans = 0;
        for (int i = 0; i  < m; ++ i)
            ans += (solve(a[i], a[i + m]) * p[i]) % mod;

        for (int i = 0; i < m + m; ++ i)
            b[i] = i;
        sort(b, b + m + m, cmp);
        int h = 0;
        for (int i = 0; i < m + m; ++ i)
            if (b[i] < m)
            {
                int x = b[i];
                ha[h] = a[x];
                hp[h] = p[x];
                ++ h;
            }
            else
            {
                int x = b[i] - m;
                int P = p[x];
                while (P)
                {
                    int delta = min(P, hp[h - 1]);
                    ans -= (solve(ha[h - 1], a[x + m]) * delta) % mod;
                    P -= delta;
                    hp[h - 1] -= delta;
                    if (hp[h - 1] == 0)
                        -- h;
                }
            }
        ans = ((ans % mod) + mod) % mod;
        printf("Case #%d: %I64d\n", __, ans);
    }
}


/*

Case #1: 6
Case #2: 1904672
Case #3: 1079971
Case #4: 9769
Case #5: 10
Case #6: 89099
Case #7: 327972
Case #8: 2220270
Case #9: 0
Case #10: 466297
Case #11: 2571
Case #12: 0
Case #13: 7788
Case #14: 85388
Case #15: 643461
Case #16: 452746
Case #17: 0
Case #18: 559622
Case #19: 260298
Case #20: 736921
*/
