#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
#define REP(i, a, b) for(int i = int(a); i <= int(b); i++)
#define LOOP(i, v) for(int i = 0; i < v.size(); i++)
#define EPS 1e-9
#define INF 1e12
#define debug(x) cerr << "DEBUG : " << (#x) << " => " << (x) << endl

int main()
{
	int T;
	scanf("%d", &T);
	
	REP(t, 1, T)
	{
		printf("Case #%d: ", t);
		fprintf(stderr, "Case #%d.\n", t);
		
		int N, K;
		vector<double> p;
		scanf("%d %d", &N, &K);
		p.resize(N);
		REP(i, 0, N-1)
		{
			cin >> p[i];
		}
		
		sort(p.begin(), p.end());
		
		/*
		sort(p.begin(), p.end());
		
		
		vector<double> q;
		REP(i, 1, K/2)
		{
			q.push_back(p[i-1]);
			q.push_back(p[N-i]);
		}
		*/
		
		double besttot = -1;
		int whichz = -1;
		
		REP(z, 0, K) // Take the z first and K-z last
		{
			vector<double> q;
			REP(i, 0, z-1)
			{
				q.push_back(p[i]);
			}
			REP(i, 1, K-z)
			{
				q.push_back(p[N-i]);
			}
			
			double dp[201][201];
			REP(i, 1, K) dp[0][i] = 0;
			dp[0][0] = 1;
			REP(j, 1, K)
			{
				dp[j][0] = dp[j-1][0] * (1-q[j-1]);
				dp[j][j] = dp[j-1][j-1] * q[j-1];
				REP(i, 1, j-1)
				{
					dp[j][i] = dp[j-1][i] * (1-q[j-1]) + dp[j-1][i-1] * q[j-1];
				}
			}
			if(dp[K][K/2] > besttot) besttot = dp[K][K/2];
		}
		
		printf("%.12lf\n", besttot);
		/*
		REP(i, 0, N-1)
		{
			printf("%.2lf ", p[i]);
			if(whichz & (1 << i)) printf("(*) ");
		}
		printf("\n");
		*/
			
	}

  return 0;
}
