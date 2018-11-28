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
#include <cstring>

using namespace std;

typedef pair<int, int> PP;
typedef long long LL;
#define pb push_back
#define fr first
#define sc second
int n, a[10000];
vector<int> x;

void f(){
	cin >> n;
	x.clear();
	map<int, int> p;
	for (int i = 0; i < n; i ++) cin >> a[i], p[a[i]] = i, x.pb(a[i]);
	if (n <= 2) {
		cout << 0 << endl; return;
	}
	sort(x.begin(), x.end());
	int res = 0;
	int lp = 0, rp = 0;
	for (int i = 0; i < n; i ++) {
		int ll, rr;
		for (ll = 0; ll < lp && a[ll] <= x[i]; ll ++);
		for (rr = 0; rr < rp && a[n - 1 - rr] <= x[i]; rr ++);
		if (p[x[i]] - ll < n - 1 - rr - p[x[i]]) {
			res += p[x[i]] - ll;
			for (int k = ll; k < p[x[i]]; k ++) p[a[k]] ++;
			for (int k = p[x[i]] - 1; k >= ll; k --) a[k + 1] = a[k];
			a[ll] = x[i];
			p[x[i]] = ll;
			lp ++;
		}
		else {
			res += n - 1 - rr - p[x[i]];
			for (int k = n - 1 - rr; k > p[x[i]]; k --) p[a[k]] --;
			for (int k = p[x[i]]; k < n - 1 - rr; k ++) a[k] = a[k + 1];
			a[n - 1 - rr] = x[i];
			p[x[i]] = n - 1 - rr;
			rp ++;
		}
	}
	cout << res << endl;
}
int main() {
	#ifdef _TEST_
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	#endif
	int testcase; 
	cin >> testcase;
	for (int i = 0; i < testcase; i ++) {
		cout << "Case #" << i + 1 <<": ";
		f();
	}

	return 0;
}

