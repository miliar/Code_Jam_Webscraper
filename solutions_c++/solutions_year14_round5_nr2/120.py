#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
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
#include <time.h>
#include <functional>
using namespace std;
 
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))
 
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
const double Pi = acos(-1.0);

typedef long long Int;
typedef unsigned long long UINT;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1000000000;
const int MOD = 1000000007;

int dp[207][2007];

int H[207];
int G[207];

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int t;
	cin >> t;
	FOR(ttt,0,t)
	{
		printf("Case #%d: " , ttt + 1 );

		FILL(dp,-1);
		dp[0][1] = 0;
		int p,q,n;
		cin >> p >> q >> n;
		FOR(i,0,n)
		{
			cin >> H[i] >> G[i];
		}

		FOR(i,0,n)
		{
			FOR(j,0,10 * n + 4)
			{
				if (dp[i][j] != -1)
				{
					int kill = (H[i] + q - 1) / q;
					dp[i + 1][j + kill] = max(dp[i + 1][j + kill] , dp[i][j]);
					int hp = H[i] % q;
					if (hp == 0) hp = q;
					int k2 = (hp + p - 1) / p;
					if ( j + kill - 1 >= k2)
					{
						dp[i + 1][j + kill - 1 - k2] = max(dp[i + 1][j + kill - 1 - k2] , dp[i][j] + G[i]);
					}
				}
			}
		}
		int res = 0;
		FOR(i,0,10 * n + 4)
		{
			res = max(res , dp[n][i]);
		}
		cout << res << endl;

	}

    return 0;
}