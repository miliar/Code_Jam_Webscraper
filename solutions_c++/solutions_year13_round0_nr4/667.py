#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <cstdlib>
#include <string>
#include <sstream>
#include <gmpxx.h>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define VVI vector< VI >
#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it = (kont).begin(); it!=(kont).end(); ++it)

char buff[20000];

VI start;
VI open;
VVI inside;
int N, K;
int dp[1100000];

int go( int mask )
	{
	//cout << mask << endl;
	VI imam = start;
	FOR( i, 0, N )
		if( mask & (1<<i) )
			{
			--imam[open[i]];
			FOR( j,0,200 )
				imam[j] += inside[i][j];
			}
	FOR( i, 0, N )
		if( imam[open[i]] > 0 && (mask & (1<<i))==0 && dp[mask | (1<<i)] == -1)
			{ dp[ mask | (1<<i) ] = i; go( mask | (1 << i ) ); }
	}

void obidji( int pos ) 
	{
	if ( dp[pos] == -1 ) return;
	else obidji( pos ^ (1 << dp[pos]) );
	printf(" %d",dp[pos]+1);
	}

int main()
    {
    int T;
    gets(buff);
    sscanf(buff,"%d",&T);

    FOR( t, 0, T )
        {
	cin >> K >> N;
        start.clear(); start.resize(200,0);
	open.clear(); open.resize(N);
	inside.clear(); inside.resize(N, VI(200,0) );
	
	FOR(i,0,K) { int tmp; cin >> tmp; start[tmp]++;}
	FOR(i,0,N)
		{
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2; open[i] = tmp1;
			FOR( j, 0, tmp2 ) { cin >> tmp1; inside[i][tmp1]++; }
		}
	memset( dp, -1, sizeof(dp ) );
	go(0);

	if( dp[(1 <<N ) -1] == -1 ) {printf("Case #%d: IMPOSSIBLE\n",t+1);}
	else
		{
		int pos = (1<<N)-1;
		printf("Case #%d:",t+1);
		obidji( pos );
		printf("\n");
		}
	}
    return 0;
    }
