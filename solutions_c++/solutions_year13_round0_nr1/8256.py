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

#define PLX 0
#define PLO 1
#define PLT 2
#define PLDOT 3


char table[40][40];


bool check(char who)
{
	FOR(i, 0, 3)
	{
		bool x = true;
		FOR(j,0,3)
		{
			if( table[i][j] != who && table[i][j] != PLT )
			{
				x = false;
				break;
			}
		}
		if( x ) return true;
	}
	FOR(j, 0, 3)
	{
		bool x = true;
		FOR(i,0,3)
		{
			if( table[i][j] != who && table[i][j] != PLT )
			{
				x = false;
				break;
			}
		}
		if( x ) return true;
	}
	bool x = true;
	FOR(i,0,3)
	{
		if( table[i][i] != who && table[i][i] != PLT )
		{
			x = false;
			break;
		}
	}
	if( x ) return true;
	x = true;
	FOR(i,0,3)
	{
		if( table[i][3-i] != who && table[i][3-i] != PLT )
		{
			//printf("(%d %d)\n",i,3-i);
			x = false;
			break;
		}
	}
	if( x ) return true;
	return false;
}


bool may(char who)
{
	FOR(i, 0, 3)
	{
		bool x = true;
		FOR(j,0,3)
		{
			if( table[i][j] != who && table[i][j] != PLT && table[i][j] != PLDOT )
			{
				x = false;
				break;
			}
		}
		if( x ) return true;
	}
	FOR(j, 0, 3)
	{
		bool x = true;
		FOR(i,0,3)
		{
			if( table[i][j] != who && table[i][j] != PLT && table[i][j] != PLDOT )
			{
				x = false;
				break;
			}
		}
		if( x ) return true;
	}
	bool x = true;
	FOR(i,0,3)
	{
		if( table[i][i] != who && table[i][i] != PLT && table[i][i] != PLDOT )
		{
			x = false;
			break;
		}
	}
	if( x ) return true;
	x = true;
	FOR(i,0,3)
	{
		if( table[i][3-i] != who && table[i][3-i] != PLT && table[i][3-i] != PLDOT )
		{
			//printf("(%d %d)\n",i,3-i);
			x = false;
			break;
		}
	}
	if( x ) return true;
	return false;
}

int main(int argc, char **argv)
{
	int TT;
	scanf("%d",&TT);
	for(int xxx = 1; xxx <= TT; ++xxx)
	{
		char temp[5];
		FOR(i,0,3)
		{
			scanf("%s",&temp[0]);
			//printf("/ %s /\n",temp);
			FOR(j,0,3)
			{
				//table[i][j] = (temp[j] == 'X')?PLX:(temp[j] == 'Y')?PLO:(temp[j] == '.')?PLDOT:PLT;
				if( temp[j] == 'X' ) table[i][j] = PLX;
				if( temp[j] == 'O' ) table[i][j] = PLO;
				if( temp[j] == '.' ) table[i][j] = PLDOT;
				if( temp[j] == 'T' ) table[i][j] = PLT;
			}
		}
		/*FOR(i,0,3)
		{
			FOR(j,0,3)
				printf("%d ",table[i][j]);
			printf("\n");
		}*/
		printf("Case #%d: ",xxx);
		bool chX = check(PLX), chY = check(PLO);

		if( chX )
		{
			printf("X won");
		}
		else if( chY )
		{
			printf("O won");
		}
		else if( may(PLX) || may(PLO) )
		{
			printf("Game has not completed");
		}
		else
		{
			printf("Draw");
		}
		printf("\n");
	}
}
