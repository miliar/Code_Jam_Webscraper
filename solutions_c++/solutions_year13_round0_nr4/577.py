#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<list>
#include<string>
#include<cstring>
#include<cstdlib>
#include<set>
#include<map>
#include<vector>
using namespace std;

#define MAX 21
int test_case;
int N,K;
vector< int > ans;
vector< int > keys[ MAX ];
int table[ ( 1 << MAX ) ];
int keyCount[ 205 ];
int keyNeeded[ MAX ];
map< int , int > mp;

int dp( int mask, int keyState [] ) {
//	printf("%d\t", mask);
	int &ret = table[ mask ];
	if( ret != -1 ){ return ret; }
	if( mask == ( 1 << N ) - 1 ) {
		return ret = 1;
	}
	bool ok = false;
	for( int i = 0; i < N; i ++ ) {
		
		if( ( mask & ( 1 << i ) ) == 0 ) {
			if( keyState[ keyNeeded[ i ] ] > 0 ) {
	//			printf("%d %d\t", mask, i);
				int keyState2 [ 205 ];
				for( int k = 0; k < 205; k ++ ) keyState2[ k ] = keyState[ k ];
				keyState2[ keyNeeded[ i ] ] --;
				int sz = keys[ i ].size();
				for( int j = 0; j < sz; j ++ ) keyState2[ keys[ i ][ j ] ] ++;
				int nmask = ( mask | ( 1 << i ) );
				//printf("%d %d\t", mask, i);
				if( dp( nmask, keyState2 ) == 1 ) {
					ans.push_back( i );
					return ret = 1;
				}
			}
		}
	}

	return ret = 0;
	
}



int main(){
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("outputD.txt", "w", stdout);
	int i, n, k, a;
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		memset( keyCount, 0, sizeof( keyCount ) ) ;
		ans.clear();
		mp.clear();
		for( i = 0; i < N; i ++ ) keys[ i ].clear();
		scanf("%d %d", &K, &N);
		for( i = 0; i < K; i ++ ) {
			scanf("%d", &n);
			keyCount[ n ] ++ ;
		}
		for( i = 0; i < N; i ++ ) {
			scanf("%d %d", &n, &k);
			keyNeeded[ i ] = n;
			if( k > 0 ) {
				for( int j = 0; j < k; j ++ ) {
					scanf("%d", &a);
					keys[ i ].push_back( a );
				}
			}
		}
		
		memset( table, -1, sizeof( table ) ) ;
		int res = dp( 0, keyCount );
		if( res == 0 ) {
			printf("Case #%d: IMPOSSIBLE\n", caseId);
		} else {
			printf("Case #%d:", caseId);
			int sz = ans.size();
			for( int z = sz - 1; z >= 0; z -- ) printf(" %d", ans[ z ] + 1);
			printf("\n");
		}

	}
	return 0;
}