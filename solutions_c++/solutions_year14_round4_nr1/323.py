#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

int TESTS, CASE;

const int MAXN = 10005;

int n, x, a[MAXN];
map<int,int,greater<int> > M;

void solve() {
	cout << "Case #" << CASE << ": ";
	M.clear();
	int cnt = 0;
	for(int i = 0; i < n; i++) {
		if(a[i]*2>x) {
			M[a[i]]++;
			cnt++;
		}
	}
	int ans = 0;
	sort(a,a+n);
	bool carry = 0;
	for(int i = n-1; i >= 0; i--) {
		if(a[i]*2<=x) {
			map<int,int,greater<int> >::iterator it = M.lower_bound(x-a[i]);
			if(it != M.end()) {
				ans++;
				(it->snd)--;
				cnt--;
				if((it->snd) == 0) {
					M.erase(it);
				}
			} else {
				if(carry) {
					ans++;
					carry = 0;
				} else {
					carry = 1;
				}
			}
		}
	}
	ans += cnt;
	ans += carry;
	cout << ans << endl;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		cin >> n >> x;
		for(int i = 0; i < n; i++) {
			cin >> a[i];
		}
		solve();
	}
}
