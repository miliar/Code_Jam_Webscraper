#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <numeric>
#define rep(x, to) for (int x = 0; x < (to); x++)
#define REP(x, a, to) for (int x = (a); x < (to); x++)
#define foreach(itr, x) for (typeof((x).begin()) itr = (x).begin(); itr != (x).end(); itr++)

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<long, long> PLL;

int T;
string GAB = "GABRIEL";
string RIC = "RICHARD";

int main() {
	cin >> T;
	rep(cnt, T) {
		int X, R, C;
		string ans;
		cin >> X >> R >> C;
		if (X == 1) {
			ans = GAB;
		} else if (X == 2) {
			if (R * C % 2 == 0) ans = GAB;
			else ans = RIC;
		} else if (X == 3) {
			if (R * C == 6 || R * C == 12 || R * C == 9) ans = GAB;
			else ans = RIC;
		} else {
			if (R * C == 12 || R * C == 16) ans = GAB;
			else ans = RIC;
		}
		printf("Case #%d: %s\n", cnt + 1, ans.c_str());
	}
	return 0;
}


