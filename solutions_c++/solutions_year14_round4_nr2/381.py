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

int n;
vector <pair <int, int> > a;
int dp[1100][1100];
int pos[1100];

void solve() {
	cin >> n;
	a.resize(n);

	for (int i = 0; i < n; ++i) {
		cin >> a[i].second;
		a[i].first = i + 1;
	}
	for (int i = 0; i <= n; ++i)
		for (int j = 0; j <= n; ++j)
			dp[i][j] = -1;
	dp[0][0] = 0;
	
	
	vector <pair <int, int> > b;
	for (int i = 0; i < n; ++i) {
		b.push_back(mp(a[i].second, i));
	}
	
	sort(b.begin(), b.end());
	for (int i = 0; i < b.size(); ++i) {
		sort(a.begin(), a.end());
		for (int j = 0; j < a.size(); ++j) {
			if (b[i].first == a[j].second) {
				pos[i + 1] = j + 1;
				swap(a[a.size() - 1], a[j]);
				a.pop_back();
				break;
			}
		}
	}

	for (int i = 1; i <= n; ++i) {
		
		int l;
		int r = i - 1;
		int newv;
		for (l = 0; l <= r; ++l) {
			if (dp[l][r] == -1)
				continue;
			newv = dp[l][r] + pos[i] - 1;
			if (dp[i][r] == -1 || dp[i][r] > newv)
				dp[i][r] = newv;
			newv = dp[l][r] + (n - i + 1 - pos[i]);
			if (dp[l][i] == -1 || dp[l][i] > newv)
				dp[l][i] = newv;
		}
		l = i - 1;
		for (r = 0; r <= l; ++r) {
			if (dp[l][r] == -1)
				continue;
			newv = dp[l][r] + pos[i] - 1;
			if (dp[i][r] == -1 || dp[i][r] > newv)
				dp[i][r] = newv;
			newv = dp[l][r] + (n - i + 1 - pos[i]);
			if (dp[l][i] == -1 || dp[l][i] > newv)
				dp[l][i] = newv;
		}
	}
	
	if (n == 1) {
		cout << 0 << endl;
		return;
	}
	int ans = -1;
	for (int i = 1; i < n; ++i) {
		if (ans == -1 || ans > dp[i][n])
			ans = dp[i][n];
		if (ans == -1 || ans > dp[n][i])
			ans = dp[n][i];
	}
	cout << ans << endl;
}