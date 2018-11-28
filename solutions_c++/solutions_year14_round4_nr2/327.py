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

const int MAXN = 1005;

int n, a[MAXN], b[MAXN];

void solve() {
	cout << "Case #" << CASE << ": ";
	
	for(int i = 0; i < n; i++) {
		b[i] = a[i];
	}
	sort(b,b+n);
	int ans = 0;
	int l = 0, r = n-1;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++) {
			if(a[j] == b[i]) {
				if(j-l < r-j) {
					ans += j-l;
					for(int k = j-1; k >= l; k--) {
						swap(a[k],a[k+1]);
					}
					l++;
				} else {
					ans += r-j;
					for(int k = j+1; k <= r; k++) {
						swap(a[k],a[k-1]);
					}
					r--;
				}
				break;
			}
		}
	}
	cout << ans << endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		cin >> n;
		for(int i = 0; i < n; i++) {
			cin >> a[i];
		}
		solve();
	}
}
