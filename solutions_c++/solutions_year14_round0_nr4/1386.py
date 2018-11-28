#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#define ll long long
using namespace std;
double a[1005], b[1005];
bool cmp(double x, double y)
{
    return x>y;
}
bool vis[1005];
int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int cas, n;
    scanf("%d", &cas);
    for (int t=1; t<=cas; t++) {
        scanf("%d", &n);
        for (int i=0; i<n; i++)
            scanf("%lf", &a[i]);
        for (int i=0; i<n; i++)
            scanf("%lf", &b[i]);
        sort(a, a+n);
        sort(b, b+n);
        memset(vis, 0, sizeof(vis));
        printf("Case #%d: ", t);
        int flag;
        for (int i=0; i<n; i++) {
            flag=1;
            for (int j=0; j+i<n; j++) {
                if (a[j+i]<b[j]) {
                    flag=0;
                    break;
                }
            }
            if (flag) {
                printf("%d ", n-i);
                break;
            }
        }
        if (!flag) printf("0 ");
        int cnt=0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (!vis[j]&&b[j]>a[i]) {
                    vis[j]=1;
                    cnt++;
                    break;
                }
            }
        }
        printf("%d\n", n-cnt);
    }
    return 0;
}
