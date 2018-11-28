#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
const double eps = 1e-9;
using namespace std;

bool cmp1(double a, double b) { return a > b; }
bool cmp2(double a, double b) { return a < b; }

double a[1005], b[1005];
int main () {
    freopen("D-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int Case, n;
    scanf("%d", &Case);
    for(int kase = 1; kase <= Case; ++kase) {
        scanf("%d", &n);
        for(int i = 0; i < n; ++i) scanf("%lf", &a[i]);
        for(int i = 0; i < n; ++i) scanf("%lf", &b[i]);

        sort(a, a + n, cmp1);
        sort(b, b + n, cmp1);
        int tq = 0, kq = 0;
        int ts = n - 1, ks = n - 1;
        int total = 0;
        for(int i = 0; i < n; ++i) {
            if((a[tq] - b[kq]) > eps) { total++; tq++; kq++; }
            else if((b[kq] - a[tq]) > eps) { kq++; ts--; }
            else if((a[ts] - b[ks]) > eps) { total++; ts--; ks--; }
            else if((b[kq] - a[ts]) > eps) { ts--; kq++; }
            else if(b[kq] == a[tq]) { kq++; tq++; }
            else if(b[ks] == a[ts]) { ks--; ts--; }
        }
        sort(a, a + n, cmp2);
        sort(b, b + n, cmp2);
        int ans = n;
        bool flag[1005];
        memset(flag, 0, sizeof(flag));
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                if(!flag[j] && a[i] < b[j]) { flag[j] = 1; ans--; break; }
            }
        }

        printf("Case #%d: %d %d\n", kase, total, ans);
    }
    return 0;
}

