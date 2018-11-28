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

vi s;

inline ll convert(int fromBase) {
	ll temp = 0;
	ll p = 1;
	for (int i = N - 1; i >= 0; i--) {
		temp += p * s[i];
		p *= fromBase;
	}
	return temp;
}

vii v;
vii p;

void dfs(int cur) {
	if (sz(v) == J)
		return;
	if (cur == N - 1) {
		vi temp;
		rep2(i,2,11)
		{
			ll x = convert(i);
			if (x % 2 == 0) {
				temp.pb(2);
				continue;
			}
			bool found = 0;
			for (ll d = 3; d * d <= x; d += 2)
				if (x % d == 0) {
					temp.pb(d);
					found = 1;
					break;
				}
			if (!found)
				break;
		}
		if (sz(temp) == 9) {
			v.pb(s);
			p.pb(temp);
		}
		return;
	}
	dfs(cur + 1);
	s[cur] = 1;
	dfs(cur + 1);
	s[cur] = 0;
}

#define SMALL
//#define LARGE

int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
#endif
	cin >> N;
	rep2(nn,1,2)
	{
		cout << "Case #" << nn << ":" << endl;
		cin >> N >> J;
		s = vi(N, 0);
		s[0] = s[N - 1] = 1;
		dfs(1);
		rep(i,J)
		{
			rep(j,N)
				cout << v[i][j];
			rep(j,9)
				cout << " " << p[i][j];
			cout << endl;
		}
#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
