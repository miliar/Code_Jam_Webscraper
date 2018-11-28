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

using namespace std;

#define FOR(i,a,b) for(int (i)=(a);i<(b);++i)
#define RFOR(i,b,a) for(int (i)=(b)-1;i>=(a);--i)
#define FILL(A,val) memset(A,val,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define MP make_pair
#define PB push_back

typedef long long Int;
typedef unsigned long long UInt;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double Pi = acos(-1.0);
const int INF = 1000000000;
const int MAX = 1000007;
const int BASE = 1000000000;
const int ST = 1000000007;

long double dp[207][207];

long double p[207];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt" , "w", stdout);



	int t;
	cin >> t;
	FOR(tt,0,t)
	{
		printf("Case #%d: " , tt + 1);

		int n , k;
		cin >> n >> k;
		FOR(i,0,n)
		{
			cin >> p[i];
		}
		sort(p, p + n);

		double res = 0;

		int msk;

		FOR(c,0,k + 1)
		{

			FILL(dp, 0);
			vector<double> P;
			FOR(i,0,c)
			{
				P.push_back(p[i]);
			}
			FOR(i,0,k - c)
			{
				P.push_back(p[n - 1 - i]);
			}
			dp[0][0] = 1;
			FOR(i,0,k)
			{
				FOR(j,0,k / 2 + 1)
				{
					dp[i + 1][j + 1] += dp[i][j] * P[i];
					dp[i + 1][j] += dp[i][j] * (1 - P[i]);
				}
			}
			if (dp[k][k / 2] > res)
			{
				res = dp[k][k / 2];
				//msk = mask;
			}
		}

		cerr << tt << ' ' << res << endl;
		printf("%.10f\n" , res);

	}

	//cout << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	return 0;
}
