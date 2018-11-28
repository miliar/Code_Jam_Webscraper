//Solution by Daniyar Maminov                                                                                                                                                                     
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<cstdio>
#include<cstdlib>
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

int t, a[6][6], n, m, i, j, x, y, id, k;

bool u[20];

int main()
{
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("output.txt","w",stdout);
	cin>>t;
	for (int cs=1; cs<=t; cs++)
	{
		scanf("%d", &id);
		cout<<"Case #"<<cs<<": ";
		memset(u, 0, sizeof(u));
		k=0;
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				scanf("%d", &a[i][j]);
				if (i==id) u[a[i][j]]=1;
			}
		}
		scanf("%d", &id);
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				scanf("%d", &a[i][j]);
				if (i==id) 
				{
					if (u[a[i][j]])
					{
						k++;
						x=a[i][j];
					}
				}
			}
		}
		if (!k)
		{
			cout<<"Volunteer cheated!\n";
		}
		else if (k>1)
		{
			cout<<"Bad magician!\n";
		}
		else
		{
			cout<<x<<endl;
		}
	}
		
	return 0;
}
