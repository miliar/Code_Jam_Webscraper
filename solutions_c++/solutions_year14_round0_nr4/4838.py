#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{int t;
scanf("%d",&t);
int c=1;
while(t--)
{
	int n;
	scanf("%d",&n);
	double first[n],second[n];
	int i,j;
	for(i=0;i<n;i++)
	scanf("%lf",&first[i]);
	for(i=0;i<n;i++)
	scanf("%lf",&second[i]);
	
	if(n==1)
	
{if(first[0]>second[0])
printf("Case #%d: 1 1\n",c);
else printf("Case #%d: 0 0\n",c);
	
}
else
{int a=0,b,count=0;
	sort(first,first+n);
	sort(second,second+n);
	double third[n];
	for(i=0;i<n;i++)
	third[i]=second[i];
	for(i=0;i<n;i++)
{int flag=0;
	for(j=0;j<n;j++)
	{
		if(first[i]<second[j])
		{count++;
		flag=1;
		second[j]=-1.0;}
		if(flag)
		break;}
}
b=n-count;

for(i=0,j=0;i<n;i++)
{
	if(first[i]>third[j])
	{
		j++;
		a++;
	}
}

printf("Case #%d: %d %d\n",c,a,b);
}
	
c++;}
return 0;}
