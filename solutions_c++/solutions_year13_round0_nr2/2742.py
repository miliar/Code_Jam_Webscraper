#pragma comment(linker, "/STACK:16777216")

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<time.h>
#include<iostream>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<utility>
#include<algorithm>
#include<list>
using namespace std;

#define pb push_back
#define MS( a ) memset( a,0,sizeof(a))
#define MSV( a,v ) memset( a,v,sizeof(a))

typedef long long Long;

#define MAX 107

long N,M;
long Grid[MAX+7][MAX+7];
long Patt[MAX+7][MAX+7];

int main( void )
{
    long i,j,k,h,Icase,Kase = 0;;

    //freopen("text1.txt","r",stdin );
    freopen("B.in","r",stdin );
    freopen("B.out","w",stdout );

    scanf("%ld",&Icase );
    while( Icase-- ){
        scanf("%ld%ld",&N,&M );
        for( i=1;i<=N;i++ ){
            for( j=1;j<=M;j++ ){
                Grid[i][j] = 100;
                scanf(" %c",&Patt[i][j] );
            }
        }
        bool IsP = true;
        for( h=100;h>=1;h-- ){
            for( i=1;i<=N;i++ ){
                for( j=1;j<=M;j++ ){
                    if( Patt[i][j]!=h ) continue;
                    bool Can = true;
                    for( k=1;k<=N;k++ ) if( Patt[k][j]>h ) Can = false;
                    for( k=1;k<=N && Can;k++ ) Grid[k][j] = h;
                    Can = true;
                    for( k=1;k<=M;k++ ) if( Patt[i][k]>h ) Can = false;
                    for( k=1;k<=M && Can;k++ ) Grid[i][k] = h;
                    if( Grid[i][j]!=h ){
                        IsP = false;
                    }
                }
            }
        }
        printf("Case #%ld: ",++Kase );
        if( IsP ) printf("YES\n");
        else printf("NO\n");
    }

    return 0;
}
