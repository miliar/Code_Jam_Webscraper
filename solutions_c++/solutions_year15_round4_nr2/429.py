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

void solve()
{
	int T;
	cin >> T;
	cout.setf(ios::fixed);
	cout.precision(9);
	for (int q = 0; q < T; q++)
	{
		int n;
		LD v1, x1;
		cin >> n >> v1 >> x1;
		LL v = LL(v1 * 10000 + eps);
		LL x = LL(x1 * 10000 + eps);

		vector <LL> ri(n), xi(n);
			for (int i = 0; i < n; i++)
			{
				LD r, x;
				cin >> r >> x;
				ri[i] = LL(r * 10000 + eps);
				xi[i] = (LL)(x * 10000 + eps);
			}

		if (n == 2)
		{
			LD ans = 0;
			if (xi[0] != xi[1] )
			{
				LL t1 = x - xi[0];
				LL t2 = xi[1] - xi[0];
				LD V1 = LD(x - xi[0]) * v / (xi[1] - xi[0]);
				LD V0 = v - V1;

				if (t1 * t2 < 0 || V0 < 0)
					ans = -1;
				else
					ans = max(V1 / ri[1], V0 / ri[0]);
			}
			else
			{
				if (xi[0] != x)
					ans = -1;
				else
					ans = LD(v) / (ri[1] + ri[0]);
			}

			if (ans < 0)
				cout << "Case #" << q + 1 << ": " << "IMPOSSIBLE" << endl;
			else
				cout << "Case #" << q + 1 << ": " << ans << endl;
		}
		else
		{
			LD ans = 0;
			if (xi[0] != x)
				ans = -1;
			else
				ans = LD(v) / (ri[0]);

			if (ans < 0)
				cout << "Case #" << q + 1 << ": " << "IMPOSSIBLE" << endl;
			else
				cout << "Case #" << q + 1 << ": " << ans << endl;
		}
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