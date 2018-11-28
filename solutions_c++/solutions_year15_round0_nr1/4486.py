#pragma warning (disable: 4786)
#pragma comment (linker, "/STACK:26777216")
#include <bits/stdc++.h>

using namespace std;
typedef long long lint;
typedef unsigned long long ulint;
#define NN 1012
#define MM 1000002
#define CLR( a ) memset( a , 0 , sizeof ( a ) )
#define negCLR( a ) memset( a , -1 , sizeof( a ) )
#define lld I64d
#define FOR(i,s,t) for(int i = (s); i <= (t); i++)
#define ROF(i,t,s) for(int i = (t); i >= (s); i--)

const lint MOD =  100000007;
const lint LINF = 1000000097999999903LL;
lint boundz = 10000000001LL;
const int INF = (1 << 29);
int N, M;
int T[ NN ];
char arr[ NN ];
int sMax, maxN;

void reset() {
    CLR( T ); CLR( arr );
}


void updateBIT( int idx, int val ) {
    int id = idx;
    while( id <= maxN ) {
        T[ id ] = (T[ id ] +  val);
        id += id & ( ~id + 1);
    }
}
int queryBIT( int id ) {
    int val = 0;
    while( id > 0 ) {
        val = (val + T[ id ]);
        id -= id & ( ~id + 1 );
    }
    return val;
}

int main() {
  //freopen("aa.in","r",stdin);
  //freopen("out.txt","w",stdout);
  int cases, caseno = 0; scanf("%d",&cases);
  while( cases-- ) {
       reset();

       scanf("%d",&sMax);
       //cout<<sMax<<endl;
       maxN = sMax + 4;
       scanf("%s", arr + 1);
       //puts( arr + 1 );
       FOR( i, 1, sMax + 1 ) {
           //printf(" %d",arr[ i ]-'0');  //single digit
           updateBIT( i, arr[ i ] - '0' );
       }

       //cout<<" input done "<<endl;

       arr[ sMax + 1 ] = '1'; //:p

       int req = 0, curReq = 0;
       FOR( i, 1, sMax + 1) {
           if( arr[ i ] - '0' == 0 ) continue;

            int id = i - 1;
            if( i == 1 ){ id++; }  // 0++ 1 , 1, 0

            curReq = queryBIT( id );
            if( curReq  < id ) {
                   curReq =  id -  curReq; //3-1 indexed  2 - 1 = req 1
                   //req = max( req, curReq );
                   //cout<<id<<" "<<curReq<<endl;
                   req += curReq;
                   updateBIT( 1, curReq); //always insert at 1 to get max audience
               }
       }



       printf("Case #%d: %d\n",++caseno,req);


  }
  return 0;
}
