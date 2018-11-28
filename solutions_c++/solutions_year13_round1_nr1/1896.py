#include <stdio.h>
#include <cmath>

typedef long long num;

long long calculate(num r, num n) {
	// N (2r + 2N - 1)
	return n * (2*n + 2*r - 1);
}

long long solve(long long r, long long t) {
	//2n^2 + N(2r-1) - t = 0
	long long b = 2 * r - 1;
	long long d = floor(sqrt(b * b + 4 * 2 * t));
	long long n = (-b + d) / 2 * 2;
	while (calculate(r, n + 1) <= t) n++;
	while (calculate(r, n) > t) n--;
	return n;
}

int main() {
	int c;
	long long r, t;
	scanf("%d", &c);
	for (int i = 0; i < c; i++) {
		scanf("%lld%lld", &r, &t);
		long long n = solve(r, t);
		printf("Case #%d: %lld\n", i+1, n);
	}
}

// p (r+1)^2 - p(r)^2=p(r + 1 - r) *  (r + 1 + r) = p(2r + 1)
// 2p(r+1)...2p(r+N)

// 2r + 1
// 2(r + 2) + 1
// 2(r + 4) + 1
// 2r + 5
// 2r + 9
// ..

// 2r + (N*4 - 3)

// (4r + 4N - 2) / 2 * N = t

// N (2r + 2N - 1) = t

 
 
// // 2p * N (N + 1 + 2r) / 2 = p N N+1+2r == p t

// N^2 + bN + b - t = 0

// -b sqrt(b^2 - 4 (b - t)) 