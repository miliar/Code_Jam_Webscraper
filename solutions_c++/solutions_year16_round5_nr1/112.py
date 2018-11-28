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

#define N 256000
int n;
char a[N];
//int d[N][N];

int smart()
{
	int r = 0;
	string st;
	REP(i,n) {
		if (st.empty() || st.back() != a[i]) {
			st.push_back(a[i]);
		}
		else
		{
			st.pop_back();
			r+=10;
		}
	}
	return r+(st.size()/2)*5;
}

int main(int argc, char **argv)
{
	string FN = "A-large";
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
		scanf("%s",a);
		n=strlen(a);
		/*CLEAR(d);
		REP(len,n+1) REP(s,n) {
			if (s+len>n) continue;
			if (len<2) continue;
			REP(mid,len-2+1) if (mid%2==0)
			{
				d[s][len] = max(d[s][len], d[s+1][mid]+d[s+mid+2][len-mid-2]+(a[s]==a[s+mid+1] ? 10 : 5));
			}
		}*/
		printf("%d\n",smart());
		//if (d[0][n] != smart()) fprintf(stderr,"!!! diff %d %d\n",d[0][n],smart());
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}