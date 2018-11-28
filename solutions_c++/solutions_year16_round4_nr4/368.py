/*

 Email : ahmed.aly.tc@gmail.com

 ahmed_aly on HackerRank, Codeforces and TopCoder

 Google Code Jam tools website: http://a2oj.com/CodeJamTools/

 */

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int N, I, J, n, m;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

#define SMALL
//#define LARGE

string s[55];

vi ord;

bool vis[55];
bool ok(int ind) {
	if (ind == n)
		return 1;
	int a = ord[ind];
	bool found = 0;
	rep(b,n)
		if (!vis[b] && s[a][b] == '1') {
			found = 1;
			vis[b] = 1;
			bool x = ok(ind + 1);
			vis[b] = 0;
			if (!x)
				return 0;
		}
	return found;
}

bool ok() {
	ord.clear();
	rep(i,n)
		ord.pb(i);
	do {
		mem(vis, 0);
		if (!ok(0))
			return 0;
	} while (next_permutation(all(ord)));
	return 1;
}

int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("D-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("D-large.in", "rt", stdin);
	freopen("D-large.out", "wt", stdout);
#endif
	cin >> N;
	rep2(nn,1,N+1)
	{
		cin >> n;
		rep(i,n)
			cin >> s[i];
		int best = oo;
		vpii v;
		rep(mask,1<<(n*n))
		{
			bool bad = 0;
			rep(i,n*n)
				if (mask & (1 << i)) {
					int a = i / n;
					int b = i % n;
					if (s[a][b] == '1')
						bad = 1;
				}
			if (bad)
				continue;
			v.pb(mp(__builtin_popcount(mask), mask));
		}
		sort(all(v));
		rep(ii,sz(v))
		{
			int mask = v[ii].second;
			rep(i,n*n)
				if (mask & (1 << i)) {
					int a = i / n;
					int b = i % n;
					s[a][b] = '1';
				}
			if (ok()) {
				best = v[ii].first;
				break;
			}
			rep(i,n*n)
				if (mask & (1 << i)) {
					int a = i / n;
					int b = i % n;
					s[a][b] = '0';
				}
		}

		cout << "Case #" << nn << ": " << best << endl;

#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
