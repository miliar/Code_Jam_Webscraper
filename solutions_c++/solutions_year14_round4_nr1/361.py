#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 10010
int n,v[maxn],cap;
int main()
{
	int t,cas;
	int i,j,k;
	freopen("1.in","r",stdin), freopen("1.out","w",stdout);
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d%d",&n,&cap);
		for(i=1;i<=n;i++){
			scanf("%d",&v[i]);
		}
		sort(v+1,v+n+1);
		int st=1;
		int cnt=0;
		for(i=n;i>st;i--){
			if(v[i]+v[st]<=cap){
				st++;
			}
			cnt++;
		}
		if(i>=st)cnt++;
		printf("Case #%d: %d\n",cas,cnt);
	}
	return 0;
}
