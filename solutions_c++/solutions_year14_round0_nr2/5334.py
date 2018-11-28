#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>

using namespace std;
#define FOR( i, a, b )	for ( int i = a; i < b; i++ )
#define FORU( i, a, b ) for ( Uint i = a; i < b; i++ )
#define FORD( i, a, b ) for ( int i = a; i > b; i-- )
#define MST( a, num )	memset( a, num, sizeof(a) )
#define MCP( d, s )	memcpy( d, s, sizeof(s) )
#define SCP( d, s )	strcpy( d, s)
#define WH( n )		while ( scanf( "%d", &n ) != EOF )
#define WHZ( n )	while ( scanf( "%d", &n ) != EOF && n != 0 )
#define SCF( a )	scanf( "%d", &a )
#define SCFL( a )	scanf( "%lld", &a )
#define SCFS( a )	scanf( "%s", a )
#define PRF( a )	printf( "%d", a )
#define PRS( a )	printf( "%s", a )
#define PRFF( a )	printf( "%d\n", a )
#define PRSF( a )	printf( "%s\n", a )
#define PRFFU( a )	printf( "%I64d\n", a )
#define PRFFL( a )	printf( "%lld\n", a )
#define min2( a, b )	( (a < b) ? a : b)
#define max2( a, b )	( (a > b) ? a : b)
#define SCF2( a, b )	scanf( "%d%d", &a, &b)
#define SCF3( a, b, c)	scanf( "%d%d%d", &a, &b, &c)
#define MOD 1000000007
typedef long long int Uint;
#define N 105
#define eps 1e-8
bool eq(double x,double y){
return fabs(x-y)<eps;
}
double solve(double C,double F,double X){
if(X<C || eq(X,C))return X/2.0;
double po = X/C-2/F-2;
if(po<-1.0 || eq(po,-1.0))return X/2.0;
int k = (int)(po + 1.0);
double cnt = 0;
double st = 2.0;
	FOR(i,0,k+1){
		cnt += C/st;
		st += F;
	}
	cnt+=X/st;
return cnt;
}
int main()
{
freopen("data.in","r",stdin);
freopen("data.out","w",stdout);
	int T;
	double C,F,X;
	SCF(T);
	FOR(cse,0,T){
		scanf( "%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: ",cse+1);
		printf("%.7f\n",solve(C,F,X));
	}
	//system("pause");
	return 0;
}
/*

*/
