#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

typedef long long ll;

int main() {
  int T, CNT = 1;
  cin >> T;
  while( T-- ) {
    cout << "Case #" << CNT++ << ": ";
    ll n;
    cin >> n;
    if( n == 0LL ) { puts("INSOMNIA"); continue; }
    set<char> S;
    ll i;
    ll prev = -1, cur = -1;
    for(i=1;(int)S.size()<10;++i) {
      ll v = n * i;
      cur = v;
      assert( prev < cur );
      prev = cur;
      stringstream ss;
      ss << v;
      string s;
      ss >> s;
      rep(j,(int)s.size()) {
        S.insert(s[j]);
      }
      assert(0LL<=v);
    }
    --i;
    cout << i * n << endl;
  }
  return 0;
}
