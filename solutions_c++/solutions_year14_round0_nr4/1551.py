#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int step1(vector<double>& a, vector<double>& b) {
	sort(a.begin(), a.end()); sort(b.begin(), b.end());
	size_t head = 0, tail = b.size() - 1;

	int ret = 0;
	for (size_t i = 0; i < a.size(); ++i) {
		if (a[i] > b[tail]) ret++, tail--;
		else if (a[i] > b[head]) ret++, head++;
		else tail--;
	}

	return ret;
}

int step2(vector<double>& a, vector<double>& b) {
	sort(a.begin(), a.end()); sort(b.begin(), b.end());
	size_t p = 0;

	int ret = 0;
	for (size_t i = 0; i < a.size(); ++i) {
		while (p < b.size() && b[p] <= a[i]) p++;
		if (p < b.size() && a[i] < b[p]) p++; else ret++;
	}

	return ret;
}

int main() {
	int T; scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		vector<double> a, b; int n; scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			double x; scanf("%lf", &x); a.push_back(x);
		}
		for (int i = 0; i < n; ++i) {
			double x; scanf("%lf", &x); b.push_back(x);
		}
		printf("Case #%d: %d %d\n", t, step1(a, b), step2(a, b));
	}

	return 0;
}
