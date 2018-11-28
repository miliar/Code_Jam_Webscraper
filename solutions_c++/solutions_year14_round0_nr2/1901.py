#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#define sqr(x) (x*x)
using namespace std;


int T,k;
double C,F,X;

int main() {
    freopen("b1.in","r",stdin);
    freopen("b1.out","w",stdout);
    scanf("%d",&T);
    for (int kase = 1;kase <= T; kase++) {
        scanf("%lf%lf%lf",&C,&F,&X);
        double sum = 0,ans = 1e18;
        ans = min(ans,X/2);
        for (int i = 1;i <= 100000; i++) {
            sum += C/((i-1)*F+2);
            ans = min(ans,sum+X/(i*F+2));
        }
        printf("Case #%d: %.7lf\n",kase,ans);
    }
    return 0;
}
