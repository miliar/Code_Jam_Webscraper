#include <stdio.h>
#include <string.h>
int main(){
    int cas, t;
    double c, f, x;
    double ans;
    double v;
    double tot;
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    for(cas = 1; cas <= t; cas++){
        scanf("%lf%lf%lf", &c, &f, &x);
        v = 2.0;
        ans = 0.0;
        while(x / v > x / (v + f) + c / v){
            ans += c / v;
            v += f;
        }
        ans += x / v;
        printf("Case #%d: %.7lf\n", cas, ans);
    }
    return 0;
}
