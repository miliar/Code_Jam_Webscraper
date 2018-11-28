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

double d[1000][1000];
bool visited[1000];
int N;

void dp(int x, double S)
{
	REP(y, 0, N-1)
	{
		if(!visited[y] && d[x][y] <= S)
		{
			visited[y] = true;
			dp(y, S);
		}
	}
}

int main()
{
	int TW;
	scanf("%d", &TW);
	
	REP(tw, 1, TW)
	{
		printf("Case #%d: ", tw);
		fprintf(stderr, "Case #%d.\n", tw);
		
		int V;
		int x[1000], y[1000], z[1000];
		scanf("%d %d", &N, &V);
		REP(i, 0, N-1)
		{
			scanf("%d %d %d", &x[i], &y[i], &z[i]);
			scanf("%*d %*d %*d");
		}
		REP(i, 0, N-1)
		{
			REP(j, 0, N-1)
			{
				d[i][j] = sqrt((double)(x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) + (z[i]-z[j])*(z[i]-z[j]));
			}
		}
		
		double down = 0, up = d[0][1];
		
		while(up-down > 0.000000001)
		{
			double middle = (down+up)/2;
			REP(i, 0, N-1) visited[i] = false;
			visited[0] = true;
			dp(0, middle);
			if(visited[1]) up = middle;
			else down = middle;
		}
		
		printf("%.9lf\n", up);
		
	}

  return 0;
}
