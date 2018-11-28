#include <cstdio>
#include <iostream>

using namespace std;

int check_pow2(int q) {
	if(q == 1) return 0;
	if(q % 2 == 1) return -1;
	return check_pow2(q / 2) + 1;
}
int num_bin_dig(int p) {
	if(p <= 1) return 1;
	return 1 + num_bin_dig(p / 2);
}
int max(int p, int q) {
	return (p > q ? p : q);
}
int min(int p, int q) {
	return p + q - max(p, q);
}
int gcd(int p, int q) {
	if(p == 0 || q == 0) return p + q;
	if(p == 1 || q == 1) return 1;
	return gcd(max(p, q) % min(p, q), min(p, q));
}

int main(void) {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int x = 1; x <= t; x++) {
		int p, q;
		scanf("%d/%d", &p, &q);
		int d = gcd(p, q);
		p /= d;
		q /= d;
		int beta = check_pow2(q);
		if(beta == -1 || beta > 40) printf("Case #%d: impossible\n", x);
		else {
			int f = num_bin_dig(p);
			if(beta - f + 1 >= 0) printf("Case #%d: %d\n", x, beta - f + 1);
			else printf("Case #%d: impossible\n", x);
		}
	}
	return 0;
}
