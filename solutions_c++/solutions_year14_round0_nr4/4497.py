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
// to use limit -> numeric_limits<type>::max()
// to set precision after decimal point -->  cout.setf(ios::fixed,ios::floatfield);
using namespace std;

template <typename T, size_t N>
T* begin(T(&arr)[N]) { return &arr[0]; }
template <typename T, size_t N>
T* end(T(&arr)[N]) { return &arr[0]+N; }

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<double> VD;

#define IFOR(i, a, b) for(int i = (a); i < (b); ++i)
#define DFOR(i, a, b) for(int i = (a)-1; i>=(b);--i)
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
    int N; cin>>N;
    VD naomi;
    VD ken;
    IFOR(i,0,N) { double tmp; cin>>tmp; naomi.PB(tmp);}
    IFOR(i,0,N) { double tmp; cin>>tmp; ken.PB(tmp);}
    sort(ALL(naomi));
    sort(ALL(ken));
    //IFOR(i,0,N) cout<<naomi[i]<<" "; cout<<endl;
    //IFOR(i,0,N) cout<<ken[i]<<" "; cout<< endl;
    // solution
    // war
    int n_point=0;
    {
      int n_in=0;
      IFOR(k_in,0,N){
        if(ken[k_in]>naomi[n_in]){
          n_in++; 
        }else{
          n_point++;
        }
      }
    }
    // deceitful war
    int n_point_dev=0;
    {
      int n_in=N-1;
      DFOR(k_in, N,0){
        if(naomi[n_in]>ken[k_in]){
          n_in--;
          n_point_dev++;
        }
      }
    }
    // print answers
    cout<< "Case #"<<t+1<<": "<<n_point_dev<<" "<<n_point <<"\n";
    
  }


  return 0;
}
