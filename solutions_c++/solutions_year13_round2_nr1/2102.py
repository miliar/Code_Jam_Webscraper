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
#define READ() freopen("Ainput.txt", "r", stdin)
#define WRITE() freopen("Aoutput.txt", "w", stdout)
#define CLR(x) memset( x, 0, sizeof(x) )
#define SET(x) memset( x, -1, sizeof(x) )
#define CHKBIT(x, i) ( ( ( x & ( 1 << i ) ) == 0 ) ? 0 : 1 )
#define SETBIT(x, i) ( x | ( 1 << i ) )
#define CLRBIT(x, i) ( x & (!( 1 << i )) )

int n;
int a[20];
int dp[20][10000];

int f(int pos, int val){
	//printf("%d %d\n", pos, val);
	if( pos >= n ) return 0;
	//printf("%d\n", a[pos]);
	if( dp[pos][val] != -1 ) return dp[pos][val];
	int ret = INT_MAX;
	ret = min( ret, 1 + f(pos+1, val) );
	//printf("#1 %d %d %d\n", pos, val, ret);
	if( a[pos] < val ){
		ret = min( ret, f(pos+1, val + a[pos]) );
		//printf("#2 %d %d %d\n", pos, val, ret);
	}
	else{
		int tval = val;
		for(int i=1; tval > 1 ; i++){
			tval += tval - 1;
			if( a[pos] < tval ){
				ret = min( ret, i + f(pos+1, tval + a[pos]) );
				break;
			}
		}
		//printf("#3 %d %d %d\n", pos, val, ret);
	}
	dp[pos][val] = ret;
	//printf("%d %d %d\n", pos, val, ret);
	return ret;
}

int main(){
	//ios_base::sync_with_stdio(false);
	READ();
	WRITE();
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		int x;
		scanf("%d %d", &x, &n);
		for(int i=0; i<n; i++) scanf("%d", &a[i]);
		sort(a, a+n);
		SET(dp);
		printf( "Case #%d: %d\n", t, f(0, x) );
	}
	return 0;
}
