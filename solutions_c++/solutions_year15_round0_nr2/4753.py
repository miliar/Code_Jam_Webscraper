//#pragma comment(linker, "/stack:1000000")

#include <ctime>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define MP make_pair
const double EPS=1e-7;
const double Pi=acos(-1.0);
#define FILL(a,v) memset(a,v,sizeof(a))
#define INF 1000000000

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PII;

int sdiv(int a, int b)
{
	if (a%b == 0)
		return a/b;
	else
		return a/b + 1;
}

int cnt(int k, int t)
{
	if (k<=t)
		return 0;
	return sdiv(k,t)-1;
}

VI p;

bool can(int t) {
	for (int eat=1; eat<=t; ++eat) {
		int split = 0;
		for(int i = 0; i<p.size(); ++i) {
			split += cnt(p[i], eat);
		}
		if (split+eat<=t)
			return true;
	}
	return false;
}

int solve() {
	int n;
	cin>>n;
	p.resize(n);
	REP(i,n) {
		cin>>p[i];		
	}	
	int l =1;
	int r = 2001;
	while (r-l > 1)
	{
		int m = (l+r)/2;
		if (can(m))
			r = m;
		else
			l = m;
	}
	while (!can(l))
		++l;
	return l;
}

int main(int argc, char** argv)
{	
	string folder = __FILE__;
	freopen("B-small-attempt0.in","r",stdin);
    freopen("bsmall_out.txt","w",stdout);
	int t;
	cin>>t;
	cerr<<t;
	REP(i,t) {
		int res = solve();
		printf("Case #%d: %d\n", i+1, res);
		cerr<<"Case "<<i+1<<": "<<res<<endl;
	}
	return 0;
}