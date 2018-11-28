#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <queue>
using namespace std;

const int maxn=10000000;

int dis[maxn+5];

int reverse(int x){
	int ans=0;
	while(x){
		ans=ans*10+x%10;
		x/=10;
	}
	return ans;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("ASMALL.txt","w",stdout);
	for(int i=1;i<=maxn;i++)
		dis[i]=INT_MAX/2;
	dis[1]=1;
	queue<int> q;
	q.push(1);
	while(!q.empty()){
		int x=q.front();q.pop();
		if(x+1<=maxn&&dis[x+1]>dis[x]+1){
			dis[x+1]=dis[x]+1;
			q.push(x+1);
		}
		int rev=reverse(x);
		if(rev<=maxn&&dis[rev]>dis[x]+1){
			dis[rev]=dis[x]+1;
			q.push(rev);
		}
	}
	int T,Case=1;
	for(scanf("%d",&T);Case<=T;Case++){
		int tmp;
		scanf("%d",&tmp);
		printf("Case #%d: %d\n",Case,dis[tmp]);
	}
    return 0;
}

