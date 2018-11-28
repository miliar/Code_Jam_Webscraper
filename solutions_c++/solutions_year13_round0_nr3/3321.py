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
vector<ll> v (30);

int main ()
{
	prepare ("");

	v[0] = 1;
	v[1] = 4;
	v[2] = 9;
	v[3] = 121;
	v[4] = 484;
	v[5] = 10201;
	v[6] = 12321;
	v[7] = 14641;
	v[8] = 40804;
	v[9] = 44944;
	v[10] = 1002001;
	v[11] = 1234321;
	v[12] = 4008004;
	v[13] = 100020001;
	v[14] = 102030201;
	v[15] = 104060401;
	v[16] = 121242121;
	v[17] = 123454321;
	v[18] = 125686521;
	v[19] = 400080004;
	v[20] = 404090404;

	int T = 0, a = 0, b = 0, cnt = 0;
	cin >> T;

	forn(i, T)
	{
		cnt = 0;
		cin >> a >> b;
		forn(i, 21)
		{
			if (v[i] >= a && v[i] <= b)
				cnt++;
		}
		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}

	return 0;
}