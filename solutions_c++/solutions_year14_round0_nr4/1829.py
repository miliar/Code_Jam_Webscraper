#include <cstdio>
#include <algorithm>
using namespace std;
#define MAXN 1000

int main(){
	int T, N, lose;
	float Naomi[MAXN], Ken[MAXN];
	scanf("%d", &T);
	for(int cases=1;cases<=T;++cases){
		scanf("%d", &N);
		printf("Case #%d:", cases);
		for(int i=0;i<N;++i)
			scanf("%f", &Naomi[i]);
		for(int i=0;i<N;++i)
			scanf("%f", &Ken[i]);
		sort(Naomi, Naomi+N);
		sort(Ken, Ken+N);
		lose = 0;
		for(int i=N-1,j=N-1;j>=0;--j){
			if(Naomi[i]<Ken[j])
				++lose;
			else
				--i;
		}
		printf(" %d", N-lose);
		lose = 0;
		for(int i=0,j=0;j<N;++j){
			if(Ken[j]>Naomi[i]){
				++lose;
				++i;
			}
		}
		printf(" %d\n", N-lose);
	}
}
