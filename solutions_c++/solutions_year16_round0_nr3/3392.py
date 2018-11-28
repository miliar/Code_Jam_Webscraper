#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(), (x).end()

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;

ll is_prime(ll n) {
  if(n == 1) return false;
  for(ll i = 2; i <= sqrt(n); ++i){
    if(n % i == 0) return i;
  }
  return 0;
}

ll convert(string s, int base) {
  ll res = 0;
  REP(i,s.length()) {
    res *= base;
    res += s[i] - '0';
  }
  return res;
}

int main(){
  int T, N, J;
  cin >> T >> N >> J;
  cout << "Case #1:" << endl;
  int cnt = 0;
  REP(i,1<<(N-2)){
    if(cnt == J) break;
    string s = "1";
    REP(j,N-2) {
      if(i & (1<<j)) s += "1";
      else s += "0";
    }
    s += "1";
    
    int a[9] = {0};
    bool f = true;
    REP(j,9){
      ll m = convert(s, j+2);
      ll dv = is_prime(m);
      if(dv == 0) {
        f = false;
        break;
      }
      a[j] = dv;
    }
    if(!f) continue;
    cout << s;
    REP(j,9) cout << " " << a[j];
    cout << endl;
    cnt++;
  }
  return 0;
}

