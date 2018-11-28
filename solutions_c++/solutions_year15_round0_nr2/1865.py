#include <stdio.h>
#include <cstring>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <string.h>
int p[10001];
int n;
int f[1002][1002];
int min(int a,int b){return a<b?a:b;}
int max(int a,int b){return a>b?a:b;}
int dp(){
	int i,j,k,sum,res;
	sum = 0;
	res = 2147483647;
	memset(f,0,sizeof(f));
	for(i=1;i<=n;i++){
		sum+=p[i];
		for(j=0;j<=sum&&j<=1000;j++){
			f[i][j]=2147483647;
			for(k=0;k<p[i]&&k<=j;k++){
				f[i][j]=min(f[i][j], max(f[i-1][j-k], (p[i]-1)/(k+1)+1 ));
			}
			if(i==n){
				if(f[i][j] + j<res){
					res = f[i][j]+j;
				}
			}
		}
	}
	return res;
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,C;
	scanf("%d",&T);
	for(C=1;C<=T;C++){
		printf("Case #%d: ",C);
		scanf("%d",&n);
		for(int i=1;i<=n;i++) scanf("%d",&p[i]);
		printf("%d\n",dp());
		fflush(stdout);
	}
}