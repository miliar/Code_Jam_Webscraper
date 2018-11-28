#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <stdio.h>
typedef long long ll;
#define mset(a, val) memset(a, val, sizeof(a))
#define up(i, s, t) for (ll i = (s); i < (t); i += 1)
#define down(i, s, t) for (ll i = (s); i > (t); i -= 1)
#define rd1(a) scanf("%d", &a)
#define rd2(a, b) scanf("%d %d", &a, &b)
#define rd3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define rd4(a, b, c, d) scanf("%d %d %d %d", &a, &b, &c, &d)
#define pii pair<int, int>

using namespace std;
const int MAXINT = 0x6fffffff;
const ll MAXLONG = (ll) 1 << 63 - 1;
const int MAXN = 1005;

double ar1[MAXN], ar2[MAXN];
int n;

int deceive() {
	int s1, t1, s2, t2;
	s1 = s2 = 0;
	t1 = t2 = n - 1;
	int res = 0;
	up(i, 0, n) {
		if (ar1[t1] > ar2[t2]) {
			res ++;
			t1 --, t2 --;
		} else {
			s1 ++, t2 --;
		}
	}
	return res;
}

int war() {
	int res = 0;
	int s2 = 0;
	up(i, 0, n) {
		double v1 = ar1[i];
		while (s2 < n && ar2[s2] < v1) {
			s2 ++;
		}
		if (s2 >= n) {
			res ++;
		} else {
			s2 ++;
		}
	}
	return res;
}

int main () {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

	int t;
	cin >> t;
	up(ca, 1, t + 1) {
		cin >> n;
		up(i, 0, n) {
			cin >> ar1[i];
		}
		up(i, 0, n) {
			cin >> ar2[i];
		}

		sort(ar1, ar1 + n);
		sort(ar2, ar2 + n);

		int res1 = deceive();
		int res2 = war();

		printf("Case #%lld: %d %d\n", ca, res1, res2);
	}
    return 0;
}