#include <stdio.h>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
bool vis[15];
bool cover(int a){
	while(a){
		vis[a%10]=1;
		a/=10;
	}
	for(int i=0;i<=9;i++){
		if(!vis[i])return 1;
	}
	return 0;
}
bool check(int a){
	while(a){
		int ck=a%10;
		if(ck&1){
			return 1;
		}
		a/=10;
	}
	return 0;
}
int main(void)
{
	int t,n,cas=0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		memset(vis,0,sizeof(vis));
		scanf("%d",&n);
		if(!n){
			printf("Case #%d: INSOMNIA\n",++cas);
			continue;
		}
		int flag;
		for(flag=1;cover(flag*n);flag++){}
		printf("Case #%d: %d\n",++cas,flag*n);
	}
	return 0;
}
