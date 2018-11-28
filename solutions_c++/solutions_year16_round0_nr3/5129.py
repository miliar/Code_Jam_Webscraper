#include <iostream>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;

typedef long long int ll;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    size_t N, J; cin >> N >> J;
    cout << "Case #" << t << ": \n";
    set<string> found;
    while (found.size() < J) {
      string S(N, '1');
      for (size_t i = 1; i+1 < N; ++i) {
        S[i] = '0'+rand()%2;
      }
      if (found.count(S)) continue;
      vector<ll> dd;
      for (int b = 2; b <= 10; ++b) {
        ll num = 0;
        for (size_t i = 0; i < N; ++i) {
          num *= b;
          num += S[i]-'0';
        }
        ll D = 0;
        for (ll d = 2; d*d <= num and not D; ++d)
          if (num%d == 0) D = d;
        if (D) dd.push_back(D);
        else break;
      }
      if (dd.size() == 9) {
        cout << S;
        for (int d : dd) cout << ' ' << d;
        cout << endl;
        found.insert(S);
      }
    }
  }
}