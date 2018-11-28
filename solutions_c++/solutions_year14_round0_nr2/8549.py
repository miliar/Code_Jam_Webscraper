#include <stdio.h>

double x,f;

int main()
{

freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);

int t,i;

scanf("%d",&t);

for(i=0;i<t;i++)
{

if(i!=0)
printf("\n");

double c,ans=0,r=2.0;

scanf("%lf%lf%lf",&c,&f,&x);

while((x*f)>(c*(r+f)))
{
ans=ans+c/r;
r=r+f;
}

ans=ans+(x/r);

printf("Case #%d: %.7lf",i+1,ans);

}

return 0;

}
