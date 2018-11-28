#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
#define SORT(x) sort(x.OP,x.ED)
#define SQ(x) ((x)*(x))
#define SSP system("pause")
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
typedef long long LL;
typedef pair<int, int> PII;
const double eps=1e-8;
const double INF=1e20;
const double PI=acos( -1. );
const int MXN = 50;
const LL MOD = 1000000007;
int dp[106][201][1001][2];
int G[111];
int H[111];
int n,P,Q;
int solve( int id,int hp,int r,int t) {
	if ( id>n )return 0;
	int &tp=dp[id][hp][r][t];
	if ( tp!=-1 )return tp;
	int i;
	if ( hp==H[id] ) {
		for ( i=r; i>=1; i-- ){
			int DA=P*i;
			if(hp>DA)cmax(tp,solve(id,hp-DA,r-i,t));
			else cmax(tp,solve(id+1,H[id+1],r-i,t)+G[id]);
		}
	}
	if ( t ) {
		if ( hp>Q )cmax( tp,solve( id,hp-Q,r,1-t ) );
		else cmax( tp,solve( id+1,H[id+1],r,1-t ) );
		return tp;
	}
	//i attack
	if ( hp>P )cmax( tp,solve( id,hp-P,r,1-t ) );
	else cmax( tp,solve( id+1,H[id+1],r,1-t )+G[id] );
	cmax( tp,solve( id,hp,r+1,1-t ) );
	if ( tp==-1 )tp=0;
	return tp;
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i;
	int T;
	scanf( "%d",&T );
	for ( int CASE=1; CASE<=T; ++CASE ) {
		memset( dp,-1,sizeof dp );
		scanf( "%d%d%d",&P,&Q,&n );
		for ( i=1; i<=n; i++ )scanf( "%d%d",&H[i],&G[i] );
		printf( "Case #%d: %d\n",CASE,solve( 1,H[1],0,0 ) );
	}
	return 0;
}
/*
1
20 21 4
190 633318
195 475266
193 245481
195 50570
*/
