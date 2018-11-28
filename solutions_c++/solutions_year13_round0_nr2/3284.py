//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define N 100010
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
int		n,m,data[105][105];

bool	fail(int x,int y,int k){
	if ( k == 0 ) 
		Rep(i,n) {
			if ( data[i][y] > data[x][y] ) return false;
		}
	else{
		Rep(j,m) {
			if ( data[x][j] > data[x][y] ) return false;
		}
	}
	return true;
}
int		main(){
	int cas , tt = 0;
	scanf("%d", &cas );
	while ( cas -- ) {
		scanf("%d%d", &n, &m );
		Rep(i,n) Rep(j,m) scanf("%d", &data[i][j] );
		bool flag = true;
		Rep(i,n) Rep(j,m){
//			printf("%d\n",fail(i,j,0) | fail(i,j,1) );
			flag &= fail(i,j,0) | fail(i,j,1);
		}
		printf("Case #%d: %s\n", ++tt , flag?"YES":"NO" );
	}
	return 0;
}
