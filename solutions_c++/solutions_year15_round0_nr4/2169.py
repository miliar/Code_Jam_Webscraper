#pragma warning (disable: 4786)
#pragma comment (linker, "/STACK:26777216")
#include <bits/stdc++.h>

using namespace std;
typedef long long lint;
typedef unsigned long long ulint;
#define NN 10002
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
int X, R, C, caseno;

void yesz() {
    printf("Case #%d: GABRIEL\n",++caseno);
}
void noz() {
    printf("Case #%d: RICHARD\n",++caseno);
}
int main() {
  //freopen("d.in","r",stdin);
  //freopen("out.txt","w",stdout);
  int cases; scanf("%d",&cases);
  while( cases-- ) {
    scanf("%d %d %d",&X, &R, &C);
    if( X == 1 ) {
        yesz();
    } else {
        int maxz = max( R, C );
        int minz = min( R, C );
        //cout<<" "<<maxz<<" "<<minz<<"  "<<X<<" "<<X-1<<endl;
        //continue;
        if( ( maxz >= X) && ( minz >= X-1 ) && ( !(maxz%X) || !(minz%X ) ) ) {
            yesz();
        } else {
            noz();
        }
    }
  }
  return 0;
}
