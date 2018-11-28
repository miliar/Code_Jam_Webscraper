/******************************************************
 * File Name:   c.cpp
 * Author:      kojimai
 * Create Time: Fri 15 Apr 2016 07:38:35 PM PDT
******************************************************/

#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
#define FFF 1005
int next[FFF];
bool vis[FFF];
int ans,n;

void dfs(int root,int pre,int now,int cnt) {
	if(next[now] == pre || next[now] == root) {
		ans = max(ans,cnt);
	}
	if(next[now] == pre) {
		for(int i = 1;i <= n;i++) {
			if(!vis[i]) {
				vis[i] = true;
				dfs(root,now,i,cnt+1);
				vis[i] = false;
			}
		}
	}
	if(!vis[next[now]]) {
		vis[next[now]] = true;
		dfs(root,now,next[now],cnt+1);
		vis[next[now]] = false;
	}
}

int main() {
	int T;
	freopen("out.out","w",stdout);
	cin >> T;
	for(int Cas = 1;Cas <= T;Cas++) {
		printf("Case #%d: ",Cas);
		memset(vis,false,sizeof(vis));
		memset(next,0,sizeof(next));
		cin >> n;
		for(int i = 1;i <= n;i++) {
			cin >> next[i];
		}
		ans = 1;
		for(int i = 1;i <= n;i++) {
			memset(vis,false,sizeof(vis));
			vis[i] = true;
			dfs(i,-1,i,1);
			vis[i] = false;
		}
		printf("%d\n",ans);
	}
	return 0;
}