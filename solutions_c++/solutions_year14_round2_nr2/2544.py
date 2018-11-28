#include <stdio.h>
int main(){
	int T;
	int A, B, K;
	scanf("%d", &T);
	for(int i=1;i<=T;++i){
		scanf("%d%d%d", &A, &B, &K);
		int cnt = 0;
		for(int j=0;j<A;++j){
			for(int k=0;k<B;++k){
				int and_ = j&k;
				if(and_ < K){
					++cnt;
				}
			}
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}
