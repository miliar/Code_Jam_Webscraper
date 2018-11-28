#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
using namespace std;

const long double eps = 1e-8;
int T;
long double X, C, F;
void read(long double &x){
     double t;
     scanf("%lf",&t);
     x = t;
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for (int tst = 1; tst <= T; tst ++){
        read(C),read(F),read(X);
        long double ans = X / 2., rate = 2., now = 0, newans;
        while (now <= ans){
            now += C / rate;
            rate += F;
            newans = now + (X / rate);
            if (fabs(newans - ans) < eps) break;
            ans = min(ans, newans);
        }
        printf("Case #%d: %.7lf\n",tst, (double)ans);
    }
    return 0;
}
