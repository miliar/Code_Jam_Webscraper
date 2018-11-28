#pragma comment(linker, "/STACK:128777216")
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <math.h>
#include <queue>
#include <stack>
#include <cassert>
#include <time.h>

#define forn(i,n) for (int i = 0; i < (int)n; i++)
#define fornd(i, n) for (int i = (int)n - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define forba(i,b,a) for (int i = (int)b; i >= (int)a; i--)
#define zero(a) memset (a, 0, sizeof (a))
#define _(a, val) memset (a, val, sizeof (a))
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
typedef long long ll;
typedef unsigned long long ull;

const ll LINF= 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

using namespace std;

void prepare (string s)
{
#ifdef _DEBUG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#else
	if (s.length() != 0)
	{
		freopen ((s + ".in").c_str(), "r", stdin);
		freopen ((s + ".out").c_str(), "w", stdout);
	}
#endif
}

const int NMAX = 100100;
vector<int> v;
ll MIN = INF;

ll rec(ll j, ll a, ll cnt)
{
	if (j == v.size()) 
		return MIN = cnt;
	if (a == 1) return MIN = v.size() - j;

	ll k = 0;
	while (a <= v[j])
	{
		a += a - 1;
		k++;
	}
	ll t = rec(j + 1, a + v[j], cnt + k);
	if (t - cnt >= v.size() - j)
	{
		MIN = min(MIN, (ll)(cnt + v.size() - j));
	}

	return t;
}

int main ()
{
	clock_t time = clock();
	prepare ("");

	ll t, a, n, val;
	cin >> t;

	forn(i, t)
	{
		MIN = INF;
		cin >> a >> n;
		forn(j, n)
		{
			cin >> val;
			v.push_back(val);
		}

		sort(v.begin(), v.end());

		rec(0, a, 0);
		cout << "Case #" << i + 1 << ": " <<  MIN << endl;

		v.clear();
	}

	time = clock() - time;
	//cout << endl << (double)time / CLOCKS_PER_SEC;
	return 0;
}