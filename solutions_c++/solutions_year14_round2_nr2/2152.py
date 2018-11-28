#include<stdio.h>
#include<math.h>
#include<string.h>
 int main()
{int t;
scanf("%d",&t);
int x=1;
while(t--)
{int a,b,k,j,i;
long long int count=0;
scanf("%d%d%d",&a,&b,&k);
for(i=0;i<a;i++)
{
	for(j=0;j<b;j++)
	{//printf("%d \n",i&j);
		if((i&j)<k)
		count++;}
}
printf("Case #%d: %lld\n",x,count);
x++;}
	
return 0;
}
