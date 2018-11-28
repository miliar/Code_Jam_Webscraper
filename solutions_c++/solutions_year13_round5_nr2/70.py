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

typedef complex<int> xy_t;
template<typename T> T dot(const complex<T>& p, const complex<T>& q){ return real(conj(p)*q); } 
template<typename T> T det(const complex<T>& p, const complex<T>& q){ return imag(conj(p)*q); }

template<typename T> 
bool intersect(complex<T> p1, complex<T> p2, complex<T> p3, complex<T> p4) 
{ 
  return (ccw(p1, p2, p3) * ccw(p1, p2, p4)) <= 0 && 
         (ccw(p3, p4, p1) * ccw(p3, p4, p2)) <= 0; 
}

template<typename T> 
int ccw(complex<T> p1, complex<T> p2, complex<T> p3)
{
  p2-=p1; p3-=p1;
  if(det(p2, p3) > 0) return +1; //
  if(det(p2, p3) < 0) return -1; //
  if(p2.real() * p3.real() < 0 ||
  p2.imag() * p3.imag() < 0) return +2; // p2-p1-p3, on line
  if(norm(p2) < norm(p3)) return -2; // p1-p2-p3, on line
  return 0;
}

typedef vector<xy_t> polygon; 

double area(polygon p){
  double val = 0;
  FOR(i,SZ(p)){
    int i2 = (i+1)%SZ(p);
    val += det(p[i],p[i2]);
  }
  return fabs(val)/2;
}

VI solve(){
  int N;
  cin>>N;
  vector<xy_t> dat(N);
  FOR(i,N){
    int x,y; cin>>x>>y; dat[i] = xy_t(x,y);
  }
  VI perm(N);
  FOR(i,N) perm[i] = i ;
  VI ans ;
  double maxArea = -1;
  do{
    vector<xy_t> poly(N);
    FOR(i,N) poly[i] = dat[perm[i]];
    double a = area(poly);
    if(maxArea < a){
      bool ok = true;
      FOR(i,N) if(ok) FOR(j,i) {
        int i2 = (i+1)%N;
        int j2 = (j+1)%N;
        if(i == j || i == j2) continue;
        if(i2 == j || i2 == j2) continue;
        if(intersect(poly[i],poly[i2],poly[j],poly[j2])){
          ok = false; 
          break;
        }
      }
      if(ok){
        maxArea = a;
        ans = perm;
      }
    }
  }while(next_permutation(perm.begin() + 1, perm.end()));
  return ans;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    VI ans = solve();
    printf("Case #%d:" , case_no++);
    FOR(i,SZ(ans)) printf(" %d", ans[i]); puts("");
  }
  return 0 ;
}
