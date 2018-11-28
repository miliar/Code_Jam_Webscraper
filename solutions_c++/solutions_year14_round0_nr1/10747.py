#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<string>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<limits.h>
using namespace std;
#define ll long long

int main()
{
	int test;
	scanf("%d",&test);
	int count=1;
	while(test--)
	{
		int x,y;
		scanf("%d",&x);
		int i,j,k;
		int a[5],b[5];
		for(i=1;i<=4;i++)
		{
			if(i==x)
			{
				for(j=1;j<=4;j++)
					scanf("%d",&a[j]);
			}
			else
			{
				for(j=1;j<=4;j++)
					scanf("%d",&k);
			}
		}
		scanf("%d",&y);
		for(i=1;i<=4;i++)
		{
			if(i==y)
			{
				for(j=1;j<=4;j++)
					scanf("%d",&b[j]);
			}
			else
			{
				for(j=1;j<=4;j++)
					scanf("%d",&k);
			}
		}
		k=-1;
		int f=0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(a[i]==b[j]&&k==-1)
				{
					k=a[i];
				}
				else if(a[i]==b[j]&&k>0)
				{
					printf("Case #%d: Bad magician!\n",count);
					f=1;
					break;
				}
			}
			if(f==1)
				break;
		}
		if(f==0)
		{
			if(k==-1)
			{
				printf("Case #%d: Volunteer cheated!\n",count);
			}
			else
				printf("Case #%d: %d\n",count,k);
		}
		count++;
	}
	return 0;
}

