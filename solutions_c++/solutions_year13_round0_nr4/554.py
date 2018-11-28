#include <numeric>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <map>
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

const int MAX_N = 20;

struct Keys
{
	int cnt[MAX_N], tot;
	void add ( const Keys& o ) {
		for ( int i = 0; i < MAX_N; ++i )
			cnt[i] += o.cnt[i];
	}
	void clear ( ) { memset ( cnt, 0, sizeof ( cnt ) ); }
};

int n;
map<int,int> mapa;
int choise[1<<MAX_N]; //choise
bool ok[1<<MAX_N];
int wanted[MAX_N];
Keys inNode[MAX_N], start;

void clearMemo ( ) {
	mapa.clear();
	start.clear();
	for ( int i = 0; i < MAX_N; ++i )
		inNode[i].clear();
}

int parse ( int num ) {
	if ( !mapa.count ( num ) ) {
		int numId = mapa.size();
		mapa[num] = numId;
	}
	return mapa[num];
}

void readInput ( ) {
	int k;
	vector<int> vStart, vWanted, vInNode[MAX_N];

	scanf ( "%d%d", &k, &n );
	
	vStart.resize ( k );
	for ( int i = 0; i < k; ++i )
		scanf ( "%d", &vStart[i] );

	vWanted.resize ( n );
	for ( int i = 0; i < n; ++i )
	{
		scanf ( "%d", &vWanted[i] );
		wanted[i] = parse ( vWanted[i] );

		scanf ( "%d", &k );
		vInNode[i].resize ( k );
		for ( int j = 0; j < k; ++j )
			scanf ( "%d", &vInNode[i][j] );
	}

	for ( int i = 0; i < (int)vStart.size(); ++i )
		if ( mapa.count ( vStart[i] ) )
			start.cnt[mapa[vStart[i]]]++;
	
	for ( int i = 0; i < n; ++i )
		for ( int j = 0; j < (int)vInNode[i].size(); ++j )
			if ( mapa.count ( vInNode[i][j] ) )
				inNode[i].cnt[ mapa[vInNode[i][j]] ]++;
}

void dodp ( )
{
	Keys cur;
	for ( int m = (1<<n)-1; m >= 0; --m )
	{
		bool& ans = ok[m];
		int& ch = choise[m];
		ch = -1;
		
		cur.clear();
		cur.add ( start );
		for ( int i = 0; i < n; ++i )
			if ( m & ( 1 << i ) ) {
				cur.add ( inNode[i] );
				cur.cnt[wanted[i]]--;
			}
		
		int minCnt = *min_element ( cur.cnt, cur.cnt+MAX_N );
		if ( 0 > minCnt ) ans = false;
		else if ( m+1 == (1<<n) ) ans = true;
		else
		{
			ans = false;
			for ( int i = 0; i < n; ++i )
				if ( ( m & ( 1 << i ) ) == 0 && cur.cnt[wanted[i]] > 0 )
					if ( ok[m|(1<<i)] ) {
						ans = true;
						ch = i;
						break;
					}
		}
	}
}

void printAnswer ( int curCase )
{
	printf ( "Case #%d:", curCase );
	if ( !ok[0] )
		printf ( " IMPOSSIBLE\n" );
	else
	{
		int m = 0;
		while ( m+1 != (1<<n) ) {
			assert ( ok[m] );
			printf ( " %d", choise[m]+1 );
			m = (m|(1<<choise[m]));
		}
		printf ( "\n" );
	}
}

void solveCase ( int curCase )
{
	clearMemo();
	readInput();
	dodp();
	printAnswer(curCase);
}

int main ( )
{
	//freopen ( "D-small-attempt1.in", "r", stdin );
	//freopen ( "D.out", "w", stdout );
	
	int nCases;
	scanf ( "%d", &nCases );
	for ( int curCase = 1; curCase <= nCases; ++curCase )
		solveCase ( curCase );
	
	return 0;
}
