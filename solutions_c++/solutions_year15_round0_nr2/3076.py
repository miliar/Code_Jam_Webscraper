#include <cstdio>
const int N = 1010;
int P[N];
int calc(int A, int T){
	return (A+T-1)/T-1;
}
int min(int a,int b){return a<b?a:b;}
int max(int a,int b){return a>b?a:b;}
int main(){
	int T;
	scanf("%d",&T);
	int count = 0;
	while(count++ < T){
		int D;
		scanf("%d",&D);
		int M = 0;
		for(int i=0;i<D;i++){
			scanf("%d",&P[i]);
			M = max(P[i],M);
		}
		int best = 1<<20;
		for(int i=1;i<=M;i++){
			int ans = i;
			for(int j=0;j<D;j++){
				ans += calc(P[j],i);
			}
			best = min(ans,best);
		}
		printf("Case #%d: %d\n",count,best);
		
	}

}
