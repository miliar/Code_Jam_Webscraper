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
  REP(t,T) {
    int N;
    cin >> N;
    if(N == 0) {
      cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
      continue;
    }

    int a[10] = {0};
    ll y = 0;
    while(1){
      bool f = true;
      REP(i,10) if(!a[i]) f = false;
      if(f) break;
      y++;
      string tmp = to_string(N * y);
      REP(i,tmp.length()) a[tmp[i]-'0'] = 1;
    }
    ll res = y * N;
    cout << "Case #" << t + 1 << ": " << res << endl;
  }
  return 0;
}

