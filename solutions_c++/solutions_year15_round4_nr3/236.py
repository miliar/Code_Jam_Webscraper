#include "bits/stdc++.h"
 
using namespace std;
 
#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define mp make_pair
#define pb push_back
#define PATH "C:\\Users\\ValenKof\\Desktop\\"
 
template<typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template<typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template<typename T> inline int sz(const T& x) { return x.size(); }
 
typedef unsigned char uchar;
 
// SOLUTIONS BEGINS HERE

typedef long long ll;

map<string, int> cached;

int cache(const string& s)
{
	auto it = cached.find(s);
	if (it == cached.end()) {
		int index = cached.size();
		cached[s] = index;
		return index;
	}
	return it->second;
}

typedef bitset<(1 << 12)> SET;

inline void update(const SET& ee, const SET& ff, SET& e, SET& f, int x, int& curr)
{
	if (ee[x] || e[x]) {
		return;
	}
	e[x] = true;
	if (ff[x] || f[x]) {
		curr++;
	}
}


void solve() {
	int n;
	cin >> n;

	string line;
	getline(cin, line);

	cached.clear();
	
	
	vector<vector<int>> lines(n);
	forn (i, n) {
		getline(cin, line);
		stringstream ss(line);
		string str;
		while (ss >> str) {
			lines[i].pb(cache(str));
		}
		sort(all(lines[i]));
		lines[i].erase(unique(all(lines[i])), lines[i].end());
	}
	
	int ans = numeric_limits<int>::max();
	SET ee;
	SET ff;
	
	int base = 0;
	for (int x : lines[0]) {
		update(ee, ff, ee, ff, x, base);
	}
	for (int x : lines[1]) {
		update(ff, ee, ff, ee, x, base);
	}

	
	// debug(base);
	for (int mask = 0; mask < (1 << n); mask += 4) {
		SET e;
		SET f;
		int curr = 0;
		for (int i = 2; i < n; ++i) {
			for (int x : lines[i]) {
				if ((mask >> i) & 1) {
					update(ee, ff, e, f, x, curr);
				} else {
					update(ff, ee, f, e, x, curr);
				}
			}
		}
		mn(ans, base + curr);
	}
	cout << ans;
	
}
 
int main() {
	// freopen(PATH"in.txt", "r", stdin);
	freopen(PATH"C-small-attempt1.in", "r", stdin);
	freopen(PATH"out.txt", "w", stdout);
	int nTests;
	cin >> nTests;
	forn (i, nTests) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
		cout << endl;
	}	
	return 0;
}