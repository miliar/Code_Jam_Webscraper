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
 
const int N = 12;

int n;
int a[N];
 
inline bool read()
{
	if(!(cin >> n))
		return false;

	forn(i, n)
	{
		assert(cin >> a[i]);
	}

    return true;
}

inline void gen()
{
	return;
}

int cnt[N];

int ans;

void rec(vector<int> have, int curans)
{
	if(curans > 9)
	{
		return;
	}

	if(curans >= ans)
	{
		return;
	}

	int mx = 0;
	forn(i, sz(have))
	{
		if(have[i] > 0)
		{
			mx = max(mx, i);
			//assert(have[i] == 1);
		}
	}

	assert(mx > 0);
	if(mx == 1)
	{
		ans = min(ans, curans);
		return;
	}

	vector<int> nhave(sz(have));

	forn(i, 10)
	{
		if(have[i] > 0 && i > 1)
		{
			nhave[i - 1] = have[i];
		}
	}

	rec(nhave, curans + 1);

	for(int nmax = 1; nmax <= 9; nmax++)
	{
		vector<int> v(sz(have));
		forn(i, sz(v))
			v[i] = have[i];
		bool was = false;
		int sum = 0;

		forn(i, 10)
		{
			if(have[i] == 0)
				continue;
			if(i <= nmax)
				continue;
			int other = i - nmax;
			if(other > nmax)
				continue;
			was = true;
			v[nmax] += have[i];
			v[other] += have[i];
			sum += have[i];
			v[i] = 0;
		}

		if(was)
		{
			rec(v, curans + sum);
		}
	}
}

inline void solve()
{
	vector<int> init(10);

	forn(i, n)
	{
		cnt[a[i]]++;
	}

	forn(i, 10)
	{
		if(cnt[i] > 0)
		{
			init[i] = cnt[i];
		}
		else
		{
			init[i] = 0;
		}
	}

	ans = 10;

	rec(init, 1);

	cout << ans << endl;
    return;
}

inline void clear()
{
	forn(i, N)
	{
		cnt[i] = 0;
	}

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