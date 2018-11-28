#pragma comment(linker, "/STACK:16777216")

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<assert.h>
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

#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define SZ(a) ((Long)a.size())
#define ALL(a) a.begin(),a.end()
#define FOREACH(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
#define AREA2(x1,y1,x2,y2,x3,y3) ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )
#define SQR(x) ((x)*(x))
#define STR string
#define IT iterator
#define ff first
#define ss second
#define MP make_pair
#define EPS 1e-9
#define INF 1000000007

#define chk(a,k) ((bool)(a&(1<<(k))))
#define set0(a,k) (a&(~(1<<(k))))
#define set1(a,k) (a|(1<<(k)))

typedef long long Long;
typedef vector<long> Vl;
typedef vector<Long> VL;
typedef pair<long,long> Pll;
typedef pair<Long,Long> PLL;
typedef long long Long;

#define MAX 21

long N,M;
string S[MAX+7];
vector<string> Set[MAX+7];
long ans1,ans2;

void Check( void )
{
    long i,j,k,tot = 0;
    for( i=1;i<=N;i++ ){
        vector<string> tmp;
        tot++;
        for( j=0;j<Set[i].size();j++ ){
            for( k=1;k<=Set[i][j].size();k++ ){
                tmp.pb( Set[i][j].substr( 0,k ) );
            }
        }
        sort( ALL( tmp ) );
        tot += tmp[0].size();
        for( j=1;j<tmp.size();j++ ){
            tot += tmp[j].size();
            for( k=0;k<tmp[j].size();k++ ){
                if( tmp[j][k]!=tmp[j-1][k] ) break;
                tot--;
            }
        }
    }
    if( tot == ans1 ) ans2++;
    else if( tot > ans1 ){
        ans1 = tot;
        ans2 = 1;
    }
}

void Find( long I )
{
    if( I>M ){
        long i;
        for( i=1;i<=N;i++ ){
            if( !Set[i].size() ) return;
        }
        Check();
        return;
    }
    long i;
    for( i=1;i<=N;i++ ){
        Set[i].pb( S[I] );
        Find( I+1 );
        Set[i].pop_back();
    }
}


int main( void )
{
    long i,j,Icase,k = 0;

    //freopen("text1.txt","r",stdin );
    freopen("d.in","r",stdin );
    freopen("d.out","w",stdout );

    scanf("%ld",&Icase );
    while( Icase-- ){
        cin>>M>>N;
        ans1 = 0;
        for( i=1;i<=M;i++ ){
            cin>>S[i];
        }
        Find( 1 );
        printf("Case #%ld: %ld %ld\n",++k,ans1,ans2 );
    }

    return 0;
}
