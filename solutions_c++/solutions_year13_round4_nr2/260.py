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

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int N;
    long long P;
    cin>>N>>P;
    long long largestGuaranteed = 0;
    long long largestCould = 0;

    // for small
    long long lower = 0 , upper = (1LL<<N);
    while(lower < upper - 1){
      long long i = (lower + upper) / 2;
      long long bestplace = 0;

      long long weaker = (1LL<<N)-i;
      int t = 0;
      while(weaker > 0){
        t++;
        weaker /= 2;
      }
      t--;
      bestplace = (1LL<<(N-t)) ;
      //cout<<i<<" "<<t<<" "<<bestplace<<endl;
      if(bestplace<=P){
        largestCould = max(largestCould, 0LL+i);
        lower = i;
      }else{
        upper = i;
      }
    }
    lower = 0 ; upper = (1LL<<N);
    while(lower < upper - 1){
      long long i = (lower + upper) / 2;    
      long long worstplace = 0;

      long long stronger = i + 1;
      int t = 0;
      while(stronger > 0){
        t++;
        stronger /= 2;
      }
      t--;

      worstplace = ((1LL<<(N-t))-1) ;
      worstplace = (1LL<<N) - worstplace;
      //cout<<i<<" "<<t<<" "<<worstplace<<endl;
      if(worstplace<=P){
        largestGuaranteed = max(largestGuaranteed, 0LL+i);
        lower = i;
      }else{
        upper = i;
      }
    }

    printf("Case #%d: %lld %lld\n" , case_no++ , largestGuaranteed, largestCould);
    
  }
  return 0 ;
}
