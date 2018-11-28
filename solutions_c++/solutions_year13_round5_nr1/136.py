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
#include<cassert>
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

double estimate(vector<long long>& X , vector<long long>& bet){
  long long minVal = 1LL<<60;
  FOR(i,SZ(X)) minVal = min(minVal, X[i] + bet[i]);
  int num = 0 ;
  double price = 0 ;
  FOR(i,SZ(X)) {
    if(minVal == X[i] + bet[i]) {
      price += 36.0 * bet[i];
      num++;
    }
  }
  return price / num;
}

double solve()
{
  long long B,N;
  cin>>B>>N;
  vector<long long> X(N);
  FOR(i,N) cin>>X[i];
  X.resize(37,0);
  
  double ans = 0;
  long long originalB = B; 
  vector<long long> bet(37);

  while(B >= 0){
    int cur = 0 ;
    ans = max(ans, estimate(X, bet) + B - originalB);
    FOR(i,SZ(X)){
      if(X[cur] + bet[cur] > X[i] + bet[i]){
        cur = i ;
      }else if(X[cur] + bet[cur] == X[i] + bet[i]){
        if(bet[cur] > bet[i]){
          cur = i ;
        }
      }
    }
    bet[cur]++;
    B--;
    //FOR(i,SZ(bet)) cout<<" "<<bet[i]; cout<<endl;
  }

  return ans ;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    double ans = solve() ;
    printf("Case #%d: %.10f\n" , case_no++ , ans);
    
  }
  return 0 ;
}
