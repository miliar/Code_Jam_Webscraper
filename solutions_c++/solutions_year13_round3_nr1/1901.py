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

	int t;
	cin >> t;

	string s;
	int n, l, r, a, b;
	bool flag= false;
	int ans = 0;
	forn(i, t)
	{
		ans = 0;
		cin >> s >> n;
		l = 0, r = s.size() - 1;
		s = s + 'a';
		a = 1;
		b = 0;

		flag = false;
		forn(j, s.size())
		{
			if (s[j] != 'a' && s[j] != 'e' && s[j] != 'i' && s[j] != 'o' && s[j] != 'u')
			{
				if (flag)
				{
					b = j;
				}
				else
				{
					a = j;
					b = j;
					flag = true;
				}
			}
			else
			{
				flag = false;

				if (b - a + 1 >= n)
				{
					forn(k, (b - a + 1) - n + 1)
					{
						ans += (a + k + 1 - l) * (r + 1 - (a + k + n - 1));
						l = a + k + 1;
					}

					a = 1;
					b = 0;
				}
			}
		}

		cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	time = clock() - time;
	//cout << endl << (double)time / CLOCKS_PER_SEC;
	return 0;
}