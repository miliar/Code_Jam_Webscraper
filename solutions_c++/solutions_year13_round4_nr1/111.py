#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

const int MOD = 1000002013;

int n, m;
map<int, int> enter, leave;
map<int, int> cards;
int ans;

int CalcMoney(int l, int r, int cnt = 1) {
	int d = r - l;
	int64 x = int64(n)*d + (int64(d-1)*d)/2;
	x %= MOD;
	x *= cnt;
	x %= MOD;
	return int(x);
};

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &n, &m);
		ans = 0;
		enter.clear();
		leave.clear();
		for (int i = 0; i<m; i++) {
			int l, r, num;
			scanf("%d%d%d", &l, &r, &num);
			enter[l] += num;
			leave[r] += num;
			ans = (ans + MOD - CalcMoney(l, r, num)) % MOD;
		}

		cards.clear();
		auto eit = enter.begin();
		auto lit = leave.begin();
		while (eit != enter.end() || lit != leave.end()) {
			bool doenter;
			if (eit == enter.end()) doenter = false;
			else if (lit == leave.end()) doenter = true;
			else if (lit->first != eit->first) doenter = (eit->first < lit->first);
			else doenter = true;

			if (doenter) {
				int pos = eit->first;
				cards[pos] += eit->second;
				eit++;
			}
			else {
				int pos = lit->first;
				int rem = lit->second;
				while (rem > 0) {
					auto cit = cards.end(); cit--;
					int dd = min(rem, cit->second);
					ans = (ans + CalcMoney(cit->first, pos, dd)) % MOD;
					rem -= dd;
					cit->second -= dd;
					if (cit->second == 0) cards.erase(cit);
				}
				lit++;
			}
		}

		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
