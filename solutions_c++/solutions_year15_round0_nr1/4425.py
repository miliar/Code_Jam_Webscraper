#include<cstdio>
#include<iostream>
using namespace std;
#define MAX 1001
int main()
{
	int t,c1,c2,i,j,s;
	char a[MAX];
	
	freopen("output.txt", "w" , stdout);
	freopen("input.txt", "r" ,stdin);
	
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		c1=c2=0;
		scanf("%d",&s);
		scanf("%s",a);
		c1=a[0]-'0';
		for(i=1;i<=s;i++)
		{
			if(a[i]-'0'!=0)
			{
			if(c1<i)
			{
			c2+=i-c1;
			c1+=(i-c1)+(a[i]-'0');
			}
			else
			c1+=(a[i]-'0');
			}
						
		}
		printf("Case #%d: %d\n",j,c2);
	}
return 0;
}
