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
	//freopen("input.txt", "r", stdin); 
	//freopen("output.txt", "w", stdout); 
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

int n, x;
vector <int> a;
vector <int> rest;

void solve() {
	cin >> n >> x;
	a.resize(n);
	rest.clear();
	for (int i = 0; i < n; ++i) 
		cin >> a[i];
	sort(a.begin(), a.end());
	int ans = 0;
	while (a.size() && a.back() > x / 2) {
		rest.push_back(x - a.back());
		a.pop_back();
		++ans;
	}
	sort(rest.begin(), rest.end());
	while (a.size()) {
		int y = a.back();
		a.pop_back();
		if (rest.size() && rest.back() >= y) {
			rest.pop_back();
		}
		else {
			++ans;
			rest.push_back(x - y);
		}
	}
	cout << ans << endl;
}