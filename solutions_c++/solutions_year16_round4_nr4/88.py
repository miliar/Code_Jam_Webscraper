#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:32000000")
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define N 32
int n;
bool a[N][N];
bool seen[1<<4][1<<4];

bool canstuck(int w, int m)
{
	if (seen[w][m]) return false;
	seen[w][m]=true;
	REP(i,n) if (!(w&(1<<i)))
	{
		bool any=false;
		REP(j,n) if (!(m&(1<<j)) && a[i][j])
		{
			any=true;
			if (canstuck(w|(1<<i), m|(1<<j))) return true;
		}
		if (!any) return true;
	}
	return false;
}

int main(int argc, char **argv)
{
	string FN = "D-small-attempt0";
	if (argc>1) FN = string(argv[1]);
	int shift = 0;
	if (argc>2) sscanf(argv[2],"%d",&shift);
	freopen((FN+".in").c_str(),"r",stdin);
	freopen((FN+".out").c_str(),"w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"=== %s : %d\n", FN.c_str(), test+shift);
		printf("Case #%d: ",test+shift);
		////////////////////////////////////////////////////////////
		scanf("%d",&n);
		REP(i,n) REP(j,n)
		{
			char c;
			do c=getc(stdin); while (!isdigit(c));
			a[i][j]=c=='1';
		}
		int start = 0;
		REP(i,n) REP(j,n) if (a[i][j]) start |= 1<<(i*n+j);
		int res=n*n;
		REP(mask,1<<(n*n)) if ((mask & start) == start) {
			int nw = 0;
			REP(i,n) REP(j,n) a[i][j] = (mask & (1<<(i*n+j))) != 0;
			REP(i,n*n) if ((mask^start)&(1<<i)) ++nw;
			CLEAR(seen);
			if (canstuck(0,0)) continue;
			res = min(res,nw);
		}
		printf("%d\n",res);
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}