#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

int gao1(double a[], double b[], int n) {
	int ret = 0;
	int beginB = 0, endB = n - 1;
	for (int i = 0; i < n; ++i) {
		if (a[i] > b[beginB]) {
			beginB++;
			++ret;
		} else {
			endB--;
		}
	}
	return ret;
}

int gao2(double a[], double b[], int n) {
	set<double> st(b, b + n);
	int ret = 0;	
	for (int i = 0; i < n; ++i) {
		auto it = st.lower_bound(a[i]);
		if (it == st.end()) {
			st.erase(*st.begin());
			++ret;
		} else {
			st.erase(*it);
		}
	}
	return ret;
}

int main() {
	int Tc;
	int n;
	double a[10000], b[10000];
	scanf("%d", &Tc);
	for (int re = 1; re <= Tc; ++re) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%lf", a + i);
		}
		for (int i = 0; i < n; ++i) {
			scanf("%lf", b + i);
		}
		sort(a, a + n);
		sort(b, b + n);
		printf("Case #%d: %d %d\n", re, gao1(a, b, n), gao2(a, b, n));
	}
	return 0;
}