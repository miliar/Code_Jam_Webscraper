#include<stdio.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,n;
    double C,F,X;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        //int n=int(X/C-C/F-1);
        //if(n<0)n=0;
        //else n--;
        double ans=X/2.0,tmp=0.0;
        for(int i=0;;i++)
        {
            tmp+=C/(2.0+i*F);
            if(tmp+X/(2.0+i*F+F)<ans)ans=tmp+X/(2.0+i*F+F);
            else break;
        }
        printf("Case #%d: %.7lf\n",t,ans);
    }
    return 0;
}
