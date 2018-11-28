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

vector<Long> good;

bool isPoly(Long x)
{
	vector<int> v;
	while (x>0)
	{
		int t = x%10;		
		v.push_back(t);
		x /= 10;
	}
	REP(i, v.size())
		if (v[i] != v[v.size()-1-i])
			return false;
	return true;
}

void gen()
{	
	FOR(i,1,10000000)
		if (isPoly(i) && isPoly(1LL*i*i))
			good.pb(i);
}

void sol(int T)
{
	Long a,b;
	cin>>a>>b;
	int res = 0;
	REP(i, good.size())
	{
		Long t = good[i]*good[i];
		if (t >= a && t <=b)
			++res;
	}
	printf("Case #%d: %d\n", T, res);
}

int main(int argc, char** argv)
{
	gen();
	int t;
	cin>>t;
	REP(i, t)
		sol(i+1);
	return 0;
}