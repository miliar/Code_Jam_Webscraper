#include <bits/stdc++.h>
#define MOD 1000000007
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define rf(i, x, y) for (int i = (x); i < (y); i++)
#define rfe(i, x, y) for (int i = (x); i <= (y); i++)
#define rb(i, x, y) for (int i = (x); i > (y); i--)
#define rbe(i, x, y) for (int i = (x); i >= (y); i--)
#define sfi(x) scanf("%d", &x)
#define pfi(x) printf("%d", x)
#define sfll(x) scanf("%lld", &x)
#define pfll(x) printf("%lld", x)
#define pfd(x) printf("%lf", x)
#define sfs(x) scanf("%s", x)
#define pfs(x) printf("%s", x)
#define eol printf("\n")
#define pb(x) push_back((x))

#define SIZE 1000005
typedef long long int ll;
using namespace std;

bool ten[10];

bool isTen(int no) {
   int tmp;
   while(no){
      tmp = no%10;
      ten[tmp]=true;
      no/=10;
   }
   rf(i,0,10) if( !ten[i] ) return false;
   return true;
}

void forNo(int c, int no) {
  int nno = no;
  if( no == 0 ) {
      printf("Case #%d: INSOMNIA\n", c);
  } else {
      rf(i,0,10) ten[i]=false;
      while( !isTen(nno) ) {
        nno+=no;
      }
      printf("Case #%d: %d\n", c, nno);
  }
}

int main() {
    int t,n;
    sfi(t);
    rfe(i,1,t){
        sfi(n);
        forNo(i,n);
    }
    return 0;
}
