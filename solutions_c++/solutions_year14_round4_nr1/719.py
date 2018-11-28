#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define foreach(e, x) for (__typeof(x.begin()) e = x.begin(); e != x.end(); e++)
typedef long long LL;
typedef pair<int, int> PII;

int t, x, n;
int s[10000];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	REP(test, t) {
		cin >> n >> x;
		REP(i, n)
			cin >> s[i];
		sort(s, s + n);
		int l = 0, r = n - 1;
		int ans = 0;
		while (l < r) {
			if (s[l] + s[r] <= x)
				++l;
			--r;
			++ans;
		}
		if (l == r)
			++ans;
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}
