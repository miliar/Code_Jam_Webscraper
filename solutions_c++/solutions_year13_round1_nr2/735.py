#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <list>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <ctime>

using namespace std;

#define MAX 1001
#define INF 1000000
#define EPS 1e-7
#define PI acos(-1.0)
#define READ() freopen("Binput.txt", "r", stdin)
#define WRITE() freopen("Boutput.txt", "w", stdout)
#define CLR(x) memset( x, 0, sizeof(x) )
#define SET(x) memset( x, -1, sizeof(x) )
#define CHKBIT(x, i) ( ( ( x & ( 1 << i ) ) == 0 ) ? 0 : 1 )
#define SETBIT(x, i) ( x | ( 1 << i ) )
#define CLRBIT(x, i) ( x & (!( 1 << i )) )

int E, R, N;
int dp[100][100];
int v[100];

int f( int x, int e ){
	if( x >= N ){
		return 0;
	}
	if( dp[x][e] != -1 ) return dp[x][e];
	int ret = 0;
	for(int i=0; i<=e; i++){
		ret = max( ret, v[x] * i + f(x+1, min(e-i+R, E))  );
	}
	dp[x][e] = ret;
	return ret;
}

int main(){
	READ();
	WRITE();
	//ios_base::sync_with_stdio(false);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		scanf("%d %d %d", &E, &R, &N);
		for(int i=0; i<N; i++){
			scanf("%d", &v[i]);
		}
		SET(dp);
		printf("Case #%d: %d\n", t, f(0, E));
	}
	return 0;
}
