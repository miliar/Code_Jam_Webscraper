#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
#include <fstream>
#include <cassert>
#ifdef HOME_PC
#include <ctime>
#endif
using namespace std;

#pragma comment(linker,"/stack:16000000")
#pragma warning (disable : 4996)

#define ALL(v) v.begin(),v.end()
#define SZ(v) (int)v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=(start);i<(N);++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)
#define sqr(x) ((x)*(x))


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

bool possible(const VVI& a)
{
	int n = a.size();
	int m = a[0].size();
	VI maxInRow(n, -1), maxInCol(m,-1);
	FOR(i,0,n) FOR(j,0,m)
		maxInRow[i] = max(maxInRow[i], a[i][j]), maxInCol[j] = max(maxInCol[j], a[i][j]);
	FOR(i,0,n) FOR(j,0,m)
	{
		if(a[i][j] < min(maxInRow[i], maxInCol[j]))
			return false;
	}
	return true;
}

int main()
{
#ifdef HOME_PC
	freopen ("B-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("B-large.out","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		int n,m; cin>>n>>m;
		VVI a(n, VI(m, 0));
		FOR(i,0,n) FOR(j,0,m) cin>>a[i][j];
		printf("Case #%d: %s\n",cas,possible(a) ? "YES":"NO");
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

