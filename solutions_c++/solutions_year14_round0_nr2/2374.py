#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
const double eps = 1e-9;
int main(){
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T, cnt = 1;
    double c, f, x;
    scanf("%d", &T);
    while(T--){
        scanf("%lf%lf%lf", &c, &f, &x);
        double t = (x*f-c*f)/c;
        double num = floor((t-2.0)/f);
        if(num < -eps){
            printf("Case #%d: %f\n", cnt++, x/2.0);
        }
        else{
            double sum = x/((num+1.0)*f+2.0)+(c/2.0);
            while(num > eps){
                sum+=(c/(num*f+2.0));
                num-=1.0;
            }
            printf("Case #%d: %f\n", cnt++, sum);
        }
    }
    return 0;
}
