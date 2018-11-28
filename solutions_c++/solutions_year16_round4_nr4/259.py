#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
#define PS system("pause");
using namespace std;
int mask;
int n;
int bitcount[1<<16];
int dp[5][1<<16];
vector<int>num[20];
bool iszero(int st,int i,int j){
	return (st&(1<<(i*n+j)))==0;
}
bool check(int st){
	int a[10];
	for(int i=0;i<n;i++)
		a[i]=i;
	do{
		bool ok=1;
		for(int i=0;i<n;i++){
			if(iszero(st,i,a[i])){
				ok=0;
				break;
			}
		}
		if(ok)
			return 1;
	}while(next_permutation(a,a+n));
	return 0;
}
int b[10];
bool vis[5];
bool dfs(int cur,int st){
	if(cur==n)
		return 1;
	bool ok=0;
	for(int i=0;i<n;i++){
		if(vis[i])
			continue;
		if(iszero(st,b[cur],i))
			continue;
		ok=1;
		vis[i]=1;
		if(!dfs(cur+1,st))
			return 0;
		vis[i]=0;
	}
	return ok;
}
bool solve(int st,int n){
	if(dp[n][st]!=-1)
		return dp[n][st];
	for(int i=0;i<n;i++)
		b[i]=i;
	do{
		memset(vis,0,sizeof(vis));
		if(!dfs(0,st)){
			dp[n][st]=0;
			return 0;
		}
	}while(next_permutation(b,b+n));
	dp[n][st]=1;
	return 1;
}
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int tt,cot=1;
	memset(dp,-1,sizeof(dp));
	scanf("%d",&tt);
	for(int i=0;i<1<<16;i++){
		for(int j=0;j<16;j++)
			if(i&(1<<j))
				bitcount[i]++;
		num[bitcount[i]].push_back(i);
	}
	while(tt--){
		cin>>n;
		mask=0;
		int cnt=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				int x;
				scanf("%1d",&x);
				if(x){
					mask|=(1<<(i*n+j));
					cnt++;
				}
			}
		}
		int ans=n*n;
		int fg=0;
		for(int i=cnt;i<=n*n;i++){
			for(int j=0;j<(int)num[i].size();j++){
				int x=num[i][j];
				if(x>=(1<<(n*n)))
					continue;
				if((x&mask)!=mask)
					continue;
				if(!check(x))
					continue;
				if(solve(x,n)){
					fg=1;
					ans=i;
					break;
				}
			}
			if(fg) break;
		}
		printf("Case #%d: %d\n",cot++,ans-cnt);
	}
	return 0;
}