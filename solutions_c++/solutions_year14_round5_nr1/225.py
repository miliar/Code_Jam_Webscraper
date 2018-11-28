#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>
#include<bitset>
#include<cassert>

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define FOR3(i,a,b) for(int i=a,i##_end=b;i<i##_end;i++)
#define FOR_EACH(it,v) for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI; 
typedef vector<VI> VVI;
typedef complex<int> xy_t;

template<typename T> void debug(T v , string delimiter = "\n")
{ for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++) cout << *it << delimiter; cout << flush ;}

int dx[]  = {0,1,0,-1};
int dy[]  = {1,0,-1,0};
string ds = "SENW";

const double PI = 4.0*atan(1.0);

long long sum[1111111];

int main() {

  int t,caseNo=1;
  cin>>t;

  while(t--){
    int N,p,q,r,s;
    cin>>N>>p>>q>>r>>s;
    VI a(N);
    FOR(i,N) a[i] = (1LL * i * p + q) % r + s;
    sum[0] = 0;
    FOR(i,N) sum[i+1] = sum[i] + a[i];
    
    ll_t lower = 0, upper = sum[N] + 10;
    ll_t ans = -1;
    while(lower <= upper){
      ll_t p = (lower + upper) / 2;
      int cur = 0 ;
      FOR(_,3){
        long long s = 0 ;
        while(cur < N && s + a[cur] <= p){
          s += a[cur++];
        }
      }
      if(cur == N){
        upper = p - 1;
        ans = p ;
      }else {
        lower = p + 1;
      }
    }

    printf("Case #%d: %.12f\n", caseNo++, 1 - 1.0 * ans / sum[N]);
    
  }
  return 0 ;
}
