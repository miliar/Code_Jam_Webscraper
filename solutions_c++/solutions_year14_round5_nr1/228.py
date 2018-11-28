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
#include <deque>
//#include <unordered_set> 
using namespace std;
typedef long long li;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define mp make_pair 
#define pb push_back
#define y1 botva
#define all(s) s.begin(), s.end() 
void solve();

#define NAME "changemeplease"
int main() {
#ifdef YA 
	//cerr << NAME << endl;
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

#define int li

void solve() {            
	li n, p, q, r, s;
	cin >> n >> p >> q >> r >> s;
	vector <int> a;
	a.resize(n);
	vector <li> pref;
	pref.assign(n, 0);
	for (int i = 0; i < n; ++i) {
		a[i] = (li(i) * p + q) % r + s;
		if (i == 0)
			pref[i] = a[i];
		else {
			pref[i] = pref[i - 1] + a[i];
		}
	}

	li ans = 0;

	for (int i = 0; i < n; ++i) {
		ans = max(ans, min(pref[i], pref[n - 1] - pref[i]));
	}
	
	/*for (int i = 1; i < n - 1; ++i)
		for (int j = 1; j < n - 1; ++j) {
			li sum1 = pref[i - 1];
			li sum2 = pref[n - 1] - pref[j];
			li sum3 = pref[n - 1] - sum1 - sum2;
			ans = max(ans, pref[n - 1] - max(sum1, max(sum2, sum3)));
		}*/

	int uk = 0;
	for (int i = 0; i < n - 1; ++i) {
		li tmp = pref[n - 1] - pref[i];
		if (pref[i] <= tmp)
			ans = max(ans, pref[i]);
		else {
			while (uk < i && pref[uk + 1] <= tmp)
				++uk;
			while (uk >= 1 && pref[uk] > tmp)
				--uk;

			if (pref[uk] <= tmp && pref[i] - pref[uk] <= tmp) {
				ans = max(ans, pref[i]);
			}
		}
	}


	uk = n - 1;
	for (int i = n - 1; i >= 1; --i) {
		li tmp = pref[i - 1];
		if (pref[n - 1] - pref[i - 1] <= tmp)
			ans = max(ans, pref[n - 1] - pref[i - 1]);
		else {
			while (uk > i && pref[n - 1] - pref[uk - 2] <= tmp)
				--uk;
			while (uk <= n - 2 && pref[n - 1] - pref[uk - 1] > tmp)
				++uk;

			if (pref[n - 1] - pref[uk - 1] <= tmp && pref[uk - 1] - pref[i - 1] <= tmp) {
				ans = max(ans, pref[n - 1] - pref[i - 1]);
			}
		}
	}

	uk = n - 1;

	for (int i = 0; i < n - 1; ++i) {
		int tmp = pref[n - 1] - (pref[i] + (pref[n - 1] - pref[uk - 1]));
		while (uk > i && tmp - a[uk - 1] >= pref[i] && tmp - a[uk - 1] >= pref[n - 1] - pref[uk - 2]) {
			tmp -= a[uk - 1];
			--uk;
		}
		while (uk <= n - 2 && (tmp < pref[i] || tmp < pref[n - 1] - pref[uk - 1])) {
			++uk;
			tmp += a[uk - 1];
		}
		if (tmp > pref[i] && tmp > pref[n - 1] - pref[uk - 1])
			ans = max(ans, pref[i] + pref[n - 1] - pref[uk - 1]);
	}
	
	cout << ld(ans) / ld(pref[n - 1]) << endl;
}