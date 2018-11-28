# include <stdio.h>
int main ()
{   freopen("B-large.in","r",stdin);
    freopen("ans.in","w",stdout);
    double f,x,c,a,b,ans;
    int t,n,r;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
{   scanf("%lf%lf%lf",&c,&f,&x);
    a=((f*x)-(2*c))/(f*c);
    n=a;ans=0;b=2;
    for(int i=0;i<n;i++)
    {  ans+=(c/b);
       b+=f;     
    }
    ans+=x/b;
    //printf("%d",n);
    printf("Case #%d: %.7lf\n",k,ans);
}    return 0;
}             
