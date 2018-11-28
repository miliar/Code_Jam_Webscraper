#include<stdio.h>
int main()
{
freopen("B-large.txt","r",stdin);
freopen("output-2-1.txt","w",stdout);
int t=0,test;
scanf("%d",&test);
while(test--)
{
t=t+1;
double c,f,x;
scanf("%lf",&c);
scanf("%lf",&f);
scanf("%lf",&x);
 double telasped=0,temp=0,time=0,at=0,r=2;
double arr[1000];
do
{

if(telasped==0)
telasped=x/r;
else
telasped=temp;
 time=c/r;
at=at+time;
r+=f;
temp=at+x/r;
 }while(temp<telasped);
 printf("Case #%d: %.7lf\n",t,telasped);
}
return 0;
}
