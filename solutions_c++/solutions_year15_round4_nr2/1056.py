#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
using namespace std;

#define CLR(x,y) memset(x,y,sizeof(x));

double V,X,c[2],r[2];
int n;
const double EPS = 1e-8;

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1 ;cas <= T ; ++cas) {
        scanf("%d%lf%lf",&n,&V,&X);
        for(int i = 0 ; i < n ; ++i) {
            scanf("%lf%lf",&r[i],&c[i]);
        }
        printf("Case #%d: ",cas);
        if(n==1) {
            if(fabs(c[0] - X) > 1e-5) {
                printf("IMPOSSIBLE\n");
            } else {
                printf("%.8lf\n",V/r[0]);
            }
        }
        else
        if(n==2) {
            if((c[0]-X)*(c[1]-X) > EPS) {
                printf("IMPOSSIBLE\n");
                //printf("%lf %lf %lf\n",X,c[0],c[1]);
            }
            else {
                if(fabs(c[0]-c[1]) < 1e-5) {
                    printf("%.8lf\n",V/(r[0]+r[1]));
                } else {
                    double a = (X-c[1])*V/(c[0]-c[1]);
                    double b = V-a;
                    printf("%.8lf\n",max(a/r[0],b/r[1]));
                }
            }
        }
    }

}

