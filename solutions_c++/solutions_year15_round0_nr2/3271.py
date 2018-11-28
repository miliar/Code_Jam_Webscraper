#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <cmath>
#include <queue>
#define maxn 2200
using namespace std;
int q[maxn];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int Case,t=0;
	scanf("%d",&Case);
	while (Case--)
	{
		int n,x,m=0,tot=0;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&q[i]);
			if (q[i]>m) m=q[i];
		}
		int ans=m;
		for (int i=1;i<m;i++)
		{
			int tmp=i;
			for (int j=1;j<=n;j++)
				if (q[j]>i) tmp+=((q[j]-1)/i);
			if (tmp<ans) ans=tmp;
		}
		printf("Case #%d: %d\n",++t,ans);
	}
	return 0;
}