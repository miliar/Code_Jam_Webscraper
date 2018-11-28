#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;
const int maxn = 1001;
double a[maxn], b[maxn];
int n;

void readWeight(double* x) {
	for (int i = 1; i <= n; i++) {
		scanf("%lf", x + i);
	}
	sort(x + 1, x + n + 1);
	return;
}

void init() {
	scanf("%d", &n);
	readWeight(a);
	readWeight(b);
	return;
}

int calcNormalBest() {
	int ans = 0;
	set<double> tb;
	for (int i = 1; i <= n; i++) {
		tb.insert(b[i]);
	}
	for (int i = n; i >= 1; i--) {
		set<double>::iterator it = tb.lower_bound(a[i]);
		if (it == tb.end()) {
			ans++;
			tb.erase(tb.begin());
		} else {
			tb.erase(it);
		}
	}
	return ans;
}

int calcBest(int ast, int ben) {
	int ans = 0;
	set<double> ta, tb;
	for (int i = ast; i <= n; i++) {
		ta.insert(a[i]);
	}
	for (int i = 1; i <= ben; i++) {
		tb.insert(b[i]);
	}
	for (int i = ast; i <= n; i++) {
		set<double>::iterator it = ta.lower_bound(*tb.begin());
		if (it == ta.end()) {
			set<double>::iterator large = tb.end();
			large--;
			ta.erase(ta.begin());
			tb.erase(large);
		} else {
			ta.erase(it);
			tb.erase(tb.begin());
			ans++;
		}
	}
	return ans;
}

void calc() {
	int normal = calcNormalBest();
	int best = max(normal, calcBest(1, n));
	int curast = 1;
	int curben = n;
	while (true) {
		curast++;
		curben--;
		if (curast > n) {
			break;
		}
		best = max(best, calcBest(curast, curben));
	}
	printf("%d %d\n", best, normal);
	return;
}

int main() {
	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; i++) {
		init();
		printf("Case #%d: ", i);
		calc();
	}
	return 0;
}