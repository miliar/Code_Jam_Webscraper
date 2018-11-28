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

int main()
{
	int t, n, s, w;
	scanf("%d", &t);
	FOR(o, 1, t)
	{
		scanf("%d%d", &n, &s);
		VI k(n);
		REP(x, n) scanf("%d", &k[x]);
		w = 0;
		sort(ALL(k));
		FORD(x, n - 1, 0) if(k[x] != INF)
		{
			FORD(y, x - 1, 0) if(k[x] + k[y] <= s)
			{
				k[y] = INF;
				break;
			}
			w++;
		}
		printf("Case #%d: %d\n", o, w);
	}
	return 0;
}
