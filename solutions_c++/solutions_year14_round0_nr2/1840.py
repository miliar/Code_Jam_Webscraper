#include<stdio.h>
int main()
{
    int T,n;
    double  C,X,F,v,t,m,i;
    //freopen("b.in","r",stdin);
    //freopen("b.txt","w",stdout);
    scanf("%d",&T);
    n=1;
    while(T--)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        for(v=2,m=0;;v+=F,m++)
        {
            if(X<(C+X/(v+F)*v)) break;
        }
        for(i=0,t=0,v=2;i<m;v+=F,i++) t+=C/v;
        t+=X/v;
        printf("Case #%d: %.7lf\n",n++,t);
    }
    return 0;
}
