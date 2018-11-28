#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
#include<queue>
#include<set>
#include<map>
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

int c,d,v;
int a[50];
int ans;
int dp[50];
int num;
int cnt;


int main()
{
	int T,R=0;
	scanf("%d",&T);
	while(T--)
	{
		R++;
		scanf("%d%d%d",&c,&d,&v);
		int i,j;
		for(i=1;i<=d;i++)
			scanf("%d",&a[i]);
		memset(dp,0,sizeof(dp));
		dp[0]=1;
		num=d;
		cnt=0;
		ans=0;
		for(i=1;i<=num;i++)
			{
				for(j=v;j>=0;j--)
				{
					if(j+a[i]<=v && dp[j]==1 && dp[j+a[i]]==0)
					{
							dp[j+a[i]]=1;
							cnt++;
					}
				}
			}
		while(cnt!=v)
		{
			for(i=1;i<=v;i++)
			{
				if(dp[i]==0)
				{
					a[++num]=i;
					ans++;
					for(j=v;j>=0;j--)
					{
						if(j+a[num]<=v && dp[j]==1 && dp[j+a[num]]==0)
						{
								dp[j+a[num]]=1;
								cnt++;
						}
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n",R,ans);
	}
	return 0;
}