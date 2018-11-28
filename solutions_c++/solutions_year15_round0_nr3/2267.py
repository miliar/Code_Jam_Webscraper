#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
 
using namespace std;
 
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define forn1(i, n) for(int i = 1; i <= (int)(n); i++)
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)((a).size())
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define x first
#define y second
#define y1 __y1
#define sqr(x) ((x) * (x))
 
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
 
const int INF = (int)(1e9);
const li INF64 = (li)(INF) * (li)(INF);
const ld eps = 1e-9;
const ld pi = ld(3.1415926535897932384626433832795);
 
bool in(int i, int j, int n, int m)
{
    return i >= 0 && i < n && j >= 0 && j < m;
}
 
inline int myrand()
{
    return (rand() ^ (rand() << 15));
}
 
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
 
const int N = 1e4 + 555;

char a[N];
string s;
int L, X;
int n;
 
inline bool read()
{
	if(!(cin >> L >> X))
		return false;

	assert(cin >> s);
	assert(sz(s) == L);
	string ss = s;

	forn(i, X - 1)
	{
		s += ss;
	}

	n = L * X;
	assert(sz(s) == n);
	forn(i, n)
	{
		a[i + 1] = s[i];
	}

    return true;
}

inline void gen()
{
	return;
}


inline pair<char, char> mul(const char &b, const pair<char, char> &a)
{
	char sign = a.X, c1 = a.Y, c2 = b;

	if(sign == '-')
	{
		if(c1 == 'i')
		{
			if(c2 == 'i')
			{
				return mp('+', '1');
			}

			if(c2 == 'j')
			{
				return mp('+', 'k');
			}

			if(c2 == 'k')
			{
				return mp('-', 'j');
			}
		}
		else
			if(c1 == 'j')
			{
				if(c2 == 'i')
				{
					return mp('-', 'k');
				}

				if(c2 == 'j')
				{
					return mp('+', '1');
				}

				if(c2 == 'k')
				{
					return mp('+', 'i');
				}
			}
			else
				if(c1 == 'k')
				{
					if(c2 == 'i')
					{
						return mp('+', 'j');
					}

					if(c2 == 'j')
					{
						return mp('-', 'i');
					}

					if(c2 == 'k')
					{
						return mp('+', '1');
					}
				}
				else
				{
					assert(c1 == '1');
					return mp('-', c2);
				}
	}
	else
	{
		if(c1 == 'i')
		{
			if(c2 == 'i')
			{
				return mp('-', '1');
			}

			if(c2 == 'j')
			{
				return mp('-', 'k');
			}

			if(c2 == 'k')
			{
				return mp('+', 'j');
			}
		}
		else
			if(c1 == 'j')
			{
				if(c2 == 'i')
				{
					return mp('+', 'k');
				}

				if(c2 == 'j')
				{
					return mp('-', '1');
				}

				if(c2 == 'k')
				{
					return mp('-', 'i');
				}
			}
			else
				if(c1 == 'k')
				{
					if(c2 == 'i')
					{
						return mp('-', 'j');
					}

					if(c2 == 'j')
					{
						return mp('+', 'i');
					}

					if(c2 == 'k')
					{
						return mp('-', '1');
					}
				}
				else
				{
					assert(c1 == '1');
					return mp('+', c2);
				}
	}

	assert(false);
}

inline pair<char, char> mul(const pair<char, char> &a, const char &b)
{
	char sign = a.X, c1 = a.Y, c2 = b;

	if(sign == '-')
	{
		if(c1 == 'i')
		{
			if(c2 == 'i')
			{
				return mp('+', '1');
			}

			if(c2 == 'j')
			{
				return mp('-', 'k');
			}

			if(c2 == 'k')
			{
				return mp('+', 'j');
			}
		}
		else
			if(c1 == 'j')
			{
				if(c2 == 'i')
				{
					return mp('+', 'k');
				}

				if(c2 == 'j')
				{
					return mp('+', '1');
				}

				if(c2 == 'k')
				{
					return mp('-', 'i');
				}
			}
			else
				if(c1 == 'k')
				{
					if(c2 == 'i')
					{
						return mp('-', 'j');
					}

					if(c2 == 'j')
					{
						return mp('+', 'i');
					}

					if(c2 == 'k')
					{
						return mp('+', '1');
					}
				}
				else
				{
					assert(c1 == '1');
					return mp('-', c2);
				}
	}
	else
	{
		if(c1 == 'i')
		{
			if(c2 == 'i')
			{
				return mp('-', '1');
			}

			if(c2 == 'j')
			{
				return mp('+', 'k');
			}

			if(c2 == 'k')
			{
				return mp('-', 'j');
			}
		}
		else
			if(c1 == 'j')
			{
				if(c2 == 'i')
				{
					return mp('-', 'k');
				}

				if(c2 == 'j')
				{
					return mp('-', '1');
				}

				if(c2 == 'k')
				{
					return mp('+', 'i');
				}
			}
			else
				if(c1 == 'k')
				{
					if(c2 == 'i')
					{
						return mp('+', 'j');
					}

					if(c2 == 'j')
					{
						return mp('-', 'i');
					}

					if(c2 == 'k')
					{
						return mp('-', '1');
					}
				}
				else
				{
					assert(c1 == '1');
					return mp('+', c2);
				}
	}

	assert(false);
}

bool goodpref[N], goodsuff[N];
bool gs2[N];

inline void solve()
{
	pair<char, char> curmul = mp('+', '1');

	for(int i = 1; i <= n; i++)
	{
		curmul = mul(curmul, a[i]);
		if(curmul == mp('+', 'i'))
		{
			goodpref[i] = true;
		}
	}

	pair<char, char> mull = mp('+', '1');

	for(int j = n; j >= 1; j--)
	{
		mull = mul(a[j], mull);
		if(mull == mp('+', 'k'))
		{
			goodsuff[j] = true;
		}
	}	

	int mx2 = 0;
	for(int j = 3; j <= n; j++)
	{
		if(goodsuff[j])
		{
			mx2 = max(mx2, j);
		}
	}

	int wasp = 0;
	for(int i = 1; i <= n - 2; i++)
	{
		if(goodpref[i])
		{
			wasp = 1;
		}
	}

	if(wasp == 0 || mx2 == 0)
	{
		cout << "NO" << endl;
		return;
	}

	for(int i = 1; i <= n; i++)
	{
		if(!goodpref[i])
			continue;
		pair<char, char> cur = mp('+', '1');
		for(int j = i + 1; j < n; j++)
		{
			if(mx2 <= j)
				break;
			cur = mul(cur, a[j]);
			if(cur == mp('+', 'j') && goodsuff[j + 1])
			{
				cout << "YES" << endl;
				return;
			}
		}
	}

	cout << "NO" << endl;
    return;
}

inline void clear()
{
	memset(goodpref, false, sizeof goodpref);
	memset(goodsuff, false, sizeof goodsuff);
	//memset(gs2, false, sizeof gs2);
	return;
}
 
int main(){
#ifdef _DEBUG
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
 
    cout << setprecision(10) << fixed;
    cerr << setprecision(10) << fixed;
 
    srand(int(time(NULL)));

	int T;
	assert(cin >> T);
 
	forn(test, T)
	{
		cerr << "RUNNING on test == " << test + 1 << endl;
		int startT = clock();
		assert(read());
		//gen();
		cout << "Case #" << test + 1 << ": ";
		solve();
		clear();
		int endT = clock();
		int Time = endT - startT;
		cerr << "Test " << test + 1 << " passed with TIME == " << Time << " ms" << endl;
		cerr << "Summary TIME == " << clock() << endl << endl << endl;
	}
 
    cerr << "TIME == " << clock() << " ms" << endl;
    return 0;
}