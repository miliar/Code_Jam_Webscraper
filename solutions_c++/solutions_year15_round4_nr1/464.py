#if 1
#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <list>
 
using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int, int> pii;
 
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const LL inf = 1e+9;
 
#define mp make_pair
#define pb push_back
#define X first
#define Y second
 
#define dbg(x) { cerr << #x << " = " << x << endl; }
 
// extended template
#pragma comment(linker, "/STACK:36777216")
typedef vector<int> vi;
typedef vector<vi> vvi;
 
#define forn(i, n) for (int i = 0; i < n; ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
 
template<typename T> istream & operator >> (istream &, vector<T> &);
template<typename T> ostream & operator << (ostream &, const vector<T> &);
 
#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;
 
#define NAME "basket"

int sm[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

string s = "v>^<";

int n, m;
vector <vector <int> > a;

bool che(int x, int y)
{
	return (x >= 0 && y >= 0 && x < n && y < m);
}

int check(int x, int y)
{
	int nap = a[x][y];

	bool fl = 0;
	for (int i = 1; i < 200; i++)
	{
		int nx = x + sm[nap][0] * i;
		int ny = y + sm[nap][1] * i;

		if (che(nx, ny))
		{
			if (a[nx][ny] != -1)
				return 0;
		}
		else
		{
			fl = 1;
			break;
		}
	}

	if (fl)
	{
		for (int np = 0; np < 4; np++)
		{
			for (int i = 1; i < 200; i++)
			{
				int nx = x + sm[np][0] * i;
				int ny = y + sm[np][1] * i;

				if (che(nx, ny))
				{
					if (a[nx][ny] != -1)
						return 1;
				}
				else
					break;
			}
		}
	}
	return -1;
}

void solve()
{
	int T;
	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		scanf("%d %d\n", &n, &m);
		a.clear();
		a.resize(n, vector <int> (m, -1));
		for (int i = 0; i < n; i++, scanf("\n"))
			for (int k = 0; k < m; k++)
			{
				char ch;
				scanf("%c", &ch);
				int pos = s.find(ch);
				if (pos != string::npos)
					a[i][k] = pos;
			}

		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			for (int k = 0; k < m; k++)
			{
				if (a[i][k] == -1)
					continue;
				int v = check(i, k);
				if (v == -1)
				{
					ans = -1;
					break;
				}
				else
					ans += v;
			}
			if (ans == -1)
				break;
		}
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", q + 1);
		else
			printf("Case #%d: %d\n", q + 1, ans);
	}
}

int main()
{

    //START
    //freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    solve();
    //END
    return 0;
}
/*******************************************
*******************************************/
 
template<typename T> istream & operator >> (istream &is, vector<T> &v)
{
    forn(i, v.size())
        is >> v[i];
    return is;
}
template<typename T> ostream & operator << (ostream &os, const vector<T> &v)
{
    forn(i, v.size())
        os << v[i] << " ";
    return os;
}
#endif