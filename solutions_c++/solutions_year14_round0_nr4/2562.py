#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
using namespace std;
const int maxn = 1005;

double A[maxn], B[maxn];
bool vis[maxn];

int main()
{
    int T, nc = 0, n;
    cin >> T;
    while(T--)
    {
        int ans1 = 0, ans2 = 0;
        printf("Case #%d: ", ++nc);
        scanf("%d", &n);
        for(int i = 0; i < n; i++) scanf("%lf", A+i);
        for(int i = 0; i < n; i++) scanf("%lf", B+i);
        sort(A, A+n);
        sort(B, B+n);

        for(int i = 0, j = 0; i < n; i++) {
            if(B[j] < A[i]) { j++; ans1++; }
        }
        memset(vis, 0, sizeof vis);
        for(int i = 0; i < n; i++) {
            double t = A[i];
            bool ok = 0;
            for(int j = 0; j < n; j++) if(!vis[j])
                if(B[j] > t) {
                    ok = 1;
                    vis[j] = 1;
                    break;
                }

            if(ok == 0) {
                for(int j = 0; j < n; j++) if(!vis[j]) {
                    vis[j] = 1;
                    ans2++;
                    break;
                }
            }
        }
        printf("%d %d\n", ans1, ans2);
    }
    return 0;
}
