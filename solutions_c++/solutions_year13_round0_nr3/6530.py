#include<stdio.h>
main()
{
freopen("in2.txt","r",stdin);
freopen("out.txt","w",stdout);
int t,a,i,b,count;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
count=0;
scanf("%d%d",&a,&b);
if(a==1)count++;
if(a<=4 && b>=4)count++;
if(a<=9 && b>=9)count++;
if(a<=121 &&b >=121)count++;
if(a<=484 && b>= 484) count++;
printf("Case #%d: %d\n",i,count);
}
return 0;
}
