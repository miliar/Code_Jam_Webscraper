#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

const int N = 1000 + 10;

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; ++ t) {
		int n;
		scanf("%d", &n);

		std::vector<double> a;
		for (int i = 1; i <= n; ++ i) {
			double x;
			scanf("%lf", &x);
			a.push_back(x);
		}
		std::vector<double> b;
		for (int i = 1; i <= n; ++ i) {
			double x;
			scanf("%lf", &x);
			b.push_back(x);
		}
		std::sort(a.begin(), a.end());
		std::sort(b.begin(), b.end());

		int res_0 = 0;
		int lower = 0, upper = n - 1;
		for (int i = 0; i < n; ++ i) {
			if (a[i] > b[lower]) {
				res_0 ++;
				lower ++;
			} else {
				upper --;
			}
		}

		int res_1 = 0;
		std::set<double> set;
		for (int i = 0; i < n; ++ i) {
			set.insert(b[i]);
		} 
		for (int i = 0; i < n; ++ i) {
			__typeof(set.begin()) iter = set.lower_bound(a[i]);
			if (iter == set.end()) {
				res_1 ++;
			} else {
				set.erase(iter);
			}
		}
		printf("Case #%d: %d %d\n", t, res_0, res_1);
	}
	return 0;
}
