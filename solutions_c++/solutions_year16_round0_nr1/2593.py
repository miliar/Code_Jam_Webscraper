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
const double eps = 1e-9;
const int inf = int(1e9);
const ll llinf = ll(1e18);
using namespace std;

unordered_set <int> used;

void check(ll x)
{
	while (x)
	{
		used.insert(x % 10);
		x /= 10;
	}
}
string print(ll x)
{
	string res;
	while (x)
	{
		res += (x % 10 + '0');
		x /= 10;
	}
	reverse(res.begin(), res.end());
	return res;
}
int main()
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	freopen(problem".in", "r", stdin);
	freopen(problem".out", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
	    int ok = 0;
	    used.clear();
	    ll n;
	    long long tmp;
		cin >> tmp;
		n = tmp;
		if (!(tmp % 2500))
			cerr << tmp << "\n";
		for (ll i = 1; i < 1e6; i++)
		{
			if (!n)
				break;
			check(i * n);
			if (used.size() == 10)
			{
				cout << "Case #" << test << ": " << print(i * n) << "\n";
				ok = 1;
				break;
			}
		}
		if (!ok)
			cout << "Case #" << test << ": INSOMNIA\n";
	}
	return 0;
}