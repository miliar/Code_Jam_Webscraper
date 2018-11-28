/**
 * Copyright (c) 2014 Authors. All rights reserved.
 * 
 * FileName: B.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2014-05-31
 */
#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for (int i = 0; i < (n); ++i)
#define FOR(i,s,t) for (int i = (s); i <= (t); ++i)
#define FOREACH(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 1000 + 5;

int n;
int a[maxn], b[maxn];

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%d", &n);
                REP(i,n) {
                        scanf("%d", &a[i]);
                        b[i] = a[i];
                }
                sort(b, b + n);
                int p = 0, q = n - 1, res = 0;
                REP(i,n) {
                        int x = p;
                        while (x < q && a[x] != b[i]) ++x;
                        if (x - p < q - x) {
                                res += x - p;
                                while (x != p) {
                                        swap(a[x], a[x-1]);
                                        --x;
                                }
                                ++p;
                        } else {
                                res += q - x;
                                while (x != q) {
                                        swap(a[x], a[x+1]);
                                        ++x;
                                }
                                --q;
                        }
                }
                printf("Case #%d: %d\n", ++cas, res);
        }

        return 0;
}
