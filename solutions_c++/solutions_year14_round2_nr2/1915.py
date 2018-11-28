#include <cstdio>

int main() {
	int T,A,B,K,sum;
	scanf("%d",&T);
	for(int z=1;z<=T;z++) {
		scanf("%d%d%d",&A,&B,&K);
		sum = 0;
		for(int a=0;a<A;a++) for(int b=0;b<B;b++) 
			if((a&b)<K) sum++;
		printf("Case #%d: %d\n",z,sum);
	}
	return 0;
}
