#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
 
using namespace std;
 
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define forn1(i, n) for(int i = 1; i <= (int)(n); i++)
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)((a).size())
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define x first
#define y second
#define y1 __y1
#define sqr(x) ((x) * (x))
 
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
 
const int INF = (int)(1e9);
const li INF64 = (li)(INF) * (li)(INF);
const ld eps = 1e-9;
const ld pi = ld(3.1415926535897932384626433832795);
 
bool in(int i, int j, int n, int m)
{
    return i >= 0 && i < n && j >= 0 && j < m;
}
 
inline int myrand()
{
    return (rand() ^ (rand() << 15));
}
 
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
 
const int N = 20;

int n;
pt a[N];
 
inline bool read()
{
	if(!(cin >> n))
		return false;

	forn(i, n)
	{
		assert(cin >> a[i].X >> a[i].Y);
	}

    return true;
}

inline void gen()
{
	return;
}

map<pt, int> ans;

ld dist(ld x1, ld y1, ld x2, ld y2)
{
	return sqrt(sqr(x1 - x2) + sqr(y1 - y2));
}

pt start;

bool cmp(pt a, pt b)
{
	double ra = atan2(a.y - start.y + 0.0, a.x - start.x + 0.0);
	double rb = atan2(b.y - start.y + 0.0, b.x - start.x + 0.0);
	if(abs(ra - rb) > eps)
		return ra < rb;
	return dist(a.x, a.y, start.x, start.y) < dist(b.x, b.y, start.x, start.y);
}

li cross_p(int a1, int b1, int a2, int b2)
{
	return a1 * 1LL * b2 - a2 * 1LL * b1;
}

vector<pt> convex_hull(vector<pt> c)
{
	bool ok = true;
	pt aa = c[0], bb = c[1];
	li A = bb.y - aa.y;
	li B = aa.x - bb.x;
	li C = -A * aa.x - B * aa.y;
	for(int i = 2; i < sz(c); i++)
	{
		li dist = A * c[i].x + B * c[i].y + C;
		if(dist != 0)
			ok = false;
	}

	if(ok)
		return c;
	static pt b[N];
	int nn = sz(c);
	forn(i, nn)
		b[i] = c[i];
		//cerr << "WTF" << endl;
	//cerr << "n == " << n << endl;
	int ind = 0;
	int miny = 1e9;
	int minx = 1e9;
	for(int i = 0; i < nn; i++)
	{
		//scanf("%d%d", &a[i].x, &a[i].y);
		if(b[i].y < miny)
		{
			miny = b[i].y;
			minx = b[i].x;
			ind = i;
		}
		else
			if(b[i].y == miny && b[i].x < minx)
			{
				ind = i;
				minx = b[i].x;
			}
	}
	//cerr << "n == " << n << endl;
	pt temp;
	temp = b[0];
	b[0] = b[ind];
	b[ind] = temp;
	start = b[0];
	sort(b + 1, b + nn, cmp);

	int j = nn - 1;
	int kol = 0;
	pt cur[N];
	//cerr << "n == " << n << endl;
	while(cross_p(b[j].x - b[0].x, b[j].y - b[0].y, b[j - 1].x - b[0].x, b[j - 1].y - b[0].y) == 0)
	{
		kol++;
		cur[kol] = b[j];
		j--;
	}
	kol++;
	cur[kol] = b[j];
	kol = 0;
	//cerr << "n == " << n << endl;
	for(int i = j; i < nn; i++)
	{
		kol++;
		b[i] = cur[kol];
		//cerr << "WTF n == " << n << endl;
	}

	//cerr << "n == " << n << endl;

	vector<pt> ans;
	//cerr << "!" << endl;
	//cerr << "nn == " << nn << endl;
	ans.push_back(b[0]);
	ans.push_back(b[1]);
	//cerr << "itch" << endl;
	for(int i = 2; i < nn; i++)
	{
		//cerr << "OMG" << endl;
		while(ans.size() >= 2)
		{
			int j = ans.size() - 1;
			if(cross_p(ans[j].x - ans[j - 1].x, ans[j].y - ans[j - 1].y, b[i].x - ans[j - 1].x, b[i].y - ans[j - 1].y) < 0)
				ans.pop_back();
			else
				break;
		}
		ans.push_back(b[i]);
	}

	//cerr << "WTF" << endl;
	//cerr << "n == " << n << endl;
	//cerr << "succ" << endl;
	return ans;
}

inline void solve()
{
	ans.clear();
	forn(i, n)
		ans[a[i]] = INF;
	//cerr << "init n == " << n << endl;

	forn(mask, (1 << n))
	{
		int cntbit = 0;
		forn(i, n)
		{
			if(mask & (1 << i))
				cntbit++;
		}

		if(cntbit == 0)
			continue;
		if(cntbit == 1)
		{
			forn(i, n)
				ans[a[i]] = min(ans[a[i]], n - 1);
			continue;
		}

		vector<pt> cc;
		//nn = 0;
		forn(i, n)
		{
			if(mask & (1 << i))
			{
				cc.pb(a[i]);
			}
		}

		//cerr << "bef CH == " << n << endl;
		vector<pt> c = convex_hull(cc);
		forn(i, sz(c))
		{
			ans[c[i]] = min(ans[c[i]], n - cntbit);
		}

		//cerr << "after CH == " << n << endl;
	}

	//cerr << "n == " << n << endl;
	cout << endl;
	forn(i, n)
		cout << ans[a[i]] << endl;
	//cout << endl;
	return;
}

inline void clear()
{
	return;
}
 
int main(){
#ifdef _DEBUG
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
 
    cout << setprecision(10) << fixed;
    cerr << setprecision(10) << fixed;
 
    srand(int(time(NULL)));

	int T;
	assert(cin >> T);
 
	forn(test, T)
	{
		cerr << "RUNNING on test == " << test + 1 << endl;
		int startT = clock();
		assert(read());
		//gen();
		cout << "Case #" << test + 1 << ": ";
		solve();
		clear();
		int endT = clock();
		int Time = endT - startT;
		cerr << "Test " << test + 1 << " passed with TIME == " << Time << " ms" << endl;
		cerr << "Summary TIME == " << clock() << endl << endl << endl;
	}
 
    cerr << "TIME == " << clock() << " ms" << endl;
    return 0;
}