#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <map>
#include <set>
#include <stack>
#include <queue>
using namespace std;

typedef long long		ll;
typedef pair<int, int> 	ii;
typedef vector<ii>		vii;
typedef vector<int>		vi;
typedef set<int>		si;
typedef map<string, int>msi;

#define INF 1000000000
#define DEBUG true
#define REP(i, n) \
	for (int i = 0; i < int(n); i++) //i is local
#define TRvi(c, it) \
	for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
	for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
	for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define pb push_back

bool isValid (string s) {
	bool used [1000] = {0};
	char active = 0;
	for (int i = 0; i < s.size(); i++) {
		char chr = s[i];
		if (chr != active && used[chr]) {
			return false;
		}
		active = chr;
		used[chr] = true;
	}
	return true;
}

int lala (string cur, vector<string> xs, vector<bool> taken, int n) {
	bool allTaken = true;
	REP(i, n) {
		allTaken = allTaken && taken[i];
	}
	if (allTaken) {
		if (isValid(cur)) {
			return 1;
		} else {
			return 0;
		}
	} else {
		if (isValid(cur)) {
			int ans = 0;
			REP(i, n) {
				if (!taken[i]) {
					string tmp = cur + xs[i];
					vector<bool> taken2 (taken);
					taken2[i] = true;
					ans += lala(tmp, xs, taken2, n);
				}
			}
			return ans;
		} else {
			return 0;
		}
	}
}

void Solve() {
	int n;
	scanf("%d ", &n);
	vector<string> xs;
	REP(i, n) {
		string x;
		cin >> x;
		xs.pb(x);
	}
	vector<bool> taken(n);
	int ans = lala("", xs, taken, n);
	printf("%d", ans);
}

int main() {
	int T; int nCase = 1;
	scanf("%d ", &T);
	while (T--) {
		printf("Case #%d: ", nCase++);
		Solve();
		printf("\n");
	}
	return 0;
}