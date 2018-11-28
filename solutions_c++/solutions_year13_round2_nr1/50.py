// compile with "g++ XXX.cc -mno-cygwin -O2" in Cygwin

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

long long solve()
{
  int A,N;
  cin>>A>>N;
  VI b(N);
  FOR(i,N) {
    cin>>b[i];
  }
  sort(ALL(b));
  long long ans = 1LL<<60;
  
  for(int sz = 0 ; sz <= N ; sz++) {
    long long removeNum = N - sz;
    long long addNum = 0 ;
    long long current = A;
    bool ng = false;
    FOR(i,sz) {
      if(current > b[i]){
        current += b[i];
      }else{
        if(current - 1 > 0){
          current += current - 1;
          addNum++;
          i--;
        }else{
          ng = true; break;
        }
      }
    }
    if(!ng) {
      ans = min(ans , removeNum + addNum);
    }
  }

  return ans;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    printf("Case #%d: %lld\n" , case_no++ , solve());
  }
  return 0 ;
}
