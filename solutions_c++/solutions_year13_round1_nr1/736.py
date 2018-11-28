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

ll_t circle(ll_t r)
{
  return r * r;
}

ll_t area(ll_t r1 , ll_t r2)
{
  return circle(r2) - circle(r1);
}

ll_t solve()
{
  ll_t r,t;
  cin>>r>>t;
  ll_t ans = 0 ;
  while(1) {
    ll_t use = area(r, r+1);
    //cout<<" "<<r<<" "<<use<<endl;
    if(use <= t) {
      t -= use;
      ans++;
    }else break;
    r += 2;
  }
  return ans;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    long long ans = -1 ;
    
    ans = solve();

    printf("Case #%d: %lld\n" , case_no++ , ans);
  }
  return 0 ;
}
