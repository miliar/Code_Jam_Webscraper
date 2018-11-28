#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long int llu;
#define SIZE 100000000
long long c[100];

static inline llu trans(llu num, llu p) {
	llu ret = 0;
	for (llu i = 1; num != 0; i *= p) {
		ret += i*(num%10);
		num /= 10;
	}
	return ret;
}
llu ans[10];
llu t;
static inline bool is_prime(llu n) {
	if (n == 2)
		true;
	for (t = 2; t*t <= n; t++)
		if (n % t == 0)
			return false;
	return true;
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	FILE *fp = fopen("output.text", "w");
	int cnt = 0;
	int tc;
	cin >> tc;
	int N, J;
	cin >> N >> J;
	llu num = (1 << (N - 1)) + 1;
	llu temp;
	int idx;
	fprintf(fp,"Case #1:\n");
	llu now;
	bool prime;
	bool flag;
	while (true) {
		if (cnt == J)
			break;
		temp = 0;
		for (int i = 0; i < N; i++)
			if ((1llu << i)&num)
				temp += pow(10, i);
		prime = false;
		idx = 0;
		for (int k = 2; k <= 10; k++) {
			now = trans(temp, k);
			if (is_prime(now)) {
				prime = true;
				break;
			}
			else
				ans[idx++] = t;
		}
		if (!prime) {
			fprintf(fp,"%llu", temp);
			for (int i = 0; i <idx; i++)
				fprintf(fp," %llu", ans[i]);
			fprintf(fp,"\n");
			cnt++;
		}
		num += 2;
	}
	return 0;
}