#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int ck[400],k[25][400],n,p[25];
int dp[2000000];
vector <int> v;

int sol (int b,int l)
{
	if (!l)
		return 1;
	if (dp[b]!=-1)
		return dp[b];

	int ret = 0;

	for (int i=0;i<n;i++)
	{
		if ((1<<i)&b)
			continue;
		if (!ck[p[i]])
			continue;
		ck[p[i]]--;
		for (int j=0;j<201;j++)
			ck[j]+=k[i][j];
		ret = sol (b|(1<<i),l-1);
		for (int j=0;j<201;j++)
			ck[j]-=k[i][j];
		ck[p[i]]++;
		if (ret)
		{
			v.push_back(i);
			break;
		}
	}

	return dp[b] = ret;
}

int main()
{
	freopen ("D.in","r",stdin);
	freopen ("D.out","w",stdout);
	int t,o=1;
	scanf ("%d",&t);

	while (t--)
	{
		memset (dp,-1,sizeof(dp));
		memset (ck,0,sizeof(ck));
		memset (k,0,sizeof(k));
		v.clear();
		
		
		int i,j,l,K;
		scanf ("%d %d",&K,&n);

		

		for (i=0;i<K;i++)
		{
			scanf ("%d",&l);
			ck[l]++;
		}
		
		for (i=0;i<n;i++)
		{
			scanf ("%d %d",&p[i],&j);
			while (j--)
			{
				scanf ("%d",&l);
				k[i][l]++;
			}
		}
		
		printf ("Case #%d: ",o++);
		
		if (sol (0,n))
		{
			for (i=n-1;i>0;i--)
				printf ("%d ",v[i]+1);
			printf ("%d\n",v[i]+1);
		}
		else
			printf ("IMPOSSIBLE\n");
	}

	return 0;
}
