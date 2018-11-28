#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std ;

typedef long long LL ;

#define MP make_pair
#define PB push_back

const LL MOD  = 1000002013LL ;
const LL MAXN = 1009LL ;

bool vis[MAXN] ;
LL n, m , tot , ans ;

vector< pair<LL,LL> > st , ed ;

LL Function( LL x ){ return (!x ? 0 : ((2ll * n + 1 - x) * x / 2ll)%MOD) ; }

struct GX{
	LL x , y ;
	LL p ;
} A[MAXN] ;

bool _CK( LL m , LL l , LL r ) { return l <= m && m <= r ; }
bool CK(GX P , GX Q){
    return _CK(P.x , Q.x , Q.y) ||
           _CK(P.y , Q.x , Q.y) ||
           _CK(Q.x , P.x , P.y) || 
           _CK(Q.y , P.x , P.y) ;
}

void dfs( LL u ){
	vis[u] = 1 ;
	st.PB( MP(A[u].x , A[u].p) ) ;
	ed.PB( MP(A[u].y , A[u].p) ) ;
	for ( int i = 0 ; i < m ; i ++ )
		if ( !vis[i] )
			if ( CK(A[u] , A[i]) )
				dfs(i) ;
}

void Init() {
	ans = 0 ;
	tot = 0 ;
	cin >> n >> m ;
	for ( int i = 0 ; i < m ; i ++ ) {
		cin >> A[i].x >> A[i].y >> A[i].p ;
		
		ans += Function(A[i].y - A[i].x) * A[i].p ;
		ans = ((ans%MOD)+MOD)%MOD ;
	}
}

void Solve() {
	memset( vis , 0 , sizeof(vis) ) ;
	for ( int i = 0 ; i < m ; i ++ ) if ( !vis[i] ) {
		st.clear() ;
		ed.clear() ;
		dfs(i) ;
		sort(st.begin() , st.end()) ;
		sort(ed.begin() , ed.end()) ;
		int op = ed.size() - 1 ;
		for ( int j = st.size()-1 ; j >= 0 ; j -- ) {
			while ( op>0 && ed[op-1].first >= st[j].first ) op -- ;
			int k = op ;
			while ( st[j].second ) {
				LL t = min( st[j].second , ed[k].second ) ;
				
				ans -= Function( ed[k].first - st[j].first ) * t ;
				ans = ((ans%MOD)+MOD)%MOD ;
				
				ed[k++].second -= t, st[j].second -= t ;
			}
		}
	}
}

int main() {
	freopen("A.in","r",stdin) ;
	freopen("A.out","w",stdout) ;
	int Test ; cin >> Test ;
	for ( int _ = 1 ; _ <= Test ; _ ++ ) {
		Init() ;
		Solve() ;
		cout << "Case #" << _ << ": " << ans << "\n" ;
	}
}



