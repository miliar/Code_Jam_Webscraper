//============================================================================
// Name        : .cpp
// Author      : Grzegorz Gajoch
// Description : 
//============================================================================

#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <ctype.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define REP(x, n) for(int x=0; x < (n); ++x)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(n) (int)n.size()
#define ALL(c) c.begin(),c.end()
#define PB(n) push_back(n)
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<bool> VB;
#define MP make_pair
#define ST first
#define ND second
const int INF = 1000000001;

#define debug

int tableSq[100000] = { 0 } ;

bool pal(int i)
{
	char x[10000];
	int end = sprintf(x,"%d",i);
	--end;
	int begin = 0;
	while( end > begin )
	{
		if( x[end] != x[begin] ) return false;
		--end;
		++begin;
	}
	return true;
}

int main(int argc, char **argv)
{
	FOR(i,1,100)
	{
		if( pal(i) && pal(i*i) ) tableSq[i*i] = 1;
		else tableSq[i*i] = 0;
	}
	//FOR(i,1,100) printf("%d: %d\n",i,tableSq[i]);
	int TT;
	scanf("%d",&TT);
	FOR(xxx,1,TT)
	{
		printf("Case #%d: ",xxx);
		int a, b;
		scanf("%d %d",&a,&b);

		int c = 0;
		FOR(i,a,b) if( tableSq[i] != 0 ) ++ c;
		printf("%d\n",c);
	}


}
