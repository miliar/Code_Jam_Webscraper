#include<stdio.h>
#include<string.h>
double c,f,x;
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int ca,cc;
    int i,j;
    double t,tim,ans,ff;
    scanf("%d",&ca);
    for (cc=1;cc<=ca;cc++){
        ans=1e100;
        scanf("%lf%lf%lf",&c,&f,&x);
        ff=2.0;
        t=0;
        for (int sum=0;sum<=100000;sum++){
            tim=x/ff+t;
            if (ans>tim) ans=tim;
            t=t+c/ff;
            ff=ff+f;
        }
        printf("Case #%d: %.9lf\n",cc,ans);
    }
    return 0;
}
                 
