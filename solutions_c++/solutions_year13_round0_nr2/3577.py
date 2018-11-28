/**
	site
	B name (Code: Lawnmower)
	Source: GCJ 2013
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <iterator>
#include <algorithm>
#include <functional>
#include <string>
#include <map>
#include <vector>
#include <set>

typedef long long ll;
typedef long long unsigned llu;

#define	_min(a,b)	((a)<(b)?(a):(b))
#define _max(a,b)	((a)>(b)?(a):(b))

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define REP(i,n) FOR(i,0,n)

#define MOD 1000000007
#define INF (int)1e9
#define EPS 1e-9

#define IT(a,it) for (typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define pb push_back
#define mp make_pair

// #define DEBUG

#ifdef DEBUG
	std::string tabs;
	#define INDENT		tabs+="\t"
	#define _EXIT(val)	{ UNINDENT; return val; }
	#define UNINDENT	tabs.erase(tabs.length()-1)
	#define SHOW(x)		cout << tabs << x
	#include <time.h>
	#define STARTTIME	clock_t start = clock();
	#define GETTIME		printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
	#define _DEBUG(x)	x
#else
	#define INDENT
	#define _EXIT(val)	return val
	#define UNINDENT
	#define SHOW(x)
	#define STARTTIME
	#define GETTIME
	#define _DEBUG(x)
#endif

using namespace std;

#define	LIMIT	100

int board[LIMIT][LIMIT], R, C;
bool numbers[LIMIT];

void sweep(int coor, bool row)
{
	if (row)
		REP(i, C)
			board[coor][i] = 0;
	else
		REP(i, R)
			board[i][coor] = 0;
			
	_DEBUG(
		cout << "After sweeping on " << (row ? "Row " : "Column ") << coor << endl;
		REP(i, R)
		{
			REP(j, C)
			{
				cout << board[i][j];
			}
			cout << endl;
		}
	);
}

bool possibleHeight(int h)
{
	SHOW( "Checking " << h << endl );
	
	REP(row, R)
	{
		REP(col, C)
		{
			if (board[row][col] == h)
			{
				bool cut = true;
				REP(i, C)	// by row
				{
					if (board[row][i] != 0 && board[row][i] != h)
						cut = false;
				}
				
				_DEBUG(
					if (! cut)
						SHOW( "No horizontal cut on " << row << "x" << col << endl );
				);
				
				if (cut) 
				{
					sweep(row, true);
					continue;
				}
				
				cut = true;
				REP(i, R)	// by column
				{
					if (board[i][col] != 0 && board[i][col] != h)
						cut = false;
				}
				_DEBUG(
					if (! cut)
						SHOW( "No vertical cut on " << row << "x" << col << endl );
				);
				if (cut)
					sweep(col, false);
				else
					return false;
			}
		}
	}
	
	return true;
}

void solve_saving()
{
	int t = GI;
	REP(i, t)
	{
		R = GI;
		C = GI;
		
		memset(board, 0, sizeof(board));
		int max = 0;
		
		REP(row, R)
		{
			REP(col, C)
			{
				cin >> board[row][col]; 
				numbers[board[row][col] - 1] = true;
				max = _max( max, board[row][col] );

				SHOW( board[row][col] );
			}
			SHOW( "\n" );
		}
				
		bool possible = true;
		REP(n, max)
		{
			if (numbers[n])
				if ( ! possibleHeight(n+1) )
				{
					possible = false;
					break;
				}
					
		}
		cout << "Case #" << i+1 << ": " << ( (possible) ? "YES" : "NO" ) << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
