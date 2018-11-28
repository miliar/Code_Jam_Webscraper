#pragma comment(linker, "/STACK:1073741824")
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <iostream>
#include <functional>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
#include <cassert>
#include <cmath>
#include <ctime>
#include <sstream>

#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define fornd(i,n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i,b,a) for (int i = (int)(b); i >= (int)(a); i--)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define _(a, val) memset (a, val, sizeof(a))
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
const ld eps = 1e-9;
const int INF = 1000000000;

using namespace std;

void prepare(string s){
#ifndef _DEBUG
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (s != "")
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

vector <ll> a;

void readdata ()
{
	
}

void writedata ()
{

}

int lennum (int k)
{
	int len = 0;
	while (k > 0)
	{
		k /= 10;
		len ++;
	}

	return len;
}

ll mpow (int a, int n)
{
	ll res = 1;
	forn(i, n)
		res *= a;
	return res;
}

ll rev (int k)
{
	ll res = 0;
	while (k > 0)
	{
		res = res*10 + k % 10;
		k /= 10;
	}
	return res;
}

bool isPal (ll k)
{
	stringstream ss("");
	ss << k;
	string s;
	ss >> s;
	string t = s;
	reverse ( all (t) );
	return s == t;
}

void solve ()
{
	for (int i = 1; i < 10000000; i++)
	{
		ll t = i * mpow(10, lennum ( i )) + rev ( i );
		if (t > 10000000)
			break;
		if (isPal (t*t))
			a.pb ( t*t );
	}
	for (int i = 1; i < 10000000; i++)
	{
		for (int j = 0; j < 10; j ++)
		{
			ll t = (i*10ll + j) * mpow(10, lennum ( i )) + rev ( i );
			if (t > 10000000)
				break;
			if (isPal (t*t))
				a.pb ( t*t );
		}
	}

	a.pb ( 1 );
	a.pb ( 4 );
	a.pb ( 9 );

	sort (all(a));
	a.erase ( unique(all(a)), a.end());

	int t;
	scanf ("%d", &t);
	forn(i, t)
	{
		printf ("Case #%d: ", i + 1);
		ll l, r;
		scanf ("%lld %lld", &l, &r);
		int ans = 0;
		for (int j = 0; j < a.size(); j++)
			if (l <= a[j] && a[j] <= r)
				ans ++;
		printf ("%d\n", ans);
	}
}

int main ()
{
	prepare("");

	readdata ();
	solve ();
	writedata ();

    return 0;
}
