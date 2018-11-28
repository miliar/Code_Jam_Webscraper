#include <cstdio>
#include <cmath>

using namespace std;

typedef  unsigned long long i64;
const i64 M = 100000001;
i64 cnt[M];

bool pali(i64 x) {
	i64 t = x;
	i64 y = 0;
	while (t != 0) {
		y = y*10 + (t % 10);
		t /= 10;
	}
	return x == y;
}

void precalc() {
	cnt[0] = 1;
	for (i64 i = 1; i < M; ++i) {
		cnt[i] = cnt[i-1];
		if (pali(i) && pali(i*i)) cnt[i]++;
	}
}

int main() {
	precalc();
	int k;
	scanf("%d", &k);
	for (int t = 1; t <= k; ++t) {
		
		/*double A,B;
		scanf("%lf %lf", &A, &B);
		i64 a = (i64)sqrt(A);
		i64 b = (i64)sqrt(B);
		printf("%lld %lld", a, b);*/
		i64 A,B;
		scanf("%lld %lld", &A, &B);
		i64 a = (i64)sqrt(A);
		if (a*a < A) a++;
		i64 b = (i64)sqrt(B);
		
		printf("Case #%d: %lld\n", t, cnt[b]-cnt[a-1]);
	}
	
	return 0;
}
