#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int calc(const vector<double> &a, const vector<double> &b) {
	int n = a.size();
	int i = 0, j = 0, res = 0;
	while (i < n) {
		while (j < n && a[i] < b[j]) {
			j++;
		}
		if (j < n && a[i] > b[j]) {
			j++;
			res++;
		}
		i++;
	}
	return res;
}

void solve() {
	int n;
	scanf("%d", &n);
	vector<double> a(n), b(n);
	for (int i = 0; i < n; ++i) {
		scanf("%lf", &a[i]);
	}
	for (int i = 0; i < n; ++i) {
		scanf("%lf", &b[i]);
	}
	sort(a.rbegin(), a.rend());
	sort(b.rbegin(), b.rend());
	printf("%d %d\n", calc(a, b), n - calc(b, a));
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}