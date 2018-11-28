#include<stdio.h>
main()
{
    double c,f,x,ans,cur,r;
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        if(c>=x) ans=x/2;
        else
        {//puts("else");
            cur=c;ans=c/2;r=2;
            while(1)
            {
                if(cur*(r+f)>=x*f) {ans+=(x-cur)/r;break;}
                r+=f;
                cur=c;ans+=cur/r;
            }
        }
        printf("Case #%d: %.7lf\n",i,ans);
    }
    return 0;
}
