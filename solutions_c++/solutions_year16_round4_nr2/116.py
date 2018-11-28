/**
 * Copyright © 2016 Authors. All rights reserved.
 * 
 * FileName: B-large.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2016-05-29
 */
#include <bits/stdc++.h>

using namespace std;

#define rep(i,n) for (int i = 0; i < (n); ++i)
#define For(i,s,t) for (int i = (s); i <= (t); ++i)
#define foreach(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 200 + 5;

int n, k;
double p[maxn];
long double f[maxn][maxn], a[maxn], ret;

long double calc()
{
        memset(f, 0, sizeof(f));
        f[0][0] = 1;
        rep(i,k) For(j,0,i) {
                f[i+1][j] += f[i][j] * (1 - a[i]);
                f[i+1][j+1] += f[i][j] * a[i];
        }
        return f[k][k/2];
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%d%d", &n, &k);
                rep(i,n) scanf("%lf", &p[i]);
                sort(p, p + n);
                ret = 0;
                For(i,0,k) {
                        int now = 0;
                        rep(j,i) a[now++] = p[j];
                        rep(j,k-i) a[now++] = p[n-j-1];
                        ret = max(ret, calc());
                }
                printf("Case #%d: %.10f\n", ++cas, (double)ret);
        }

        return 0;
}
