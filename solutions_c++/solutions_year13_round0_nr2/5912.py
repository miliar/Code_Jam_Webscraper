//Solution by Daniyar Maminov                                                                                                                                                                     
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#define mp make_pair
#define f first
#define pb push_back
#define s second
#define ub upper_bound
#define lb lower_bound
#define inf 1000*1000*1000
using namespace std;

int a[111][111], i, j, n, m, t, k, x, mx;

bool u[111][111], found, ok;

int main()
{
//	#ifndef ONLINE_JUDGE
	freopen (".in","r",stdin);
	freopen (".out","w",stdout);
//	#endif
	cin>>t;
	for (int cs=1; cs<=t; cs++)
	{
		found=0;
		cout<<"Case #"<<cs<<": ";
		scanf("%d%d", &n, &m);
		for (i=1; i<=n; i++)
		{
			for (j=1; j<=m; j++)
			{
				scanf("%d", &a[i][j]);
				u[i][j]=0;
			}
		}
		for (i=1; i<=n; i++)
		{
			if (a[i][1]==1)
			{
				ok=0;
				for (j=2; j<=m; j++)
				{
					if (a[i][j]!=1)
					{
						ok=1;
						break;
					}
				}
				if (!ok)
				{
					for (j=1; j<=m; j++)
						u[i][j]=1;
				}
		    }
			if (a[i][m]==1)
			{
				ok=0;
				for (j=1; j<m; j++)
				{
					if (a[i][j]!=1)
					{
						ok=1;
						break;
					}
				}
				if (!ok)
				{
					for (j=1; j<=m; j++)
						u[i][j]=1;
				}
		    }
		}
		for (j=1; j<=m; j++)
		{
			if (a[1][j]==1)
			{
				ok=0;
				for (i=2; i<=n; i++)
				{
					if (a[i][j]!=1)
					{
						ok=1;
						break;
					}
				}
				if (!ok)
				{
					for (i=1; i<=n; i++)
						u[i][j]=1;
				}
		    }
			if (a[n][j]==1)
			{
				ok=0;
				for (i=1; i<n; i++)
				{
					if (a[i][j]!=1)
					{
						ok=1;
						break;
					}
				}
				if (!ok)
				{
					for (i=1; i<=n; i++)
						u[i][j]=1;
				}
		    }
		}
		for (i=1; i<=n; i++)
		{
			for (j=1; j<=m; j++)
			{
				if (a[i][j]==1 && !u[i][j])
				{
					cout<<"NO\n"; 
					found=1;
					break;
				}
			}
			if (found) break;
		}
		if (!found)
		{
			cout<<"YES\n";
		}



					
	}		
	

	return 0;
}