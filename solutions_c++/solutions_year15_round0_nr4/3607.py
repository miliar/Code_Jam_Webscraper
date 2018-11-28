#include<stdio.h>
#include<stdlib.h>
int a,b,c;
int rhs();
int main(){
int i,t;

scanf("%d",&t);
for(i=1;i<=t;i++)
{
	scanf("%d",&a);
	scanf("%d",&b);
	scanf("%d",&c);
	if((a>=7|| (b<a && c<a) || c<a/2+1 || b<a/2+1 || b*c%a!=0)&& rhs())
		printf("Case #%d: RICHARD\n",i);
	else
	{
		printf("Case #%d: GABRIEL\n",i);
	}
}
return 0;
}
int rhs()
{
	if(a>2 || (a==2 && (b*c<2 || b*c%2!=0))) 
	return 1;
	else
	return 0;
}
