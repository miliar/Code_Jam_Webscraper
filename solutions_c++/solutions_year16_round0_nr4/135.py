#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iostream>
#define MAXN 100050
#define LL long long
using namespace std;
LL qpow(LL a,LL b){
	LL res=1;
	while(b){
		if(b&1)res*=a;
		a*=a;
		b>>=1;
	}
	return res;
}
LL ans[111];
void solve(LL k,LL c,LL s){
	if(c==1){
		if(k==s){
			for(int i=1;i<=k;++i)
				printf(" %d",i);
			puts("");
		}else
			puts(" IMPOSSIBLE");
		return;
	}
	LL n=qpow(k,c);
	int cnt=0;
	LL now=0;
	int tail=0;
	while(cnt<k&&tail<s){
		int x=c-1;
		LL y=0;
		LL bas=qpow(k,c-1);
		while(x>0){
			x--;
			if(cnt<k)
				cnt++;
			y+=bas*(cnt-1);
			bas/=k;
		}
		if(cnt<k)cnt++;
		y+=cnt;

		ans[tail++]=y;
		now=qpow(k,c-1)*cnt;
	}
	if(cnt==k){
		for(int i=0;i<tail;++i)
			printf(" %I64d",ans[i]);
		printf("\n");
	}else{
		puts(" IMPOSSIBLE");
	}
}
int main() {
	freopen("D-large.in","r",stdin);
	freopen("D-large.txt","w",stdout);

	int tt,ri=0;
	scanf("%d",&tt);
	while(tt--){
		LL K,C,S;
		scanf("%I64d %I64d %I64d",&K,&C,&S);
		printf("Case #%d:",++ri);
		solve(K,C,S);

	}
	return 0;
}
