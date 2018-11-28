#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<map>
#include<string>
#include<vector>
using namespace std;
typedef long long lld;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
int s[100010];
bool vis[100010];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n,limit;
		scanf("%d %d",&n,&limit);
		for(int i=0;i<n;i++)
			scanf("%d",&s[i]);
		sort(s,s+n);
		for(int i=0;i<n;i++)
			vis[i]=false;
		int ans=0;
		int j=n-1;
		for(int i=0;i<n;i++)
		{
			if(vis[i])
				continue;
			ans++;
			vis[i]=true;
			while(j >= 0 && s[i]+s[j] > limit)
				j--;
			while(j >= 0 && vis[j])
				j--;
			if(j >= 0 && !vis[j])
			{
				vis[j]=true;
				j--;
			}
		}
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
/*
3
3 100
10 20 70
4 100
30 40 60 70
5 100
10 20 30 40 60

 */
