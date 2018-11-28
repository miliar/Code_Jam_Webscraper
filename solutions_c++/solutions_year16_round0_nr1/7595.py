#include <cstdio>

int T;

typedef long long LL;

int main(){
	freopen("A.txt", "w", stdout);
	LL N;
	scanf("%d", &T);
	int cas = 0;
	while(T--){
		scanf("%lld", &N);
		printf("Case #%d: ", ++cas);
		if(N == 0){
			printf("INSOMNIA\n");
			continue;
		}
		LL mask = 0;
		LL now = 0;
		while(mask < (1ll << 10) - 1){
			now += N;
			LL x = now;
			while(x){
				mask |= (1ll << (x % 10));
				x /= 10;
			}
		}
		printf("%lld\n", now);
	}
	return 0;
}
