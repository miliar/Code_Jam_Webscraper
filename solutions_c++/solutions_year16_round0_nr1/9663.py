#include <cstdio>
#include <cstring>

int T;
long long N, now;
bool app[10];
int cnt;

int main() {
	scanf("%d", &T);
	for(int ti=1; ti<=T; ti++) {
		scanf("%lld", &N);
		memset(app, false, sizeof(app));
		cnt = 0;
		now = 0;
		if(N == 0) {
			printf("Case #%d: INSOMNIA\n", ti);
		}
		else {
			while(true) {
				now += N;
				if(now < 0) {
					printf("ERROR on %lld\n", N);
					while(1);
				}
				long long tnow = now;
				while(tnow > 0) {
					if(!app[tnow%10]) {
						app[tnow%10] = true;
						cnt ++;
					}
					tnow /= 10;
				}
				if(cnt >= 10) break;
			}
			printf("Case #%d: %lld\n", ti, now);
		}
	}
	return 0;
}