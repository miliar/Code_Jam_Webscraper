#include<stdio.h>
#include<string.h>
int main ()
{
    freopen("B-large.in","r",stdin);
    freopen("out","w",stdout);
    int T,n;
    double C,F,X,dn;
    double ans;
    scanf("%d",&T);
    for(int icase =1;icase<=T;icase++){
        scanf("%lf%lf%lf",&C,&F,&X);
        double y= F*X-2*C;
        if(y<0)
            ans = X/2;
        else{
            dn = y/(C*F);
            n = (int)(dn);
            ans = 0;
            for(int i=1;i<=n;i++){
                ans+=C/(2+(i-1)*F);
            }
            ans +=X/(2+n*F);
        }
        printf("Case #%d: %lf\n",icase,ans);
    }
    return 0;
}
