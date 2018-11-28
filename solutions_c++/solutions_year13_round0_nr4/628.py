#include <iostream>
#include <algorithm>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <iomanip>
#include <cmath>
using namespace std;

#define forl(i, s, t) for(__typeof(s) i = s; i < t; i++)
#define rforl(i, s, t) for(__typeof(s) i = s; i > t; i--)
#define foreach(itr, c) forl(itr, (c).begin(), (c).end())
#define rforeach(itr, c) forl(itr, (c).rbegin(), (c).rend())

#define rep(n) forl(rep_c, 0, n)
#define fill2d_nn(g, s, z, v) forl(i, 0, s) fill_n(g[i], z, v)
#define fill2d_n(g, s, v) fill2d_nn(g, s, s, v)
//#define read(s, t) forloop(read_c, s, t) cin >> *read_c
//inline void read(ForwardIterator s, ForwardIterator e) { forloop(i, s, e) cin >> *i; }
//#define read_n(x, n) forl(read_n_c, 0, n) cin >> x[read_n_c]
//#define rread_n(x, n) rforl(rread_n_c, n-1, -1) cin >> x[rread_n_c]

#define tpop(x) (x).top(); (x).pop()
#define fpop(x) (x).front(); (x).pop()
//#define all(x) (x).begin(), (x).end()
#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)

//#define chmin(a, b) a = min(a, b)
//#define chmax(a, b) a = max(a, b)
template<typename T> inline void chmin(T& a, const T& b) { a = min(a, b); }
template<typename T> inline void chmax(T& a, const T& b) { a = max(a, b); }

int gcd(int a, int b) { if(b == 0) return a; return gcd(b, a % b); }
#define gcd_n(a, n) accumulate(a+1, a+n, a[0], gcd);
template <class ForwardIterator>
inline int gcd_r(ForwardIterator s, ForwardIterator e) { return accumulate(s+1, e, s[0], gcd); }

#ifdef DEBUG
#define varcontent(v) #v << '=' << v
#define debug(v) cerr << varcontent(v) << endl
#define pdebug(v, w) cerr << '(' << varcontent(v) << ',' << varcontent(w) << ')' << endl
#define dmsg(a) cerr << a << endl
#else
#define varcontent(v) 0
#define debug(v) 0
#define pdebug(v, w) 0
#define dmsg(a) 0
#endif

#define printarr(a, n) cerr << #a << " = ["; forloop(i, 0, n) cerr << a[i] << ' '; cerr.seekp(cerr.tellp()-1L); cerr << ']' << endl
#define printgrid(g, y, x) cerr << endl << #g << ':' << endl; forl(i, 0, y) { forl(j, 0, x) cerr << g[i][j] << ' '; cerr << endl; } cerr << endl
#define rprintgrid(g, x, y) cerr << endl << #g << ':' << endl; forl(i, 0, x) { forl(j, 0, y) cerr << g[j][i] << ' '; cerr << endl; } cerr << endl
/*inline void printgrid(RandomAccessIterator g, int y, int x) {
	cerr << endl << #g << ':' << endl;
	forloop(i, 0, y) {
		forloop(j, 0, x) cout<< g[i][j] << ' ';
		cout << endl;
	}
	cerr << endl;
}*/
/*inline void rprintgrid(RandomAccessIterator g, int x, int y) {
	cerr << endl << #g << ':' << endl;
	forloop(i, 0, x) {
		forloop(j, 0, y) cout<< g[j][i] << ' ';
		cout << endl;
	}
	cerr << endl;
}*/

const int INF = numeric_limits<int>::max()/2;
const double EPS = INF*numeric_limits<double>::epsilon();

set<int> cache;
bool open_chest(map<int,int>& keys, vector< pair< int,vector<int> > >& chest, vector<bool>& opened, vector<int>& order) {
	int N = chest.size();
	int id = 0;
	forl(n, 0, N) {
		if(opened[n]) id |= (1 << n);
	}
	if(cache.find(id) != cache.end()) return false;
	cache.insert(id);
	if(order.size() == N) {
		forl(n, 0, N) {
			cout << ' ' << order[n];
		}
		cout << endl;
		return true;
	}
	forl(n, 0, N) {
		if(!opened[n] && keys[chest[n].first] > 0) { //open_chest(keys, chest, unopened)
			keys[chest[n].first]--;
			foreach(i, chest[n].second) {
				keys[*i]++;
			}
			opened[n] = true;
			order.push_back(n+1);
			if(open_chest(keys, chest, opened, order)) return true;
			order.pop_back();
			opened[n] = false;
			foreach(i, chest[n].second) {
				keys[*i]--;
			}
			keys[chest[n].first]++;
		}
	}
	return false;
}

void gcjmain() {
	int K, N;
	cin >> K >> N;
	map<int,int> keys;
	forl(k, 0, K) {
		int i;
		cin >> i;
		keys[i]++;
	}
	vector< pair< int,vector<int> > > chest(N);
	vector<bool> opened(N);
	forl(n, 0, N) {
		//unopened.insert(n);
		int t, k;
		cin >> t >> k;
		chest[n].first = t;
		chest[n].second.reserve(k);
		forl(i, 0, k) {
			int j;
			cin >> j;
			chest[n].second.push_back(j);
		}
	}
	vector<int> order;
	order.reserve(N);
	cache.clear();
	if(!open_chest(keys, chest, opened, order)) {
		cout << " IMPOSSIBLE" << endl;
	}
}

int main() {
	int T;
	cin >> T;
	forl(t, 1, T+1) {
		cerr << "Case: " << t << '/' << T << endl;
		cout << "Case #" << t << ":";
		gcjmain();
	}
}
