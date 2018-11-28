#include <bits/stdc++.h>
using namespace std;

const int INF = 1<<28;
const int MAXP = 1001;
int ans;
multiset<int> P;

void rec(int w = 0) {
  const int b = *P.rbegin();
  if(w + (b+1)/2 + 1 >= ans) return;
  ans = min(ans, w + b);
  for(int a = 1; a < b; ++a) {
    if(!P.count(a)) continue;
    for(int k = 1; k <= (a+b)/2; ++k) {
      P.erase(P.lower_bound(a));
      P.erase(P.lower_bound(b));
      P.insert(k);
      P.insert((a+b)-k);
      rec(w + 1);
      P.erase(P.lower_bound(k));
      P.erase(P.lower_bound((a+b)-k));
      P.insert(a);
      P.insert(b);
    }
  }
  for(int k = 1; k <= b/2; ++k) {
    P.erase(P.lower_bound(b));
    P.insert(k);
    P.insert(b-k);
    rec(w + 1);
    P.erase(P.lower_bound(k));
    P.erase(P.lower_bound(b-k));
    P.insert(b);
  }
}

int main() {
  int T; cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    cout << "Case #" << tc << ": ";
    int D; cin >> D;
    P.clear();
    for(int i = 0; i < D; ++i) {
      int p; cin >> p;
      P.insert(p);
    }
    ans = *P.rbegin();
    rec();
    cout << ans << endl;
  }
  return 0;
}

