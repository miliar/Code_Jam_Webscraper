#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <iostream>
#include <sstream>
#include <cctype>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;

void solve() {
	int n;
	vector<int> v;
	cin >> n;
	REP(i, n) {
		int x; cin >> x;
		v.push_back(x);
	}
	int res = INT_MAX;
	FOR (i, 1, 1000) {
		int cnt = i;
		REP(j, v.size()) cnt += v[j]/i + (v[j]%i!=0) - 1;
		res = min(res, cnt);
	}
	printf("%d\n", res);
}

int main() {
	int t; scanf("%d", &t);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
