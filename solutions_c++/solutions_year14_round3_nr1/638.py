



#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <numeric>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
const ULL B = 100000007; // ¹þÏ£µÄ»ùÊý¡£


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
#define INF 1000000000
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


LL maxC(LL p, LL q)
{
	LL y = q % p;
	while(y != 0)
	{
		q = p;
		p = y;
		y = q % p;
	}
	return p;
}

bool IsBinary(LL q)
{
	while(q != 1)
	{
		if(q % 2 == 1)
		{
			return false;
		}
		q = q / 2;
	}
}

int findMP(LL p, LL q)
{
	int k = 0;
	while(p < q)
	{
		q = q / 2;
		k++;
	}
	return k;
}


int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin>>t;
	LL p,q;
	char ch;
	for(int i=1; i<=t; ++i)
	{
		cin>>p>>ch>>q;
		LL com = maxC(p, q);
		p = p / com;
		q = q / com;
		if(IsBinary(q))
		{
			int k = findMP(p,q);
			cout<<"Case #"<<i<<": "<<k<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<"impossible"<<endl;
		}

	}
	return 0;
}