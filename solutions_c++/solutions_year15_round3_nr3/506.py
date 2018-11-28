#pragma comment (linker, "/STACK:128000000")
#include <iostream> 
#include <cstdio> 
#include <fstream>
#include <functional>
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

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
    string s = FILENAME;
#ifdef YA
    //assert(!s.empty());
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //cerr<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock();
#else
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout); 
    cin.tie(0);
#endif
    cout.sync_with_stdio(0);
    cout.precision(10);
    cout << fixed;
    int t = 1;
    
	cin >> t;
    for (int i = 1; i <= t; ++i) {
        //++timer;
		cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}

void solve() {
	int c, d, v;
	cin >> c >> d >> v;
	vector <int> a(d);
	for (int i = 0; i < d; ++i) {
		cin >> a[i];
	}

	vector <int> used(v + 1);

	for (int mask = 0; mask < (1 << d); ++mask) {
		int sum = 0;
		for (int j = 0; j < d; ++j) {
			if (mask & (1 << j)) {
				sum += a[j];	
			}
		}
		if (sum <= v)
			used[sum] = 1;
	}

	int ans = 0;

	while (true) {
		
		int sum = 0;

		for (int i = 1; i <= v; ++i) {
			sum += used[i];	
		}

		if (sum == v) {
			break;
		}
		++ans;

		int x;
		for (int i = 1; i <= v; ++i) {
			if (!used[i]) {
				x = i;
				break;
			}
		}

		for (int j = v; j >= 0; --j) {
			if (j + x <= v && used[j]) {
				used[j + x] = 1;
			}
		}
	}

	cout << ans << endl;
}