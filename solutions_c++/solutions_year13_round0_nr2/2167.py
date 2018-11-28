# include <iostream>
# include <fstream>
# include <sstream>
# include <algorithm>
# include <cstdio>
# include <cmath>
# include <numeric>
# include <cstdlib>
# include <cstring>
# include <vector>
# include <list>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <cctype>
# include <climits>
# include <complex>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,PII> TRI;
typedef vector<string> VS;

#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) REP(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define bitcount(x) __builtin_popcount(x)
#define pb push_back
#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define EPS (double)(1e-9)
#define INF 1000000000
#define MOD 1000000007
#define PI (double)(3.141592653589793)

inline int ni()
{
	register int r=0,c;
	for(c=getchar_unlocked();c<=32;c=getchar_unlocked());
	if(c=='-')
		return -ni();
	for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar_unlocked());
	return r;
}

int a[105][105], n, m;

bool check_col(int x, int val)
{
	REP(i,0,n)
		if(a[i][x] > val)
			return false;
	return true;
}

bool check_row(int x, int val)
{
	REP(j,0,m)
		if(a[x][j] > val)
			return false;
	return true;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t;

	t = GI;

	REP(tcase,1,t+1)
	{
		n = GI; m = GI;

		REP(i,0,n)
			REP(j,0,m)
				a[i][j] = GI;
				
		REP(i,0,n)
			REP(j,0,m)
				if(!check_row(i,a[i][j]) && !check_col(j,a[i][j]))
				{
					printf("Case #%d: NO\n",tcase);
					goto next;
				}

		printf("Case #%d: YES\n",tcase);
		next:;
	}
		
	return 0;
}

