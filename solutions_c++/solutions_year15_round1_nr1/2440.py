#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const int maxn =10010;
int T,N;

int d[maxn];

int max(int x,int y){return x>y?x:y;}
typedef long long LL;

LL firstWay(int d[],int n){
	int i;
	LL ret=0;
	for(i=1;i<n;i++){
		if(d[i]<d[i-1])ret+=d[i-1]-d[i];
	}
	return ret;
}

LL secondWay(int d[],int n){
	int i;
	LL ret=0;
	int rate=0;
	for(i=1;i<n;i++)rate=max(rate,d[i-1]-d[i]);
	for(i=0;i<n-1;i++){
		if(d[i]>=rate)ret+=rate;
		else ret+=d[i];
	}
	return ret;
}

int main()
{
	int i;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	int kcase=1;
	while(T-- && scanf("%d",&N)==1){

		for(i=0;i<N;i++)scanf("%d",&d[i]);
		printf("Case #%d: %lld %lld\n",kcase++,firstWay(d,N),secondWay(d,N));
	}
	return 0;
}
