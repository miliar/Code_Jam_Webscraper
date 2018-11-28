#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string.h>
#include <cassert>
#include <unordered_set>
#include <unordered_map>

#define mp make_pair
#define pb push_back
#define problem "test"
typedef __int128 ll;
typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long ull;
const int z = 111111;
const int n = 32;
const double eps = 1e-9;
const int inf = int(1e9);
const ll llinf = ll(1e18);
using namespace std;

int a[n];
ll get(ll x)
{
	for (ll i = 2; i * i <= x && i <= 100; i++)
		if (!(x % i))
			return i;
	return -1;
}
int k;
void check()
{
    vector <int> d;
	for (ll base = 2; base < 11; base++)
	{
	    ll res = 0;
//	    for (int i = 0; i < n; i++)
//	    	cout << a[i];
//		cout << "\t";
		for (int i = 0; i < n; i++)
		{
			res *= base;
			res += a[i];
		}
//		cout << res << " (base = " << base << ")\t\t\t";
		ll tmp = get(res);
		if (tmp == -1)
		{
			for (int i = 0; i < n; i++)
	    		cerr << a[i];
			cerr << "\tis bad\t" << k << "\n";
			return;

		}
		d.pb(tmp);
	}
	for (int i = 0; i < n; i++)
		cout << a[i];
	cout << " ";
	for (ll x : d)
		cout << (long long)x << " ";
	cout << "\n";					         
	k++;
	cerr << k << "\n";
    if (k == 500)
		exit(0);
}
void gen(int k)
{
	if (k == n - 1)
	{
		check();
		return;
	}
	a[k] = 0;
	gen(k + 1);
	a[k] = 1;
	gen(k + 1);
	a[k] = 0;
}
int main()
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	freopen(problem".in", "r", stdin);
	freopen(problem".out", "w", stdout);
	a[0] = a[n - 1] = 1;
	gen(1);
	return 0;
}