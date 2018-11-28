#include <stdio.h>
#include <algorithm>

long long to_N_from_10(long long n, bool rec = true)
{
	int c = 0;
	long long r = 0;
	long long d = n;
	long long k = 1;
	while (d) {
		r *= 10;
		r += d%10;
		d /= 10;
		if (d) {
			k *= 10;
		}
		c++;
	}
	
	long long res = n-k;
	if (rec && n%10 == 0) {
		res = std::min(res, to_N_from_10(n-1, false)+1);
	} else {
		for (int i=0; i<=c; i++) {
			long long q = 0;
			long long a = 1;
			long long b = 1;
			for (int j=0; j<i; j++) {
				a *= 10;
			}
			q += n%a;
			for (int j=i; j<c; j++) {
				b *= 10;
			}
			q += r%b;
			res = std::min(res, q);
		}
	}
	return res;
}


long long make9(int c)
{
	long long res = 0;
	for (int i=0; i<c; i++) {
		res *= 10;
		res += 9;
	}
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		long long N;
		scanf("%lld", &N);
		long long res = 1;
		long long d = N;
		int c = 0;
		while (d) {
			d /= 10;
			c++;
		}
		for (int i=1; i<c; i++) {
			res += to_N_from_10(make9(i));
			res++;
		}
		res += to_N_from_10(N);

		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}
