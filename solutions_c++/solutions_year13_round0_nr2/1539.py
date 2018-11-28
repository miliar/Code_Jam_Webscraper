#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
using namespace std;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mod 1000000007
#define inf (1LL)<<60
typedef long long lld;
int g[110][110];
int main()
{
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n,m;
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&g[i][j]);
		bool flag=true;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				bool flag1=true;
				for(int k=0;k<n;k++)
					if(g[k][j] > g[i][j])
						flag1=false;
				bool flag2=true;
				for(int k=0;k<m;k++)
					if(g[i][k] > g[i][j])
						flag2=false;
				if(!flag1 && !flag2)
					flag=false;
			}
		printf("Case #%d: ",cc);
		if(flag)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
