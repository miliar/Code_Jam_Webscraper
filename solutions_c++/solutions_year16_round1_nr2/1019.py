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

//#define SMALL
#define LARGE

vii v;

int grid[55][55];

int valid() {
	int cc = 0;
	rep(i,n)
		rep(j,n)
		{
			if (grid[i][j])
				cc++;
			if (i && grid[i][j] && grid[i - 1][j]
					&& grid[i][j] <= grid[i - 1][j])
				return 0;
			if (j && grid[i][j] && grid[i][j - 1]
					&& grid[i][j] <= grid[i][j - 1])
				return 0;
		}
	return cc;
}

vpii fill2(int from, int to, bool col) {
	vpii res;
	rep(i,n)
		if (col) {
			if (!grid[i][to])
				res.pb(mp(i, to));
			grid[i][to] = v[from][i];
		} else {
			if (!grid[to][i])
				res.pb(mp(to, i));
			grid[to][i] = v[from][i];
		}
	return res;
}

bool fit(int from, int to, bool col) {
	bool ok = 0;
	rep(i,n)
		if (col) {
			if (grid[i][to]) {
				ok = 1;
				if (grid[i][to] != v[from][i])
					return 0;
			}
		} else {
			if (grid[to][i]) {
				ok = 1;
				if (grid[to][i] != v[from][i])
					return 0;
			}
		}
	return ok;
}

void clear(vpii res) {
	rep(i,sz(res))
		grid[res[i].first][res[i].second] = 0;
}

bool colv[55], rowv[55];

vi ret;

void check() {
	int vv = valid();
	if (vv != n * n)
		return;
	multiset<vi> st;
	rep(i,n)
	{
		vi x;
		rep(j,n)
			x.pb(grid[i][j]);
		st.insert(x);
		x.clear();
		rep(j,n)
			x.pb(grid[j][i]);
		st.insert(x);
	}
	rep(i,2*n-1)
	{
		multiset<vi>::iterator it = st.find(v[i]);
		if (it == st.end())
			return;
		st.erase(it);
	}
	ret = *st.begin();
}

int to;
void dfs(int cur) {
	if (sz(ret))
		return;
	if (cur > to) {
		check();
		return;
	}
	rep(i,n)
	{
		if (!colv[i] && fit(cur, i, 1)) {
			colv[i] = 1;
			vpii res = fill2(cur, i, 1);
			dfs(cur + 1);
			colv[i] = 0;
			clear(res);
		}
		if (!rowv[i] && fit(cur, i, 0)) {
			rowv[i] = 1;
			vpii res = fill2(cur, i, 0);
			dfs(cur + 1);
			rowv[i] = 0;
			clear(res);
		}
	}
}

int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt22.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif
	cin >> N;
	rep2(nn,1,N+1)
	{
		cout << "Case #" << nn << ":";

		cin >> n;
		v.clear();
		rep(i,2*n-1)
		{
			vi x(n);
			rep(j,n)
				cin >> x[j];
			v.pb(x);
		}
		if(nn<29)
			continue;

		sort(all(v));
		int mx = 0;
		rep(i,2*n-1)
			mx = max(v[i][n - 1], mx);
		vi bb;
		rep(i,2*n-1)
			if (v[i][n - 1] == mx)
				bb.pb(i);
		if (sz(bb) == 2) {
			vi xx = v[bb[0]];
			vi yy = v[bb[1]];
			v.erase(v.begin() + bb[1]);
			v.erase(v.begin() + bb[0]);
			v.pb(xx);
			v.pb(yy);
		}

		mem(grid, 0);
		mem(colv, 0);
		mem(rowv, 0);
		ret.clear();
		int from = 0;
		to = 2 * n - 2;
		if (v[0][0] == v[1][0]) {
			from += 2;
			fill2(0, 0, 0);
			fill2(1, 0, 1);
			rowv[0] = 1;
			colv[0] = 1;
		} else {
			to -= 2;
			fill2(2 * n - 2, n - 1, 0);
			fill2(2 * n - 3, n - 1, 1);
			rowv[n - 1] = 1;
			colv[n - 1] = 1;
		}
		random_shuffle(v.begin()+from,v.begin()+to+1);

		dfs(from);

		rep(i,sz(ret))
			cout << " " << ret[i];
		cout << endl;

#ifdef SMALL
		if (!sz(ret)) {
			cerr << n << endl;
			rep(i,2*n-1)
			{
				rep(j,n)
				cerr << v[i][j] << " ";
				cerr << endl;
			}
		}
		cerr << nn << " of " << N << " is done." << " " << sz(ret) << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << " " << sz(ret) << endl;
#endif
	}
	return 0;
}
