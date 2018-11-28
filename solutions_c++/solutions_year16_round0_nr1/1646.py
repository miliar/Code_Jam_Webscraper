#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <complex>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>

using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PF push_front

int n;
LL a,b,c,k;
int seen[10];
int nr,mak;
LL check(int x)
{
	REP(i,10)
	seen[i]=0;
//	pos=0;
	LL num;
	num=1;
	bool koniec;
	FOR(i,1,1000)
	{
		koniec=true;
		num=((LL)(i))*((LL)(x));
		while(num>0)
		{
			seen[num%10]=1;
			num/=10;
		}
		REP(p,10)
		{
			if(seen[p]==0)
			koniec=false;
		}
		if(koniec)
		return (LL)(i);
	}
	return -1;
}
int main()
{
	int t;
	LL wyn;
	scanf("%d", &t);
	FOR(tt,1,t)
	{
		printf("Case #%d: ",tt);
		scanf("%d", &nr);
		//nr=tt; //fml
		wyn=check(nr);
		if(wyn>=0)
		printf("%lld\n",wyn*((LL)(nr)));
		else
		printf("INSOMNIA\n");
	}
}
