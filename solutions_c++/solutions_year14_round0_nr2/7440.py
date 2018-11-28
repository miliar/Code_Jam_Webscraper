#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstring>
#include <string>
#include <stack>
using namespace std;

typedef long long LL;
typedef long double LD;
#define first ST
#define second ND
#define push_back PB
#define make_pair MP
#define SIZE(v) ((int)(v).size())
#define REP(i,n) for(typeof(n)i=0;i<(n);++i)
#define FOR(i,a,b) for(typeof(a)i=(a);i<=(b);++i)
#define FORD(i,a,b) for(typeof(a)i=(a);i>=(b);--i)
#define FOREACH(it,v) for(typeof((v).begin())it=(v).begin();it!=(v).end();++it)
#define ALL(v) ((v).begin(),(v).end())

int main()
{
	int q;
	scanf("%d", &q);

	FOR(i,1,q)
	{
		LD p = 2.0, b, x, c, t = 0.0;
		scanf("%Lf%Lf%Lf", &c,&b,&x);
		t = c / p;
		while((x-c)*(p+b)> x*p)
		{
			p += b;
			t += c / p;
		}
		t += (x-c)/p;
		printf("Case #%d: %.8Lf\n", i,t);
	}

	return 0;
}
