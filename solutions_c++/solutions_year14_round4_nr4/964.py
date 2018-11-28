#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;
typedef long long LL;
typedef vector<LL> VLL;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
const int INF = 1000000001;
const double EPS = 10e-9;

bool Permutate(VI& div, int m)
{
	div[0]++;
	REP(x, SIZE(div))
	{
		if(div[x] == m)
		{
			div[x] = 0;
			if(x + 1 == SIZE(div)) return true;
			div[x + 1]++;
		}
		else
		{
			break;
		}
	}
	return false;
}

int main()
{
	int t, n, m, q, w, r;
	LL b;
	cin >> t;
	FOR(o, 1, t)
	{
		w = r = 0;
		cin >> n >> m;
		vector<string> str(n);
		VI div(n, 0);
		REP(x, n) cin >> str[x];
		while(1)
		{
			q = 0;
			REP(s, m)
			{
				set<int> k;
				k.insert(0);
				REP(i, n) if(div[i] == s)
				{
					b = 0;
					REP(x, SIZE(str[i]))
					{
						b *= 27;
						b += str[i][x] - '@';
						k.insert(b);
					}
				}
				if(SIZE(k) > 1) q += SIZE(k);
			}
			if(q > w)
			{
				w = q;
				r = 1;
			}
			else if(q == w) r++;
			if(Permutate(div, m)) break;
		}
		cout << "Case #" << o << ": " << w << " " << r << endl;
	}
	return 0;
}
