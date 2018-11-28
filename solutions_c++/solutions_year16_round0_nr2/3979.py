#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(), (x).end()

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;

int main(){
  int T;
  cin >> T;
  REP(t,T){
    string s;
    cin >> s;
    int n = s.length();
    int res = 0;
    for(int i = n - 1; i >= 0; --i){
      if(s[i] == '+') continue;
      for(int j = 0; j <= i; ++j){
        if(s[j] == '+') s[j] = '-';
        else s[j] = '+';
      }
      res++;
    }
    cout << "Case #" << t + 1 << ": " << res << endl;
  }
  return 0;
}

