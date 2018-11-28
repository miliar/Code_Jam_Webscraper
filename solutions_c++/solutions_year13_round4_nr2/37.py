#include <cstdio>
#include <algorithm>

int main(){

	int T;
	scanf("%d" ,&T);

	for(int t = 1; t <= T; t++){

		printf("Case #%d: " ,t);

		int n;
		long long p;
		scanf("%d %lld" ,&n ,&p);

		int cnt = 0;
		long long sum = 0, now = 1LL << n;
		while(sum + now / 2 < p && now){
			cnt++;
			sum += now / 2;
			now >>= 1;
		}
		//printf("--- %d %lld %lld\n" ,cnt ,sum ,now);

		long long mx = std::min((1LL << (cnt + 1)) - 2, (1LL << n) - 1);

		cnt = 0, now = 1LL << n;
		while(now > p) cnt++, now >>= 1;

		long long mx2 = (1LL << n) - (1LL << cnt);
		printf("%lld %lld\n" ,mx ,mx2);

	}

}
