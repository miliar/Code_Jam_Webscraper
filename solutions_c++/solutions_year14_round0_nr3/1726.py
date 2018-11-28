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
#define N 55
int mat[N][N];
int getMatrix(int R,int C,int M){
//R<C, M is blank
MST(mat,0);
if(M<=1){
	if(M)mat[0][0]='c';
	return 1;
}
if(R==1)
	FOR(j,0,M)mat[0][j]='.';
else if(R==2)
	if(M&0x01)return 0;
	else if(M<=2)return 0;
	else FOR(i,0,2)FOR(j,0,M/2)mat[i][j]='.';
else if(R==3)
	if(M%3==0)
		if(M<=3)return 0;
		else FOR(i,0,3)FOR(j,0,M/3)mat[i][j]='.';
	else if(M%3==2)
		if(M<=5)return 0;
		else{
			FOR(i,0,3)FOR(j,0,M/3)mat[i][j]='.';
			FOR(i,0,2)mat[i][M/3]='.';
		}
	else//%3 1
		if(M==7)return 0;
		else{
			FOR(i,0,3)FOR(j,0,M/3-1)mat[i][j]='.';
			FOR(i,0,2)FOR(j,M/3-1,M/3+1)mat[i][j]='.';
		}
else if(R==4){
if(M%4==0)
	if(M==4)return getMatrix(2,C,M);
	else FOR(i,0,4)FOR(j,0,M/4)mat[i][j]='.';
else if(M%4==1)
	if(M==5)return 0;
	else if(M==9) return getMatrix(3,C,M);
	else{
			FOR(i,0,4)FOR(j,0,M/4-1)mat[i][j]='.';
			FOR(i,0,3)mat[i][M/4-1] = '.';
			FOR(i,0,2)mat[i][M/4] = '.';
	}
else if(M%4==2)
	if(M==2)return 0;
	else if(M==6)return getMatrix(3,C,M);
	else{
			FOR(i,0,4)FOR(j,0,M/4)mat[i][j]='.';
			FOR(i,0,2)mat[i][M/4] = '.';
	}
else//% 3
	if(M==3||M==7)return 0;
	else{
			FOR(i,0,4)FOR(j,0,M/4)mat[i][j]='.';
			FOR(i,0,3)mat[i][M/4] = '.';
	}
}
else if(R==5){
if(M%5==0)
	if(M==5)return 0;
	else FOR(i,0,5)FOR(j,0,M/5)mat[i][j]='.';
else if(M%5==1)
	if(M==6)return getMatrix(3,C,M);
	else if(M==11)return getMatrix(3,C,M);
	else{
			FOR(i,0,5)FOR(j,0,M/5-1)mat[i][j]='.';
			FOR(i,0,4)mat[i][M/5-1]='.';
			FOR(i,0,2)mat[i][M/5] = '.';
	}
else if(M%5==2)
	if(M==2)return 0;
	else if(M==7)return 0;
	else{
			FOR(i,0,5)FOR(j,0,M/5)mat[i][j]='.';
			FOR(i,0,2)mat[i][M/5]='.';
	}
else if(M%5==3)
	if(M==3)return 0;
	else if(M==8)return getMatrix(4,C,M);
	else{
			FOR(i,0,5)FOR(j,0,M/5)mat[i][j]='.';
			FOR(i,0,3)mat[i][M/5]='.';
	}
else//%5 = 4
	if(M==4)return getMatrix(2,C,M);
	else if(M==9)return getMatrix(3,C,M);
	else{
			FOR(i,0,5)FOR(j,0,M/5)mat[i][j]='.';
			FOR(i,0,4)mat[i][M/5]='.';
	}

}
mat[0][0]='c';
return 1;
}
void print(int R,int C){
if(R<=C)
FOR(i,0,R){
	FOR(j,0,C)
		if(!mat[i][j])printf("*");
		else printf("%c",mat[i][j]);
	printf("\n");
}
else
FOR(j,0,R){
	FOR(i,0,C)
		if(!mat[i][j])printf("*");
		else printf("%c",mat[i][j]);
	printf("\n");
}

}
int main()
{
freopen("data.in","r",stdin);
freopen("data.out","w",stdout);
	int T;
	int R,C,M;
	SCF(T);
	FOR(cse,0,T){
		SCF3(R,C,M);
		printf("Case #%d:\n",cse+1);
		if(!getMatrix(min2(R,C),max2(R,C),R*C-M))
			printf("Impossible\n");
		else
			print(R,C);
	}
//	system("pause");
	return 0;
}
/*

*/
