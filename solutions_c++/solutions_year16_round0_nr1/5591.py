/* Problem A. Counting Sheep */


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

#define FOR(i, s, f) for (int (i) = (s); (i) < (f); ++(i))
#define ROF(i, f, s) for (int (i) = (f) - 1; (i) >= (s); --(i))
#define forn(i, f) for (int (i) = 0; (i) < (f); ++(i))
#define rofn(i, f) for (int (i) = (f) - 1; (i) >= 0; --(i))
#define all(x) (x).begin(), (x).end()
#define TASK "A-large"

typedef const int cint;
typedef unsigned int uint;
typedef long long ll;
typedef const long long cll;
typedef unsigned long long ull;
typedef long double ld;
typedef const long double cld;
typedef pair < int, int > pi;
typedef pair < ll, ll > pll;
typedef pair < ld, ld > pld;
typedef vector < int > vi;
typedef vector < vi > vvi;
typedef vector < vvi > vvvi;
typedef vector < vvvi > vvvvi;
typedef vector < ll > vll;
typedef vector < ld > vld;
typedef vector < string > vs;
typedef set < int > si;
typedef set < ll > sll;
typedef set < ld > sld;
typedef set < string > ss;
typedef map < int, int > mi;
typedef map < ll, ll > mll;
typedef map < int, ll > mill;
typedef map < ll, int > mlli;
typedef map < int, string > mis;
typedef map < string, int > msi;

bool countt[14];

bool check_count()
{
	forn(i, 10)
		if (!countt[i])
			return false;
	return true;
}

int main()
{
	freopen(TASK".in", "r", stdin);
	freopen(TASK".out", "w", stdout);

	//	cout.precision(30);

	int t;
	cin >> t;
	forn(i, t)
	{
		int n;
		cin >> n;

		cout << "Case #" << i + 1 << ": ";

		if (n == 0)
			cout << "INSOMNIA";
		else
		{
			memset(countt, 0, sizeof(countt));

			int tt;
			for (tt = 1; !check_count(); ++tt)
			{
				int cur = tt * n;

				do
				{
					countt[cur % 10] = true;
					cur /= 10;
				} while (cur != 0);
			}
			cout << (tt - 1) * n;
		}

		cout << endl;
	}

	//	fclose(stdin);
	//	fclose(stdout);
	return 0;
}
