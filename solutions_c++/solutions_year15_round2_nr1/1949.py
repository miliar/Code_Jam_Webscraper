#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;
#define Maxn 10000500
bool vis[Maxn];
int dp[Maxn];
int bit[20];
int work(int x){
	int top=0;
	memset(bit,0,sizeof(bit));
	while (x){
		bit[++top]=x%10;
		x/=10;
	}
	int y=0;
	for (int i=1;i<=top;i++) y=y*10+bit[i];
	return y;
}
int n;
int bfs(int src){
	memset(vis,false,sizeof(vis));
	memset(dp,0x3f,sizeof(dp));
	queue<int> que;
	que.push(src);dp[src]=1;vis[src]=true;
	while (!que.empty()){
		int x=que.front();que.pop();
		int y=x+1;
		if (y<=n && !vis[y]){
			vis[y]=true;dp[y]=dp[x]+1;
			que.push(y);
		}
		y=work(x);
		if (y<=n && !vis[y]){
			vis[y]=true;dp[y]=dp[x]+1;
			que.push(y);
		}
	}
	return dp[n];
}
int main(){
	int cases;
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%lld",&n);
		int ans=bfs(1);
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}