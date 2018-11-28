#include<cstdio>
#include<cstring>
int T,t,i;
double c,f,x,nc,pre,now;
double culc(int s)
{
    double ans=pre-x/nc;
    ans+=c/nc;
    nc+=f;
    return ans+x/nc;
}
bool comp()
{
     now=culc(i);
     if (now<pre)return pre=now,1;
     return 0;
 }
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        nc=2;
        pre=x/2;
        for (i=1;comp();i++);
        printf("Case #%d: %.7f\n",t,pre);
    }
    return 0;
}
