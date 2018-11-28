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
		cerr << i << endl;
		cout << "Case #" << i << ": ";
		solve();
	}
#ifdef YA 
	//cout << "\n\n\nTime:" << ((clock() - start) / 1.0 / CLOCKS_PER_SEC);
#endif 
	return 0;
}

void solve() {            
	int n, p, q;
	cin >> p >> q >> n;
	vector <int> h, g;
	h.resize(n);
	g.resize(n);
	for (int i = 0; i < n; ++i) {
		cin >> h[i] >> g[i];
	}
	vector < vector <int> > dp;
	dp.assign(n + 1, vector <int> (n * 10 + 10, -1));
	dp[0][1] = 0;
	
	int ans = -1;

	for (int i = 0; i <= n; ++i) {
		for (int j = 0; j <= n * 10 + 3; ++j) {
			if (dp[i][j] == -1)
				continue;
			if (ans == -1 || dp[i][j] > ans)
				ans = dp[i][j];
			if (i == n)
				continue;
			
			//do noth
			int tmp = (h[i] + q - 1) / q;
			int tmp2 = dp[i][j];
			if (dp[i + 1][j + tmp] == -1 || dp[i + 1][j + tmp] < tmp2)
				dp[i + 1][j + tmp] = tmp2;

			for (int z = 0; z < tmp; ++z) {
				if (z == 0) {
					if ((h[i] + p - 1)/ p <= j) {
						int tmp = -((h[i] + p - 1) / p);
						int tmp2 = dp[i][j] + g[i];
						if (dp[i + 1][j + tmp] == -1 || dp[i + 1][j + tmp] < tmp2)
							dp[i + 1][j + tmp] = tmp2;
					}
				}
				else {
					if ((h[i] - z * q + p - 1)/ p <= j + z) {
						int tmp = z - ((h[i] - z * q + p - 1)/ p);
						int tmp2 = dp[i][j] + g[i];
						if (dp[i + 1][j + tmp] == -1 || dp[i + 1][j + tmp] < tmp2)
							dp[i + 1][j + tmp] = tmp2;
					}
				}
			}
		}
	}
	cout << ans << "\n";
}