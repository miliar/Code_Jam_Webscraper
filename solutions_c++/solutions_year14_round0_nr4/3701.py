#include <iostream> 
#include <cstdio> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <stack> 
#include <cmath> 
#include <algorithm> 
#include <cstring> 
#include <bitset> 
#include <ctime> 
#include <sstream>
#include <stack> 
#include <cassert> 
#include <list> 
//#include <unordered_set> 
using namespace std;
typedef long long li;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define mp make_pair 
#define pb push_back 
#define all(s) s.begin(), s.end() 
void solve();

#define NAME "changemeplease"
int main() {
#ifdef YA 
	cerr << NAME << endl;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout); 
	clock_t start = clock();
#else 
	freopen("input.txt", "r", stdin); 
	freopen("output.txt", "w", stdout); 
#endif 
	ios_base::sync_with_stdio(false);
	cout << fixed;
	cout.precision(10);
	int t = 1;
	cin >> t;	 
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

#ifdef YA 
	//cout << "\n\n\nTime:" << ((clock() - start) / 1.0 / CLOCKS_PER_SEC);
#endif 
	return 0;
}

int n;
set <ld> a[2];

int solve1() {
	int ans = 0;
	set <ld> b[2];
	for (int i = 0; i < 2; ++i)
		b[i] = a[i];
	for (set <ld>::iterator it = b[0].begin(); it != b[0].end(); ++it) {
		if (*it > *(--b[1].end())) {
			++ans;
			b[1].erase(--b[1].end());
		}
		else {
			b[1].erase(b[1].lower_bound(*it));
		}
	}
	return ans;
}

void solve() {
	cin >> n;
	for (int i = 0; i < 2; ++i) {
		a[i].clear();
		for (int j = 0; j < n; ++j) {
			ld x;
			cin >> x;
			a[i].insert(x);
		}
	}
	int res[2];
	res[0] = 0;
	res[1] = solve1();
	while (!a[0].empty()) {
		if (*a[0].begin() > *a[1].begin()) {
			++res[0];
			a[0].erase(a[0].begin());
			a[1].erase(a[1].begin());
		}
		else {
			a[0].erase(a[0].begin());
			a[1].erase(--a[1].end());
		}
	}
	cout << res[0] << " " << res[1] << "\n";
}