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

double memo[1<<20];

double dfs(int N, int b){
  if(b == (1<<N) - 1) return 0 ;
  double& ret = memo[b];
  if(!isnan(ret)) return ret;
  double val = 0;
  FOR(i,N){
    int pay = N;
    int cur = i;
    while((b & (1<<cur))) {
      cur = (cur + 1) % N;
      pay--;
    }
    val += pay + dfs(N, (b | (1<<cur)));
  }
  return ret = val / N;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    double ans = 0;
    string s;
    cin>>s;
    int b = 0;
    FOR(i,SZ(s)) if(s[i] == 'X') b |= (1<<i);
    memset(memo , -1 , sizeof(memo));
    ans = dfs(SZ(s), b);
    printf("Case #%d: %.10f\n" , case_no++ , ans);
    
  }
  return 0 ;
}
