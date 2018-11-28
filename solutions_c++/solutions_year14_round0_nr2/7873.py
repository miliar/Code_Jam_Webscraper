#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define maxn 1000005
using namespace std;

int N,M,d[maxn],e[maxn];

void init()
{
	memset(d,0,sizeof(d)),memset(e,0,sizeof(e));
	scanf("%d",&N);
	for (int i=1,x,y; i<N; i++) scanf("%d%d",&x,&y),e[x]++,e[y]++;
	scanf("%d",&M);
	for (int i=1,x,y; i<M; i++) scanf("%d%d",&x,&y),d[x]++,d[y]++;
}

bool check()
{
	int s=0;
	for (int i=1; i<=M; i++) if (d[i]>1) if (d[i]!=M-1) return 1; else s++;
	if (s>1) return 1;
	if (M==1) return 0;
	if (M==2) return N<=4?0:1;
	else if (M==3)
	{
		if (N!=4) return 1;
		return *max_element(e+1,e+N+1)<=2;
	}
	return 1;
}

int main()
{
	int T;
	scanf("%d",&T);
	for (int i=1; i<=T; i++)
	{
		init();
		printf("Case %d: %s\n",i,check()?"YES":"NO");
	}
	return 0;
}
