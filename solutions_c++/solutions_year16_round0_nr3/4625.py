/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

int MN;

int n, j;
int have;
int d[20];

long long getFactor(long long x) {
	long long i;
	for (i = 2; i * i <= x; ++i) {
		if (x % i == 0) return i;
	}
	return -1;
}

void getAnswer() {
	int i, j;
	vector<long long> v;
	for (i = 2; i <= 10; ++i) {
		long long cur = 0;
		for (j = 0; j < MN; ++j) {
			cur = cur * i + d[j];
		}
		long long factor = getFactor(cur);
		if (factor == -1) return ;
		v.push_back(factor);
	}
	for (i = 0; i < MN; ++i ) printf("%d", d[i]);
	for (auto &x : v) printf(" %lld", x);
	puts("");
	++have;
}

void getFactors(int i = 0) {
	if (have >= j) return ;
	if (i == MN) {
		getAnswer();
		return ;
	}

	if (i != 0 && i != MN - 1) {
		d[i] = 0;
		getFactors(i + 1);
	}
	d[i] = 1;
	getFactors(i + 1);
}

int main() {
	freopen("output.txt", "w", stdout);

	scanf("%d", &n);
	scanf("%d %d", &n, &j);
	MN = n;

	puts("Case #1:");
	getFactors();
	return 0;
}
