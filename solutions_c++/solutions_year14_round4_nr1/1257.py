#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdlib>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)

using namespace std;

typedef long long li;
typedef long double ld;

typedef pair<int,int> pt;
#define ft first
#define sc second

int n, x;
int s[10005];

bool read() {
	if (!(cin >> n >> x))
		return false;
	forn(i, n)
		cin >> s[i];
	return true;
}

void solve() {
	sort(s, s+n);
	int res = 0, l = 0, r = n-1;
	while (l <= r) {
		res++;
		if (s[r] + s[l] <= x)
			l++;
		r--;
	}
	cout << res;
}

int main() {
#ifdef dans
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

#ifdef TASK_NAME
	freopen(TASK_NAME ".in", "r", stdin);
	freopen(TASK_NAME ".out", "w", stdout);
#endif

	int t;
	cin >> t;
	t = 1;
	while (read()) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		++t;
	}
	
	return 0;
}

