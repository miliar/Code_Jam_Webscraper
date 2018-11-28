#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <cassert>
#include <string>
#include <memory.h>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <cctype>
#include <iomanip>
#include <sstream>
#include <complex>
#include <cctype>
#include <fstream>
#include <cmath>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define ITER(c) __typeof((c).begin())
#define PB(e) push_back(e)
#define FOREACH(i, c) for(ITER(c) i = (c).begin(); i != (c).end(); ++i)
#define MP(a, b) make_pair(a, b)
#define PARITY(n) ((n) & 1)

typedef long long ll;
typedef complex<double> P;
typedef pair<P, P> L;
const int INF = 1000 * 1000 * 1000 + 7;
const double EPS = 1e-10;

double cross(const P &a, const P &b){
  return imag(conj(a) * b);
}
double dot(const P &a, const P & b){
  return real(conj(a) * b);
}

int ccw(const P a, P b, P c){
  b -= a;
  c -= a;
  if(cross(b, c) > 0) return 1;
  if(cross(b, c) < 0) return -1;
  if(dot(b, c) < 0) return 2;
  if(norm(b) < norm(c)) return -2;
  return 0;
}

bool intersectSS(const L &l1, const L &l2){
  return
    ccw(l2.first, l2.second, l1.first) *
    ccw(l2.first, l2.second, l1.second) <= 0 &&
    ccw(l1.first, l1.second, l2.first) *
    ccw(l1.first, l1.second, l2.second) <= 0;
}
             
string solve(){
  int N;
  cin >> N;             
  vector<P> ps(N);

  REP(i, N){
    cin >> ps[i].real() >> ps[i].imag();
  }
  

  int p[20];
  REP(i, N) p[i] = i;

  double ans = 0;
  vector<int> res;
  
  do{
    vector<P> tp;
    REP(i, N) tp.push_back(ps[p[i]]);

    bool valid = true;
    REP(i, N)REP(j, i){
if(tp[j] == tp[(i+1) % N] || tp[i] == tp[(j+1) % N] ||
   tp[j] == tp[i] || tp[(i+1) % N] == tp[(j+1) % N]) continue;      
      L l1(tp[i], tp[(i+1) % N]);
      L l2(tp[j], tp[(j+1) % N]);

      
      
      if(intersectSS(l1, l2)){
        valid = false;
        break;
      }
    }
    
    if(valid){

      double sum = 0;
      for(int i = 0; i < N - 2; i++){
        sum += cross(tp[i+1] - tp[0], tp[i+2] - tp[0]);
      }

      if(abs(sum) / 2 > ans){
        ans = abs(sum) / 2;
        res = vector<int>(p, p + N);
      }
    }
    
  }while(next_permutation(p + 1, p + N));

  ostringstream out;
  
  REP(i, res.size()){
    if(i > 0) out << " ";
    out << res[i];
  }
  return out.str();
}

int main(){
  int T;
  cin >> T;
  REP2(t, 1, T + 1){
    cout << "Case #" << t << ": " << solve() << endl;
  }
  return 0;
}
