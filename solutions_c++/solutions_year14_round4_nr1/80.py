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

int main() {

  int t,caseNo=1;
  cin>>t;
  while(t--){
    int N, X;
    cin>>N>>X;
    VI S(N);
    FOR(i,N) cin>>S[i];
    sort(ALL(S));
    VI used(N);
    int ans = 0;
    for(int i=N-1;i>=0;i--) {
      if(used[i]) continue;
      used[i] = true;
      int t = -1;
      FOR(j,i) {
        if(S[i] + S[j] > X) break;
        if(!used[j]){
          t = j;
        }
      }
      if(t != -1) used[t] = true;
      ans++;
    }
    printf("Case #%d: %d\n", caseNo++, ans);
  }
  return 0 ;
}
