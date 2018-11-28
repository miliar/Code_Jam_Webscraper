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
int t;
vector <char> g;
string s;
int ruch;
int greedy()
{
	int wyn=0;
	int lpos=-1;
	FORD(i,SIZE(g)-1,0)
	{
		if(g[i]=='-')
		{
			lpos=i;
			break;
		}
	}
	if(lpos<0)
	return 0;
	wyn=1;
	FOR(i,1,lpos)
	{
		if(g[i]!=g[i-1])
		wyn++;
	}
	return wyn;
}
int main()
{
	scanf("%d", &t);
	getline(cin,s);
	FOR(tt,1,t)
	{
		printf("Case #%d: ",tt);
		g.clear();
		s.clear();
		getline(cin,s);
		
		REP(i,SIZE(s))
		{
			if(s[i]=='+' || s[i]=='-')
			g.PB(s[i]);
		}
		printf("%d\n",greedy());
	}

}






