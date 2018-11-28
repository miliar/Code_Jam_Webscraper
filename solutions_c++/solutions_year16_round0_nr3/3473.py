#include <stdio.h>
#include <iostream>
using namespace std;

#define MAXM (1000000)

int p[MAXM];
bool flag[MAXM];
int m, n, s;
long long a[15];
long long b[15];
long long ans[501][15];
int now;

void primes() {
	m = 0;
	int j;
	for (int i = 2;i < MAXM;++i) flag[i] = true;

	for (int i = 2;i < MAXM;++i)
		if (flag[i]) {
			p[m++] = i;
			j = i+i;
			while (j < MAXM) {
				flag[j] = false;
				j += i;
			}
		}
	//printf("%d\n", m);
}

int find_divisor(long long k) {
	for (int i = 0;i < m;++i) {
		if (p[i] >= k) return -1;
		if (k % p[i] == 0) return p[i];
	}
	return -1;
}

void check() {
	//printf("%d", a[10]);
	for (int i = 2;i <= 10;++i) {
		b[i] = find_divisor(a[i]);
		if (b[i] == -1) return;
	}
	ans[now][0] = a[10];
	for (int i = 2;i <= 10;++i)
		ans[now][i] = b[i];
	now++;
}

long long cal(int k, int p) {
	long long t = 1;
	long long ret =0;
	while (p > 0){
		if (p % 2 == 1)  ret += t;
		t *= k;
		p /= 2;
	}
	return ret;
}

int main() {
	int k;
//	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	primes();
	n = 16;
	s = 50;
	for (int i = 2;i <= 10;++i) {
		a[i] = 1;
		for (int j = 0;j < n-1;++j) a[i] *= i;
		a[i] += 1;
	}
	//printf("%lld", a[10]);
	now = 0;
	while (now < s) {
		check();
		a[2] += 2;
		for (int i = 3;i <= 10;++i) a[i] = cal(i, a[2]);
	}
	printf("Case #1:\n");
	for (int i = 0;i < s;++i) {
		printf("%lld", ans[i][0]);
		for (int j = 2;j <= 10;++j)
			printf(" %lld", ans[i][j]);
		printf("\n");
	}

}