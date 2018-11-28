#include <bits/stdc++.h>
using namespace std;
int main() 
{	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{	int s,j,sum=0,count=0;
		scanf("%d",&s);
		char a[s+1];
		scanf("%s",a);
		for(j=0;j<=s;j++)
		{	if(j==0)
			{	sum+=(a[j]-'0');
			}
			else if(j<=sum)
			{	sum+=(a[j]-'0');
			}
			else
			{	count+=1;
				sum+=(a[j]-'0')+1;
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}