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

vector<i64> precalced;

i64 f(i64 n)
{
	int id = lower_bound(ALL(precalced), n) - precalced.begin();
	if(id == precalced.size())
		return precalced.size();
	if(precalced[id] != n)
		--id;

	return id + 1;
}

i64 solve(i64 a, i64 b)
{
	return f(b) - f(a-1);
}

const i64 MAXN = 10000000;
//const i64 MAXN = 3;

bool pal(string s)
{
	if(s.empty()) return true;
	int l = 0;
	int r = s.size() - 1;
	while(l < r && s[l] == s[r]) { ++l; --r; }
	return l>=r;
}

bool pal(int n)
{
	stringstream ss;
	ss<<n;
	return pal(ss.str());
}

void precalc()
{
	for(i64 i = 1; i <= MAXN; ++i)
		if(pal(i) && pal(i*i))
			precalced.push_back(i*i);

	sort(ALL(precalced));
	make_unique(precalced);
}

int main()
{
#ifdef HOME_PC
	freopen ("C-small-attempt0 (1).in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("C-small-attempt0.out","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif
	precalc();
//	cout<<precalced.size()<<endl;
//	vdebug(precalced);
	int tt;
	scanf("%d",&tt);

	for(int cas = 1;cas<=tt;++cas)
	{
		i64 a,b;
		cin>>a>>b;
		printf("Case #%d: %lld\n",cas, solve(a,b));
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

