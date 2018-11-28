#include <iostream>
#include <stdio.h>
#include <set>
#include <string.h>
#include <algorithm>
#include <vector>
#include <time.h>
#include <queue>
#include <math.h>
#define ll long long
using namespace std;
const int N=2e5+9;
int n,m;
vector<int> a;
int dp[N],b[N],fr[N];
queue<int> q;
void dfs(int now)
{
	if(fr[now]+1) dfs(fr[now]);
	q.push(now);//cout<<now<<endl;
}
void init()
{
	a.clear();
	for(int i=0;i<n;i++)
	{
		int t;scanf("%d",&t);
		a.push_back(t);
	}
	reverse(a.begin(),a.end());
	a[n]=N;
	dp[0]=1;fr[0]=-1;
	b[1]=0;
	b[0]=n;
	int en=1;
	for(int i=1;i<n;i++)
	{
		int s=0,t=en;
		while(s<=t)
		{
			int mid=(s+t)>>1;
			if(a[b[mid]]>a[i]) s=mid+1;
			else t=mid-1;
		}
		if(s==en+1)
		{
			dp[i]=en+1;
			fr[i]=b[en];
			en++;
			b[en]=i;
		}else
		{
			dp[i]=t+1;
			fr[i]=b[t];
			if(fr[i]==n) fr[i]=-1;
			if(a[i]>a[b[t+1]])
			b[t+1]=i;
		}
	}
	// for(int i=0;i<n;i++) printf("%d %d\n",dp[i],fr[i]);
	 int pos=0;
	 for(int i=1;i<n;i++)
	 if(dp[i]>dp[pos]||dp[i]==dp[pos]&&a[i]<a[pos]) pos=i;
	 
	 printf("%d\n",dp[pos]);
	 // if(dp[pos]>m) puts("Transportation failed");
	 // else 
	 // {
		// dfs(pos);
		// memset(b,0,sizeof(b));
		// int st=0,top=dp[pos];
		// for(int i=0;i<n;i++)
		// {
			// int s=st,t=top-1;
			// while(s<=t)
			// {
				// int mid=(s+t)>>1;
				// if(b[mid]<a[i]) t=mid-1;
				// else s=mid+1;
			// }
			 // printf("%d%c",s+1," \n"[i==n-1]);
			// dp[a[i]]=s+1;
			 // if(s==top)while(1);
			// b[s]=a[i];
			// if(i==q.front())
			// {
				// st++;
				// q.pop();
			// }
			
		// }
		// for(int i=1;i<=n;i++) printf("%d%c",dp[i]," \n"[i==n]);
	 // }
 }
int main()
{
	int c;
	cin>>c;
	// while(scanf("%d%d",&n),n)
	while(c--)
	{
		cin>>n;
		init();
	}
	
	return 0;
}