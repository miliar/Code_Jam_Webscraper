/* Problem C. Coin Jam */


#include <set>
#include <map>
#include <vector>
#include <string>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <time.h>
#include <iostream>

using namespace std;

#define FOR(i, s, f) for (ll (i) = (s); (i) < (f); ++(i))
#define ROF(i, f, s) for (ll (i) = (f) - 1; (i) >= (s); --(i))
#define forn(i, f) for (ll (i) = 0; (i) < (f); ++(i))
#define rofn(i, f) for (ll (i) = (f) - 1; (i) >= 0; --(i))
#define all(x) (x).begin(), (x).end()
#define TASK "C-small-attempt0"

//typedef const ll cll;
//typedef unsigned ll ull;
typedef long long ll;
//typedef const long long cll;
//typedef unsigned long long ull;
//typedef long double ld;
//typedef const long double cld;
//typedef pair < ll, ll > pi;
//typedef pair < ll, ll > pll;
//typedef pair < ld, ld > pld;
typedef vector < ll > vi;
//typedef vector < vi > vvi;
//typedef vector < vvi > vvvi;
//typedef vector < vvvi > vvvvi;
//typedef vector < ll > vll;
//typedef vector < ld > vld;
//typedef vector < string > vs;
//typedef set < ll > si;
//typedef set < ll > sll;
//typedef set < ld > sld;
//typedef set < string > ss;
//typedef map < ll, ll > mi;
//typedef map < ll, ll > mll;
//typedef map < ll, ll > mill;
//typedef map < ll, ll > mlli;
//typedef map < ll, string > mis;
//typedef map < string, ll > msi;
typedef pair < ll, vi > pivi;

bool bit(ll cur, ll ind);
vector < pivi > answer;

int main()
{
	freopen(TASK".in", "r", stdin);
	freopen(TASK".out", "w", stdout);

	ll n, j;
	cin >> n >> j;

	for (ll i = 0; answer.size() < j; ++i)
	{
//		cout << answer.size() << "\r";

		vi tmp;

		int ttt = answer.size();

		ll cur = (1 << (n - 1)) + (i << 1) + 1;
		FOR(power, 2, 11)
		{
			ll number = 0;
			forn(ind, n)
			{
				if (bit(cur, ind))
					number += pow(power, ind);
			}

			ll sqr = sqrt(number) + 1;
			FOR(q, 2, sqr)
			{
				if (number % q == 0 && number != q)
				{
					tmp.push_back(q);
					break;
				}
			}
		}

		if (tmp.size() == 9)
			answer.push_back(pivi(cur, tmp));
	}

	cout << "Case #1:\n";
	for (pivi tmp : answer)
	{
		rofn(i, n)
			cout << bit(tmp.first, i);

		for (ll cur : tmp.second)
			cout << ' ' << cur;
		cout << endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}

bool bit(ll cur, ll ind)
{
	return (cur & (1 << ind));
}
