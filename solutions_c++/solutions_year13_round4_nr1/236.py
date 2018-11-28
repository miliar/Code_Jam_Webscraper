#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef long long int LL;

const int MOD = 1000002013;

LL ticketCost(LL n, LL p, LL d) {
  LL ret = ((d*n) - (d*(d-1)/2)) % MOD;
  ret = ret * (p % MOD); ret %= MOD;
  return ret;
  }

int main() {
  int nc; cin >> nc;
  for (int curC = 1; curC <= nc; ++curC) {
    int n, m; cin >> n >> m;

    vector<int> stops;
    map<int, LL> embark, debark;

    LL price = 0;
    while (m--) {
      int o, e, p; cin >> o >> e >> p;
      stops.push_back(o); stops.push_back(e);
      embark[o] += p;
      debark[e] += p;

      price = (price + ticketCost(n, p, e-o)) % MOD;
      }

    sort(stops.begin(), stops.end());
    int ns = unique(stops.begin(), stops.end()) - stops.begin();

    LL paid = 0;
    map<int, LL> onBoard;
    for (int i = 0; i < ns; ++i) {
      if (embark.count(stops[i]))
        onBoard[stops[i]] += embark[stops[i]];
      if (debark.count(stops[i])) {
        LL p = debark[stops[i]];
        while (p) {
          map<int, LL>::iterator z = --onBoard.end();
          LL k = min(z->second, p);
          paid = (paid + ticketCost(n, k, stops[i] - z->first)) % MOD;
          p -= k;
          z->second -= k;
          if (!z->second) onBoard.erase(z);
          }
        }
      }

    LL loss = (price - paid) % MOD;
    if (loss < 0) loss += MOD;

    cout << "Case #" << curC << ": " << loss << '\n';
    }
  }

