#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <queue>
#include <bitset>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <limits>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<int, double> PID;
typedef pair<double, double> PDD;

#define pb(x) push_back(x)
#define X first
#define Y second

int T, cases, n;
double x;
set<double> a, b, c;

int main(){
	for (scanf("%d", &T), cases = 1; cases <= T; ++cases) {
		printf("Case #%d: ", cases);
		scanf("%d", &n);
		a.clear(); b.clear();
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &x);
			a.insert(x);
		}
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &x);
			b.insert(x);
		}
		c = a;

		int cnt = 0;
		for (auto iter = b.begin(); iter != b.end(); ++iter) {
			auto target = c.upper_bound(*iter);
			if (target == c.end()) break;
			c.erase(target);
			++cnt;
		}
		printf("%d ", cnt);

		cnt = 0;
		for (auto iter = a.begin(); iter != a.end(); ++iter) {
			auto target = b.upper_bound(*iter);
			if (target == b.end()) {
				++cnt;
				b.erase(b.begin());
			} else {
				b.erase(target);
			}
		}
		printf("%d\n", cnt);
	}
}
