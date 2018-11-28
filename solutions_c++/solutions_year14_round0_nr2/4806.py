#include<stdio.h>
#include<string.h>

#define eps 1e-7

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,tt,i,n;
    double c,f,x,tem,tem1,ans,v;
    scanf("%d",&t);
    tt = 0;
    while(t--){
        tt++;
        scanf("%lf%lf%lf",&c,&f,&x);
        v = 0;
        n = 0;
        ans = x/2;
        while(1){
            n++;
            v += c/(2+(n-1)*f);
            tem = x/(2+n*f)+v;
            if(ans-tem<eps)
                break;
            if(ans > tem)
                ans = tem;
        }
        printf("Case #%d: %.6lf\n",tt,ans);
    }
    return 0;
}
