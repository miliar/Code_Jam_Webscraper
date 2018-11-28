#include<stdio.h>
int main()
{
int z;
scanf("%d",&z);
double c,f,r=2;
double t1,t2,t=0,x;
int k;
for(k=0;k<z;k++)
{
scanf("%lf %lf %lf",&c,&f,&x);
r=2;
t=0;
while(1)
{
t1=x/r;
t2=c/r+x/(r+f);
if(t1>t2)
{
    t+=(c/r);
    r+=f;
}
else
{
    t+=(x/r);
    break;
}
}
printf("Case #%d: %.7lf\n",k+1,t);
}
return 0;
}
