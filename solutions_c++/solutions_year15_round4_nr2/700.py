#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;
const int Mn = 100 + 10;
const double eps = 1e-8;
int dcmp(double x) {
    return x < -eps ? -1 : x > eps;
}
double V,X;

double r[Mn],c[Mn];
int n;
int main() {
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas) {
          scanf("%d%lf%lf",&n,&V,&X);
          for(int i = 1; i <= n; ++i)
            scanf("%lf%lf",&r[i],&c[i]);  
            if(n == 1) {
                if(dcmp(c[1] - X) == 0) {
                    printf("Case #%d: %.6f\n",cas,V / r[1]);
                } else {
                    printf("Case #%d: IMPOSSIBLE\n",cas);
                }
            } else if(n == 2) {
                if(dcmp(X - min(c[1],c[2])) < 0 || dcmp(X - max(c[1],c[2])) > 0) {
                    printf("Case #%d: IMPOSSIBLE\n",cas);    
                } else if(dcmp(c[1] - c[2]) == 0) {
                    printf("Case #%d: %.6f\n",cas,V / (r[1]+r[2]));
                } else {
                    if(dcmp(c[1] - c[2]) > 0) {
                        swap(c[1],c[2]);
                        swap(r[1],r[2]);
                    }
                    double p1 = (c[2] - X) / (c[2] - c[1]);
                    double p2 = (X - c[1]) / (c[2] - c[1]);
                    printf("Case #%d: %.6f\n",cas,max(V * p1 / r[1] ,V * p2 / r[2]));
                }
            } else {
                /*double l = 0, r = 1e20;
                for(int i = 1; i <= 100; ++i) {
                    double mid = l + r;
                    if(check(mid, V  * X)) 
                        l = mid;
                    else
                        r = mid;
                }*/
            }
         
        printf("");
    }
    return 0;
}
