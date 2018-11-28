#include <bits/stdc++.h>
using namespace std;

#define sc( x ) scanf( "%d" , &x )
#define REP( i , n ) for( int i = 0 ; i < n ; i++ )
#define FOR( it , A ) for( typeof A.begin() it = A.begin() ; it != A.end() ; it++ )
#define clr( t , val ) memset( t , val , sizeof(t) )

#define all(v)  v.begin() , v.end()
#define rall(v)  v.rbegin() , v.rend()
#define pb push_back

#define mp make_pair
#define fi first
#define se second

#define ones(x) __builtin_popcount(x)
#define test puts("************test************");
#define sync ios_base::sync_with_stdio(false);

#define N 10000000
#define MOD 1000000007
#define INF (1<<30)
#define EPS (1e-5)

typedef long long ll;
typedef double ld;

ld C , F , X;
void solve(){
	ld ans = 1e100 , S = 0;
	for( int it = 0 ; it <= N ; ++it ){
		if( it )S += C/(2.0 + (it-1)*F);
		ans = min( ans , S + X/(2.0 + it*F ) );
		//printf( "it : %d %.10f\n" , it , (double)(S + X/(2.0 + it*F )) );
	}
	printf( "%.10f\n" , (double)ans );
}
int main(){
	int cases;
	cin >> cases;
	REP( tc , cases ){
		cin >> C >> F >> X;
		cout << "Case #" << tc + 1 << ": ";
		solve();
	}
}


