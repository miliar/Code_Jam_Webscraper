#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

const int MAXN = 1000;
int n, m;
double a[MAXN];
double v[MAXN];
int b[MAXN];

double dp(int size, int t) {
	double f[2][(MAXN << 1) + 3];
	memset(f, 0, sizeof(f));
	int a = 0, b = 1;
	f[0][0] = 1;
	for (int i = 0; i < size; ++i) {
		memset(f[b], 0, sizeof(f[b]));
		for (int j = 0; j < i + 1; ++j) {
			f[b][j] += f[a][j] * (1 - v[i]);
			f[b][j + 1] += f[a][j] * v[i];
		}
		swap(b, a);
	}
	return f[a][t];
}

void Work() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		scanf("%lf", &a[i]);

	sort(a, a + n);
	double ret = 0.0;
	for (int i = 0; i < m + 1; ++i) {
		int idx = 0;

		for (int j = 0; j < i; ++j)
			v[idx++] = a[j];
		for (int j = 0; j < m - i; ++j)
			v[idx++] = a[n - j - 1];
		ret = max(ret, dp(idx, m >> 1));
	}
	printf("%.8f", ret);
}

int main(int argc, char** argv) {
	int case_number;
	scanf("%d", &case_number);
	for (int i = 0; i < case_number; i++) {
		printf("Case #%d: ", i + 1);
		Work();
		printf("\n");
	}
	return 0;
}
