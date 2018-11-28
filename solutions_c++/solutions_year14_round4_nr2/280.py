#if 1
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"
ostream & operator << (ostream &o, pii a) { return o << "(" << a.X << "," << a.Y << ")"; }
template<class T> string to_str(const T &a) { oss os; os << a; return os.str(); }
template<> string to_str<LD>(const LD& a) { oss os; os.precision(10); os.setf(ios::fixed); os << a; return os.str(); }
template<class T> T from_str(const string &s) { iss is; T val; is >> val; return val; }
string T(int test) { ostringstream os; os << "Case #" << test << ":"; return os.str(); }
int _test_start = -1, _test_end = -1;
bool need_to_run(int test) { return _test_start == -1 || _test_start <= test && test <= _test_end; }

vector<pii> b;
const int maxn = 1001;
int f[maxn][maxn];
int n;
vector<int> tol, tor;
struct fenwick_t
{
	vector<int> f;
	void init(int n)
	{
		f.assign(n, 0);
	}
	void add(int idx, int val)
	{
		for (int i = idx; i < f.size(); i |= i + 1)
			f[i] += val;
	}
	int sum(int right)
	{
		int res = 0;
		for (int i = right; i >= 0; i &= i + 1, --i)
			res += f[i];
		return res;			
	}
	int sum(int left, int right)
	{
		return sum(right) - sum(left - 1);
	}
		
};
int get_pos(int left, int right)
{
	int idx = left + right;
	return b[idx].Y - tol[idx] + left;
}

int go(int left, int right)
{
	int &res = f[left][right];
	if (res != -1)
		return res;
	if (left + right == n)
		return 0;

	int npos = get_pos(left, right);
	int r1 = go(left + 1, right) + abs(npos - left);
	int r2 = go(left, right + 1) + abs(npos - (n - right - 1));
	res = min(r1, r2);
	return res;		
}

void solve(int test)
{
	// read
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	
	if (!need_to_run(test)) return;
	// solve
	vector<int> all = a;
	sort(all.begin(), all.end());
	for (int i = 0; i < a.size(); ++i)
		a[i] = lower_bound(all.begin(), all.end(), a[i]) - all.begin();
	b.clear();
	b.resize(n);
	for (int i = 0; i < n; ++i)
		b[i] = mp(a[i], i);
	sort(b.begin(), b.end());
	tol.resize(n);
	tor.resize(n);
	fenwick_t fenwick;
	fenwick.init(n);
	for (int i = 0; i < n; ++i)
	{
		tol[i] = fenwick.sum(0, b[i].Y);
		tor[i] = fenwick.sum(b[i].Y, n - 1);
		fenwick.add(b[i].Y, 1);
	}
	// dbgv(a);
	// dbgv(b);
	// dbgv(tol);
	memset(f, -1, sizeof f);
	int res = go(0, 0);
	// write
	cout << T(test) << " " << res << endl;
}

int main(int argc, char *argv[])
{
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin); freopen(NAME ".out","w",stdout);
	if (argc == 2) { _test_start = _test_end = from_str<int>(argv[1]); }
	if (argc == 3) { _test_start = from_str<int>(argv[1]); _test_end = from_str<int>(argv[2]); }

	clock_t tstart = clock();
	
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; ++test)
	{
		clock_t tprev = clock();
		solve(test);
		if (need_to_run(test))
			dbg("elapsed for #" << test << ": " << (clock() - tprev) / LD(CLOCKS_PER_SEC));
	}

	dbg("elapsed: " << (clock() - tstart) / LD(CLOCKS_PER_SEC));
	return 0;
}
/*************************
*************************/
#endif

