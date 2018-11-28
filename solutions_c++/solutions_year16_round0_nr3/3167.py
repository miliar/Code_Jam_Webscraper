#include<bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')

typedef long long int lld;
const int INF = (1LL << 30) - 1;
const lld LINF = (1LL << 62) - 1;

int N, K;

int is_composite(lld x) {
	for (lld i = 2; i * 1LL * i <= x; i++)
		if (x % i == 0)
			return i;
	return 0;
}

bool is_okay(lld i) {
	for (int j = 2; j <= 10; j++) {
		lld aux = i;
		lld val = 0;
		lld p = 1;
		while (aux) {
			val += p * (aux % 2);
			aux /= 2;
			p *= j;
		}
		if (!is_composite(val))
			return 0;
	}
	return 1;
}

void print_binary(lld i) {
	if (i == 1) {printf("%d", 1); return;}
	print_binary(i / 2);
	printf("%d", (int)(i % 2));
}

void print_divisors(lld i, int j) {
	lld aux = i;
	lld val = 0;
	lld p = 1;
	while (aux) {
		val += p * (aux % 2);
		aux /= 2;
		p *= j;
	}
	printf("%d ", is_composite(val));
}

void solution() {
	scanf("%d%d", &N, &K);

	if (N <= 16)
		for (int i = (1 << (N - 1)) + 1; i <= (1 << N) - 1 && K; i += 2) {
			if (is_okay(i)) {
				print_binary(i);
				printf(" ");
				for (int j = 2; j <= 10; j++)
					print_divisors(i, j);
				printf("\n");
				K--;
			}
		}
	else {
		N /= 2;
		for (int i = (1 << (N - 1)) + 1; i <= (1 << N) - 1 && K; i += 2) {
			if (is_okay(i)) {
				print_binary(i);
				print_binary(i);
				printf(" ");
				for (int j = 2; j <= 10; j++)
					print_divisors(i, j);
				printf("\n");
				K--;
			}
		}
	}
}

int main() {
	cin.sync_with_stdio(false);

	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	int nrtests;

	scanf("%d", &nrtests);

	for (int testcase = 1; testcase <= nrtests; testcase++) {
		printf("Case #%d:\n", testcase);
		solution();
	}

	return 0;
}