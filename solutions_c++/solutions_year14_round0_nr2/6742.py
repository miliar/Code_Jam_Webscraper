#include<stdio.h>
#include<stdlib.h>

int main()
{
int t,k;
double c,f,x,rate,t1,t2,ans=0.0,cookies=0.0,v;
// freopen("new 3.txt","r",stdin);
//freopen("out2.txt","w",stdout);
scanf("%d",&t);
for(k=1;k<=t;k++)
{ans=cookies=0.0;
scanf("%lf %lf %lf",&c,&f,&x);
//printf("%lf %lf %lf\n",c,f,x);
rate=2.0;
while(cookies<x)
{
t1=t2=0.0;
t1=x/rate;
//printf("t1: %lf\n",t1);
t2=c/rate;
//printf("t2: %lf\n",t2);
rate+=f;
v=x/rate;
//t2+=x/rate;
v+=t2;
//printf("increase in t2: %lf\n",x/rate);
//printf("t2: %lf\n",v);
if(t1<=v)
{
ans+=t1;
cookies=x;
}
else
{
ans+=t2;
cookies=0;
}
//printf("ans: %lf\n",ans);
//printf("cookies: %lf\n",cookies);
}
printf("Case #%d: %.7lf\n",k,ans);
//printf("\n");
}
return 0;
// fclose(stdin);
//fclose(stdout);
}
