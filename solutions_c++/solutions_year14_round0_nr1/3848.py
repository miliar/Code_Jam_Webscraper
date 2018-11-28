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

int ans[2];
int a[2][4][4];

void solve() {
	for (int i = 0; i < 2; ++i) {
		cin >> ans[i];
		--ans[i];
		for (int x = 0; x < 4; ++x)
			for (int y = 0; y < 4; ++y) {
				cin >> a[i][x][y];
			}
	}
	int count = 0;
	int res;

	for (int i = 1; i <= 16; ++i) {
		bool f = true;
		for (int j = 0; j < 2; ++j) {
			for (int x = 0; x < 4; ++x)
				for (int y = 0; y < 4; ++y) 
					if (a[j][x][y] == i) {
						if (x != ans[j])
							f = false;
					}
		}
		if (f) {
			++count;
			res = i;
		}
	}
	if (count == 1) {
		cout << res << "\n";
	}
	else if (count == 0) {
		cout << "Volunteer cheated!\n";
	}
	else {
		cout << "Bad magician!\n";
	}
}