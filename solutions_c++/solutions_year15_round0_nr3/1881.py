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
		cerr << "!!!" << i << "!!" << endl;

		cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}

void solve() {
	int l, x;
	cin >> l >> x;
	string s;
	cin >> s;
	
	string t;
	for (int i = 0; i < x; ++i) {
		t += s;
	}

	int go[4][4] = {{0,0,0,0},{0,1,0,1}, {0,1,1,0}, {0,0,1,1}};

	vector <int> a(t.size());
	for (int i = 0; i < a.size(); ++i) {
		if (t[i] == 'i') {
			a[i] = 1;
		}
		if (t[i] == 'j') {
			a[i] = 2;
		}
		if (t[i] == 'k') {
			a[i] = 3;
		}
	}

	vector <int> sumL(a.size() + 1);
	vector <int> sumR(a.size() + 1);

	for (int i = 0; i < a.size(); ++i) {
		sumL[i + 1] = sumL[i] ^ a[i];
	}
	for (int i = a.size() - 1; i >= 0; --i) {
		sumR[i] = sumR[i + 1] ^ a[i];
	}

	vector < vector <int> > bal(a.size() + 1, vector <int> (a.size() + 1));
	
	for (int st = 0; st < a.size(); ++st) {
		int cur = 0;
		for (int j = st; j < a.size(); ++j) {
			bal[st][j + 1] = bal[st][j] + go[cur][a[j]];
			cur ^= a[j];
		}
	}

	if (sumL[a.size()] != (1 ^ 2 ^ 3)) {
		cout << "NO\n";
		return;
	}

	for (int left = 0; left < a.size(); ++left) {
		for (int right = left + 1; right <= a.size(); ++right) {
			
			if (sumL[left] != 1 || (sumL[right] ^ sumL[left]) != 2 || (bal[0][left] % 2) || (bal[left][right] % 2) || (bal[right][a.size()] % 2)) {
				continue;
			}
			cout << "YES\n";
			return;
		}
	}
	cout << "NO\n";
}