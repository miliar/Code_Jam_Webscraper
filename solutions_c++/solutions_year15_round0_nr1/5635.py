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

int main() {
	cin >> T;
	rep(cnt, T) {
		int S;
		int sum = 0;
		int ans = 0;
		cin >> S;
		rep(i, S + 1) {
			int x;
			scanf("%1d", &x);
			if (x > 0 && sum < i) {
				ans += (i - sum);
				sum += (i - sum);
			}
			sum += x;
		}
		printf("Case #%d: %d\n", cnt + 1, ans);
	}
	return 0;
}


