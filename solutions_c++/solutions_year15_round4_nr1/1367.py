#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
#include<queue>
#include<set>
#include<set>
#include<math.h>
#include<string>
#include<bitset>
#include <time.h>
using namespace std;
//#pragma warning(disable:4996)
#pragma comment(linker, "/STACK:102400000,102400000")
#define ll long long
#define mp make_pair 
#define pb push_back
#define pii pair<int,int>
#define mem(a,b) memset(a,b,sizeof(a))
#define maxn 110
#define inf 0x3f3f3f3f
const int dir[4][2]={0,1,0,-1,1,0,-1,0};
const double eps = 1e-9;
const ll mod = 1e9 + 7;

int n,m;
char ts[105];
int bp[105][105];
int visx[105],visy[105];

int main()
{
	int T,R=0;
	scanf("%d",&T);
	while(T--)
	{
		R++;
		int i,j;
		scanf("%d%d",&n,&m);
		memset(visx,0,sizeof(visx));
		memset(visy,0,sizeof(visy));
		for(i=1;i<=n;i++)
		{
			scanf("%s",ts);
			for(j=1;j<=m;j++)
			{
				if(ts[j-1]=='.')
					bp[i][j]=0;
				else if(ts[j-1]=='^')
					bp[i][j]=1;
				else if(ts[j-1]=='v')
					bp[i][j]=2;
				else if(ts[j-1]=='<')
					bp[i][j]=3;
				else if(ts[j-1]=='>')
					bp[i][j]=4;

				if(bp[i][j]>0)
				{
					visx[i]++;
					visy[j]++;
				}
			}
		}
		int flag=1;
		int ans=0;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				if(bp[i][j]>0)
				{
					if(bp[i][j]==3)
					{
						if(visx[i]>1 || visy[j]>1)
						{
							ans++;
						}
						else
						{
							flag=0;
						}
					}
					break;
				}
			}
			if(flag==0)
				break;
		}
		for(i=1;i<=n;i++)
		{
			for(j=m;j>=1;j--)
			{
				if(bp[i][j]>0)
				{
					if(bp[i][j]==4)
					{
						if(visx[i]>1 || visy[j]>1)
						{
							ans++;
						}
						else
						{
							flag=0;
						}
					}
					break;
				}
			}
			if(flag==0)
				break;
		}
		for(j=1;j<=m;j++)
		{
			for(i=1;i<=n;i++)
			{
				if(bp[i][j]>0)
				{
					if(bp[i][j]==1)
					{
						if(visx[i]>1 || visy[j]>1)
						{
							ans++;
						}
						else
						{
							flag=0;
						}
					}
					break;
				}
			}
			if(flag==0)
				break;
		}
		for(j=1;j<=m;j++)
		{
			for(i=n;i>=1;i--)
			{
				if(bp[i][j]>0)
				{
					if(bp[i][j]==2)
					{
						if(visx[i]>1 || visy[j]>1)
						{
							ans++;
						}
						else
						{
							flag=0;
						}
					}
					break;
				}
			}
			if(flag==0)
				break;
		}
		if(flag==0)
			printf("Case #%d: IMPOSSIBLE\n",R);
		else
			printf("Case #%d: %d\n",R,ans);
	}
	return 0;
}