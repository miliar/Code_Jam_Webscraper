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

int g1[4][4];
int g2[4][4];

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int r1,r2;
    cin>>r1;
    FOR(i,4) FOR(j,4) cin>>g1[i][j];
    cin>>r2;
    FOR(i,4) FOR(j,4) cin>>g2[i][j];
    r1--; r2--;
    VI ans1, ans2;
    FOR(i,4) {
      ans1.push_back(g1[r1][i]);
      ans2.push_back(g2[r2][i]);
    }

    //FOR(i,4) cout<<" "<<ans1[i]; cout<<endl;
    //FOR(i,4) cout<<" "<<ans2[i]; cout<<endl;
    sort(ALL(ans1));
    sort(ALL(ans2));
    VI ans;
    set_intersection(ALL(ans1), ALL(ans2), back_inserter(ans));

    if(SZ(ans) == 1){
      printf("Case #%d: %d\n" , case_no++ , ans[0]);
    }else if(SZ(ans) == 0){
      printf("Case #%d: Volunteer cheated!\n" , case_no++);
    }else {
      printf("Case #%d: Bad magician!\n" , case_no++);
    }
    
  }
  return 0 ;
}
