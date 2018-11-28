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

int main ()
{
	clock_t time = clock();
	prepare ("");

	ll T = 0, r = 0, t = 0;
	cin >> T;

	ll sum = 0, r1 = 0;
	ll cnt = 0;
	forn(i, T)
	{
		cnt = 0;
		sum = 0;
		cin >> r >> t;

		r1 = r + 1;
		while (1)
		{
			if (sum + (r1*r1 - r*r) > t)
				break;
			sum += (r1*r1 - r*r);
			r1 += 2;
			r += 2;
			cnt++;
		}

		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}

	time = clock() - time;
	//cout << endl << (double)time / CLOCKS_PER_SEC;
	return 0;
}