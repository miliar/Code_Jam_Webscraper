// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////
// }}}

vector<LL> e;

long long ne = 39;
long long ee[39] = {1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL};

bool ispalindrome(long long x) {
  char c[20];
  sprintf(c,"%lld",x);
  int d = strlen(c);
  FOR(i,d) if(c[i] != c[d-i-1]) return false;
  return true;
}

void solve(){
  char a[105], b[105];
  scanf("%s %s\n",a,b);
  LL A,B,I;
  I = 100000000;
  I *= I;

  if(strlen(a) >= 16) A = I; else sscanf(a,"%lld",&A);
  if(strlen(b) >= 16) B = I; else sscanf(b,"%lld",&B);
  int ret=0;
  FOR(i,ne) if( (A <= ee[i]) && (ee[i] <=B)) ret++;
  printf("%d\n",ret);
}

int main(){
/*  
  FR(i,1,10000000) if(ispalindrome(i)) {
    long long x = i;
    x *= x;
    if(ispalindrome(x)) e.PB(x);
  }
  printf("%d\n",(int)e.SZ);
  FORSZ(i,e) printf(",%lldLL",e[i]);
*/
  int pvs; scanf("%d\n",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);
     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
