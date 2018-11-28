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
	int k, l, s;
	cin >> k >> l >> s;
	
	vector <ld> prob(26);

	for (int i = 0; i < k; ++i) {
		char c;
		cin >> c;
		prob[c - 'A'] += 1.0 / k;
	}

	vector <int> a(l);
	for (int i = 0; i < l; ++i) {
		char c;
		cin >> c;
		a[i] = c - 'A';
	}

	vector <vector <int> > gopref(l + 1, vector <int> (26));

	for (int len = 0; len <= l; ++len) {
		for (int c = 0; c < 26; ++c) {
			vector <int> newstr;
			for (int i = 0; i < len; ++i) {
				newstr.push_back(a[i]);
			}
			newstr.push_back(c);
			gopref[len][c] = 0;

			for (int pref = min(l, (int)newstr.size()); pref >= 1; --pref) {
				bool f = true;
				for (int j = 0; j < pref; ++j) {
					if (a[j] != newstr[newstr.size() - pref + j]) {
						f = false;
						break;
					}
				}
				if (f) {
					gopref[len][c] = pref;
					break;
				}
			}
		}
	}

	vector <vector <vector <ld> > > dp(s + 1, vector <vector <ld> > (l + 1, vector <ld> (s + 2)));

	dp[0][0][0] = 1.0;

	ld eps = 0;

	for (int i = 0; i < s; ++i) {
		for (int pref = 0; pref <= l; ++pref) {
			for (int ans = 0; ans <= s; ++ans) {
				if (dp[i][pref][ans] < eps) {
					continue;
				}
				for (int c = 0; c < 26; ++c) {
					if (prob[c] < eps) {
						continue;
					}

					int npref = gopref[pref][c];

					if (npref == l) {
						dp[i + 1][npref][ans + 1] += dp[i][pref][ans] * prob[c];
					}
					else {
						dp[i + 1][npref][ans] += dp[i][pref][ans] * prob[c];
					}
				}
			}
		}
	}


	int maxans = 0;
	for (int pref = 0; pref <= l; ++pref) {
		for (int ans = maxans + 1; ans <= s; ++ans) {
			if (dp[s][pref][ans] > eps) {
				maxans = ans;
			}
		}
	}

	ld res = 0;

	for (int pref = 0; pref <= l; ++pref) {
		for (int ans = 0; ans <= s; ++ans) {
			res += ld(maxans - ans) * dp[s][pref][ans];
		}
	}
	cout << res << "\n";
}