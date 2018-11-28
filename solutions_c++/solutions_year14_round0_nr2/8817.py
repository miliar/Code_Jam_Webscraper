#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;

void solve() {
	double t, c, f, x;
	cin >> c >> f >> x;
	double ans = x / 2, temp = 0, l = 1;
	while((l <= 1000 * 10000 + 10) /*|| ((x / (l * f + 2) + c / ((l - 1) * f + 2) < x / ((l - 1) * f) + 2))*/) {
		temp += c / ((l - 1) * f + 2);
		ans = min(ans, temp + x / (l * f + 2));
		++l;
	} 
	/*l = (x * f - c) / (c * f);
	int i;
	for (i = 0; i < l - 1; ++i) {
		temp += c / (i * f + 2);
	}
	ans = temp + x / (i * f + 2);*/
	printf("%.7lf\n", ans);
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	
	return 0;
}
