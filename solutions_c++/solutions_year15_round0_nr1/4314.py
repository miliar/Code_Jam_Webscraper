#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int test;
	scanf("%d",&test);
	for(int j=1;j<=test;j++)
	{
		int n,i;
		char a[1002];
		scanf("%d",&n);
		scanf("%s",a);
		int sum=0;
		int people=0;
		//sum=sum+(a[0]-'0');
		for(i=0;i<=n;i++)
		{
			if(a[i]!='0')
			{
				if(i>sum)
				{
					people=people+i-sum;
					sum=i+(a[i]-'0');
				}
				else
				{
					sum=sum+(a[i]-'0');
				}
			}
		}
		printf("Case #%d: %d\n",j,people);
	}
	return 0;
}
