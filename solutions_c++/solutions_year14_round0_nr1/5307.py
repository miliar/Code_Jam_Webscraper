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
int A[4][4];
int B[4][4];

int main()
{
freopen("data.in","r",stdin);
freopen("data.out","w",stdout);
	int T;
	int s,t,cnt,num;
	SCF(T);
	FOR(cse,0,T){
		SCF(s);FOR(i,0,4)FOR(j,0,4)SCF(A[i][j]);
		SCF(t);FOR(i,0,4)FOR(j,0,4)SCF(B[i][j]);
		cnt=0;
		FOR(j,0,4)
			FOR(k,0,4)
			if(A[s-1][j]==B[t-1][k]){
				cnt++;
				num=A[s-1][j];
			}
		printf("Case #%d: ",cse+1);
		if(cnt==0)PRSF("Volunteer cheated!");
		else if(cnt>1)PRSF("Bad magician!");
		else PRFF(num);
	}
//	system("pause");
	return 0;
}
/*

*/
