#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cstring>
using namespace std;

#define mp make_pair
#define pp push_back
#define Sort(x) sort(x.begin(), x.end())
#define rep(i, x, y) for(int i = x; i < y; i++)
#define Rep(i, x, y) for(int i = x; i <= y; i++)
#define vi vector<int>
#define vvi vector<vector<int> >
#define ll long long
#define all(v) v.begin(),v.end()
#define ii pair<int, int>
#define mem(x, v) memset(x, v, sizeof(x))
#define nl '\n'

ll gcd(ll x, ll y)
{
	if(!(y % x))
		return x;
	else
		return gcd(y % x, x);
}


int main()
{
	int t;
	char ch;
	ll p, q;
	ll temp;
	ll res;
	bool possible;
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("aaelfout.txt", "w", stdout);
	cin >> t;
	Rep(i, 1, t)
	{
		possible = true;
		cin >> p >> ch >> q;
		temp = gcd(p, q);
		p/= temp;
		q/= temp;
		if(ceill(logl(q) / logl(2)) != floor(logl(q) / logl(2)))
			possible = false;
		if(possible)
		{
			temp = min(q / 2, p);
			q = ceill((long double) q / (long double)temp) ;
			res = ceill(logl(q) / logl(2));
		}
		cout << "Case #" << i <<": ";
		if(possible)
			cout << res << nl;
		else
			cout << "impossible" << nl;
	}

	return 0;
}