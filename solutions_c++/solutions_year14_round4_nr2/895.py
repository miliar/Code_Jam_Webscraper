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

#define MAX 100007

long N;
long A[MAX+7];

long invCount( vector<long> &seq )
{
    long i,j,c = 0;
    for( i=0;i<seq.size();i++ ){
        for( j=0;j<i;j++ ){
            if( seq[i] < seq[j] ) c++;
        }
    }
    return c;
}

bool isOk( vector<long> &v )
{
    long i;
    for( i=1;i<v.size();i++ ){
        if( v[i]<v[i-1] ) break;
    }
    for( i++;i<v.size();i++ ){
        if( v[i]>v[i-1] ) return false;
    }
    return true;
}


int main( void )
{
    long i,j,Icase,k = 0;

    //freopen("text1.txt","r",stdin );
    freopen("b.in","r",stdin );
    freopen("b.out","w",stdout );

    scanf("%ld",&Icase );
    while( Icase-- ){
        scanf("%ld",&N );
        vector<long> vc;
        for( i=0;i<N;i++ ){
            scanf("%ld",&A[i] );
            vc.pb( A[i] );
        }
        sort( ALL( vc ) );
        long ans = N*N;
        do{
            if( isOk( vc ) ){
                map<long,long> mp;
                for( i=0;i<vc.size();i++ ){
                    mp[vc[i]] = i;
                }
                vector<long> tmp;
                for( i=0;i<N;i++ ){
                    tmp.pb( mp[A[i]] );
                }
                ans = min( ans,invCount( tmp ) );
            }
        } while( next_permutation( ALL( vc ) ) );
        printf("Case #%ld: %ld\n",++k,ans );
    }

    return 0;
}
