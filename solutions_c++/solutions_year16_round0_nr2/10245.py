#pragma warning (disable: 4786)
#pragma comment (linker, "/STACK:26777216")
#include <bits/stdc++.h>

using namespace std;
typedef long long lint;
typedef unsigned long long ulint;
#define NN 12
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
int lenz = 0;
int org = 0;
char arr[ NN ];
int mem[ 1<<11 ];

void reset() {
    FOR(i,0,1<<lenz) {
        mem[ i ] = INF;
    }
}
void printz( int x ) {
   FOR(i, 0, lenz-1 ) {
        if(x&(1<<i) ) {
            printf("+ ");
        }else{
            printf("- ");
        }
    }
    printf("\n");
    printf("%d\n",mem[ x ]);
}
int f( int prev ) {
   int cur = prev, lbit = 0, rbit = 0;
   FOR( i, 0, lenz - 1 ) {
       int ith = 0, jth = i;
       cur = prev;
       while( ith <= jth ) {
           lbit = ( cur&(1<<ith) ) == 0 ? 0 : 1 ;  lbit = !lbit;
           rbit = ( cur&(1<<jth) ) == 0 ? 0 : 1 ;  rbit = !rbit;

           //printf("%d %d %d %d %d %d %d   ",cur, (1<<ith), (1<<jth),  lbit, rbit, ith, jth);

           if( lbit == 1 ){ cur |=( 1<< jth );  }else{ cur &= ~(1<<jth); }
           if( rbit == 1 ){ cur |=( 1<< ith );  }else{ cur &= ~(1<<ith); }

           //printf("-- %d %d %d %d %d %d %d   ",cur, cur & (1<<ith), cur & (1<<jth),  lbit, rbit, ith, jth);
           //printz( cur );
           ith++; jth--;
       }
       if( mem[ cur ] > mem[ prev ] + 1 ) {
           mem[ cur ] = mem[ prev ] + 1;
           //printz( cur );
           f( cur );
       }
   }
   //return mem[ ( 1<<lenz ) - 1 ];
}

int main() {
  freopen("B-small-attempt0.in","r",stdin);
  //freopen("b_small_out.txt","w",stdout);
  int cases; scanf("%d",&cases);
  getchar();
  int caseno = 0;
  while( cases-- ) {
    CLR(arr);
    gets(arr);
    lenz = strlen(arr);
    org = 0 ;
    FOR(i, 0, lenz-1) {
       if( arr[ i ] == '+' ) {
           org |= (1<<i);
       }
    }
    //printf("%d %d %d\n",org, (1<<lenz) - 1, lenz);
    //printz(org);
    int ret = 0;
    if( org == (1<<lenz) - 1 ) {
        ret = 0;
    } else if( org  == 0 ) {
        ret = 1;
    } else {
        reset();
        mem[ org ] = 0;
        f( org );
        ret = mem[ (1<<lenz) - 1 ];
    }


    printf("Case #%d: %d\n",++caseno,ret);

  }
  return 0;
}


