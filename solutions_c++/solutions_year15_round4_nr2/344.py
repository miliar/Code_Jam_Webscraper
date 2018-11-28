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

const ld eps = 1e-07;

void solve() {
	ld V, X;
	int n;
	cin >> n >> V >> X;
	vector <ld> r(n);
	vector <ld> c(n);
	for (int i = 0; i < n; ++i) {
		cin >> r[i] >> c[i];
	}
	
	if (n == 1) {
		if (abs(c[0] - X) > eps) {
			cout << "IMPOSSIBLE\n";
		}
		else {
			cout << V / r[0] << "\n";
		}
		return;
	}

	
	ld vv[2];
	
	if (abs(c[0] - X) > eps && abs(c[1] - X) > eps) {
		if (abs(c[0] - c[1]) < eps) {
			cout << "IMPOSSIBLE\n";
			return;
		}
		vv[1] = (X - c[0]) * V / (c[1] - c[0]);
		vv[0] = V - vv[1];
		if (vv[1] < -eps || vv[0] < -eps) {
			cout << "IMPOSSIBLE\n";
			return;
		}
		cout << max(vv[0] / r[0], vv[1] / r[1]) << "\n";
	}
	else {
		if (abs(c[0] - X) < eps && abs(c[1] - X) < eps) {
			cout << V / (r[0] + r[1]) << "\n";
		}
		else {
			ld rr;
			if (abs(c[0] - X) < eps) {
				rr = r[0];
			}
			else {
				rr = r[1];
			}
			cout << V / rr << "\n";
		}
	}
}