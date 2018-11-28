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

ld c, f, x;

ld getans(int n) {
	ld ans = 0;
	for (int i = 0; i <= n; ++i) {
		ans += c / (2.0 + ld(i) * f);
	}
	ans += x / (2.0 + ld(n + 1) * f);
	return ans;
}

void solve() {
	cin >> c >> f >> x;
	ld ans = x / 2.0;
	if (c >= x) {
		cout << ans << endl;
		return;
	}
	int n =	int(((x - c) * (2.0 + f) - 2 * x) / f / c);
	for (int i = max(n - 2, 0); i <= n + 2; ++i)
		ans = min(ans, getans(i));
	cout << ans << "\n";
}