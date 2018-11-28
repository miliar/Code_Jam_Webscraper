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
 
const int N = 1e5 + 555;

int a[N];
int n;
 
inline bool read()
{
	if(!(cin >> n))
		return false;

	forn1(i, n)
	{
		assert(cin >> a[i]);
	}

    return true;
}

inline void gen()
{
	return;
}

inline void solve()
{
	int ans1 = 0;
	for(int i = 1; i < n; i++)
	{
		if(a[i] > a[i + 1])
		{
			ans1 += a[i] - a[i + 1];
		}
	}

	int ans2 = INF;

	for(int v = 0; v <= 20001; v++)
	{
		bool ok = true;
		int cur = 0;
		int cnt = a[1];

		forn1(i, n - 1)
		{
			int can = min(v, a[i]);
			cnt -= can;
			cur += can;
			if(i == n)
				break;
			if(a[i + 1] < cnt)
			{
				ok = false;
				break;
			}
			else
			{
				cnt = a[i + 1];
			}
		}

		if(ok)
			ans2 = min(ans2, cur);

		/*
		for(int i = 1; i < n; i++)
		{
			if(a[i] > a[i + 1])
			{
				int dif = a[i] - a[i + 1];
				if(dif > v)
				{
					ok = false;
					break;
				}

				cur += dif;
			}

			if(a[i] < a[i + 1])
			{
				if(a[i] <= v)
					cur += a[i];
				else
					cur += v;
				//cur += min(v, a[i]);
				continue;
			}

			if(a[i] == a[i + 1])
			{
				if(a[i] <= v)
					cur += a[i];
				else
					cur += v;
				continue;
			}
		}

		if(ok)
			ans2 = min(ans2, cur);
		if(v < 100 && ok)
			cerr << "v cur == " << v << ' ' << cur << endl;*/
	}

	assert(ans1 < INF && ans2 < INF);
	cout << ans1 << ' ' << ans2 << endl;
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