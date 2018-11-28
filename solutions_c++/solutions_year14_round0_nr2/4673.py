#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<vector>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<set>
#include<utility>
#include<algorithm>
#include<map>
#include<numeric>
#include<limits>
#include<iomanip>

using namespace std;

template <typename T, size_t N>
T* begin(T(&arr)[N]) { return &arr[0]; }
template <typename T, size_t N>
T* end(T(&arr)[N]) { return &arr[0]+N; }

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;

#define IFOR(i, a, b) for(int i = (a); i < (b); ++i)
#define EFOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define RESET(a, b) memset(a, b, sizeof(a))
#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair

int main(){
  int T;
  cin>>T;
  IFOR(t, 0, T){
    // get inputs
    float C,F,X;
    cin>>C>>F>>X;
    // solution
    cout.setf(ios::fixed,ios::floatfield);
    float ans = numeric_limits<float>::max();
    // fc = farmCount
    int fc=0;
    // 1/2 --> 1/2 + (1/2+ 1/(2+F)) --> 1/2 +(1/2+1/(2+F))+(1/2+1/(2+F)+1/(2+2F)) --> ...
    float calPart = 0;
    float totalPart=0;
    while(true){
      //cout<<"X"<<X<<"C"<<C<<"fc"<<fc<<"calPart"<<calPart<<"\n";
      float s = (X+C*fc+C*F*totalPart)/(2+fc*F);
      if(s<ans){
        ans=s;
      }else break;
      calPart += 1.0/(2+fc*F);
      totalPart += calPart;
      fc++;
    }
    // print answers
    printf("Case #%d: %.7f\n",t+1,ans);
  }


  return 0;
}
