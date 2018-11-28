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
  int t,case_no=1;
  cin>>t;
  while(t--){
    int N;
    cin>>N;
    vector<double> naomi(N), ken(N);
    FOR(i,N) cin>>naomi[i];
    FOR(i,N) cin>>ken[i];
    int ans1=0,ans2=0;
    sort(ALL(naomi));
    sort(ALL(ken));
    {
      int p1 = 0, p2 = N-1;
      ans1 = 0;
      FOR(i,N) {
        if(naomi[i] > ken[p1]) {
          ans1++;
          p1++;
        }else {
          p2--;
        }
      }
    }
    {
      int cur = 0;
      ans2 = N;
      FOR(i,N) {
        while(cur < N && naomi[i] > ken[cur]) cur++;
        if(cur >= N) break;
        ans2--;
        cur++;
      }
    }
    printf("Case #%d: %d %d\n" , case_no++, ans1, ans2);
  }
  return 0 ;
}
