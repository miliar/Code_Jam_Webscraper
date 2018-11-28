#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int dp[10][20];
int n,e,r,v[20];

int sol (int l,int ind)
{
	if (ind == n)
		return 0;
	if (dp[l][ind]!=-1)
		return dp[l][ind];
	int ret = -1;
	for (int i=0;i<=l;i++)
		ret = max (ret, sol (min(l-i+r,e),ind+1)+i*v[ind]);
	return dp[l][ind]=ret;
}

int main ()
{
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int T,c=1;
	scanf ("%d",&T);
	while (T--)
	{
		memset (dp,-1,sizeof(dp));
		int i,j;
		scanf ("%d %d %d",&e,&r,&n);
		for (i=0;i<n;i++)
			scanf ("%d",&v[i]);
		printf ("Case #%d: %d\n",c++,sol(e,0));
	}
	//system("pause");
	return 0;
}
