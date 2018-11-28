#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <cmath>
#define maxn 2200
using namespace std;
int v[maxn];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int Case,t=0;
	scanf("%d",&Case);
	while (Case--)
	{
		int m,n;
		char c;
		scanf("%d",&n);
		scanf("%c",&c);
		for (int i=0;i<=n;i++)
		{
			scanf("%c",&c);
			v[i]=c-'0';
		}
		int ans=0,sum=v[0];
		for (int i=1;i<=n;i++)
		{
			if (sum<i)
			{
				ans+=(i-sum);
				sum+=(i-sum);
			}
			sum+=v[i];
		}
		printf("Case #%d: %d\n",++t,ans);
	}
	return 0;
}