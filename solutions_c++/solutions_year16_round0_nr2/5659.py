/* Problem B. Revenge of the Pancakes */


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
#define TASK "B-large"

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



int main()
{
	freopen(TASK".in", "r", stdin);
	freopen(TASK".out", "w", stdout);

	int t;
	cin >> t;
	forn(tt, t)
	{
		string s;
		cin >> s;
		reverse(all(s));

		int cnt = 0;
		char prev = '+';
		forn(i, s.length())
		{
			if (s[i] != prev)
				++cnt;
			prev = s[i];
		}

		cout << "Case #" << tt + 1 << ": " << cnt << endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
