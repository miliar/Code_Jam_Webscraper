/*************************************************************************
    > File Name: B.cpp
    > Author: milaso
    > Mail: 562058113@qq.com 
    > Created Time: 六  4/11 19:18:22 2015
 ************************************************************************/

#include<iostream>
#include<math.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std;


int p[1010];
int c[1010];

int dfs(int n,int cen){
	if(n < 4 ) return n+cen;
	int m = (int)sqrt(n*1.0);
	int ans = n+cen;
	for(int i=2;i<=m;i++){
		c[n/i] += (i-1)*c[n];
		c[n-n/i*(i-1)]+=c[n];
		int maxn = n-1;
		while(!c[maxn] ) maxn--;
		ans = min(ans,dfs(maxn,cen+(i-1)*c[n]));
		c[n/i] -= (i-1)*c[n];
		c[n-n/i*(i-1)]-=c[n];
	}
	return ans;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int tt = 1;tt <= T;tt++){
		int D,maxn = 0;
		memset(p,0,sizeof(p));
		memset(c,0,sizeof(c));
		scanf("%d",&D);
		//printf("%d\n",D);
		for(int i=0;i<D;i++){
			scanf("%d",&p[i]);
			//printf("%d ",p[i]);
			c[p[i]]++;
			maxn = max(maxn,p[i]);
		}
		//printf("\n");
		/*int ans =maxn,cen=0;
		while(maxn){
			cen += c[maxn];
			c[maxn/2] += c[maxn];
			c[maxn-maxn/2] += c[maxn];
			maxn--;
			while(!c[maxn]) maxn--;
			ans = min(ans,cen+maxn);
		}*/
		int ans = dfs(maxn,0);
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
