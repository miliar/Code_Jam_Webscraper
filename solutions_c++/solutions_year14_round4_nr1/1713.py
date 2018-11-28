#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <string.h>
#include <math.h>
#include <sstream>
#include <stdio.h>

using namespace std;
typedef long long ll;
const int maxn = 2 * 100000 + 10, MOD = 1000 * 1000 * 1000 + 7, INF = 1000 * 1000 * 1000;
const ll LINF = (1ll) << 30;
#define pB push_back
#define mP make_pair
#define X first
#define Y second
#define pii pair<int, int>
#define endl "\n"
#define show(x) {cout << (#x) << " = " << x << endl;}
const double EPS = 1e-9, PI = 2. * acos(0.0);

multiset <int> all;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	// ios_base::sync_with_stdio(false);
	int test; cin >> test;
	int testNum = 1;
	while(test--) {
		// cout << "here" << endl;
		int n; cin >> n;
		int x; cin >> x;
		all.clear();
		// cout << "wh" << endl;
		for (int i = 0; i < n; ++i) {
			int temp; cin >> temp;
			all.insert(temp);
			// show(temp);
		}
		int ans = 0;
		// cout << "here2" << endl;
		while(!all.empty()) {
			if((int)all.size() == 1) {
				ans++;
				break;
			}
			multiset <int> :: iterator me, nx;
			me = all.begin();
			nx = all.lower_bound(x - (*me) + 1); 
			if(nx == me) {
				ans += (int) all.size();
				break;
			}
			nx--;
			// show(*me);
			// show(*nx);
			if(me == nx) {
				ans += (int) all.size();
				break;
			}
			else {
				all.erase(me);
				all.erase(nx);
				ans++;	
			}
		}

		cout << "Case #" << testNum++ << ": " << ans << endl;

	}
	
	
	return 0;
}

