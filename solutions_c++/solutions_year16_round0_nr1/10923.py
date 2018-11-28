#include    <bits/stdc++.h>
#define     REP(i,a,b)  for(int i=(a);i<(b);i++)
#define     CLR(m,x)    memset(m,x,sizeof(m))
#define     __nCASE     int _(1),__;for(scanf("%d",&__);_<=__;_++)
#define     SYNC        ios::sync_with_stdio(0)
using namespace std;
typedef double DB;
typedef long long LL;
/********************************************************/
const int lmt = 1e6;
const int maxN = lmt + 10;
bool v[10];
int an[maxN];
void calc(int x){
      while( x ){
            v[x%10] = 1;
            x /= 10;
      }
}
bool check(){
      for(int i = 0; i <= 9; i++) if( !v[i] ) return false;
      return true;
}
int main()
{
      #ifdef LOCAL
            freopen("A-large.in","r",stdin);
            freopen("output.txt", "w", stdout);
      #endif

      for(int i = 1; i <= lmt; i++){
            memset( v, 0, sizeof(v) );
            int m;
            for(int j = 1; ; j++){
                  int t = i * j;
                  calc( t );
                  if( check() ) {
                        m = j;
                        break;
                  }
            }
            an[i] = m * i;
      }

      __nCASE
      {
            printf("Case #%d: ", _);

            int n;
            scanf("%d", &n);

            if( !n )
                  printf("INSOMNIA\n");
            else
                  printf("%d\n", an[n]);
      }

      return 0;
}
