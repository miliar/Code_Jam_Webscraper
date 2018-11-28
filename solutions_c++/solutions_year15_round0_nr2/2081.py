#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
#include<queue>
using namespace std;


#define inf 0x3f3f3f3f
#define eps 1e-9
#define mod 1000000007
#define FOR(i,s,t) for(int i = s; i < t; ++i )
#define REP(i,s,t) for( int i = s; i <= t; ++i )
#define LL long long
#define ULL unsigned long long
#define pii pair<int,int>
#define MP make_pair
#define lson id << 1 , l , m
#define rson id << 1 | 1 , m + 1 , r 
#define maxn ( 100000+100 )
#define maxe ( 200000+10 )
#define mxn 20000

int a[1010];
int main () {
	int T;
	freopen( "in.in", "r", stdin );
	freopen( "out.out", "w", stdout );
	scanf("%d", &T );
	int cas = 1;
	while( T-- ) {
		int n;
		scanf("%d", &n );
		int ans = 0;
		int ma = 0;
		for( int i = 0; i < n; ++i )
		{
			scanf("%d", &a[i] );
			ma = max( ma, a[i] );
		}
		ans = ma;
		for( int i = 1; i <= ma; ++i ) {
			int tmp = 0;
			for( int j = 0; j < n; ++j ) {
				tmp += a[j] / i - 1 + ( a[j] % i ? 1 : 0 );
			}
			ans = min( ans, tmp + i );
		}
		printf("Case #%d: %d\n", cas++,ans );
	}
}
