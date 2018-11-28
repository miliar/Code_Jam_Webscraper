#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<P> Vp;
typedef map<int, Vi> MAP;

int N, D;
ll S0, As, Cs, Rs, M0, Am, Cm, Rm;
Mi net;
Vi par;
Vi S, M;
Vi reach;
int mini, maxi;

void update(int x) {
  // cerr << "update(" << x << ")" << endl;
  if (mini <= S[x] and S[x] <= maxi) {
    reach[x] = 1;
    for (int i = 0; i < int(net[x].size()); ++i) {
      int y = net[x][i];
      reach[x] += reach[y];
    }
  } else {
    reach[x] = 0;
  }
  if (x != 0) {
    update(par[x]);
  }
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> N >> D;
    cin >> S0 >> As >> Cs >> Rs;
    cin >> M0 >> Am >> Cm >> Rm;

    S = M = Vi(N);
    S[0] = S0;
    M[0] = M0;
    for (int i = 1; i < N; ++i) {
      S[i] = (S[i - 1]*As + Cs)%Rs;
      M[i] = (M[i - 1]*Am + Cm)%Rm;
    }

    // cerr << "A" << endl;

    net = Mi(N);
    par = Vi(N);
    par[0] = -1;
    for (int i = 1; i < N; ++i) {
      par[i] = M[i]%i;
      net[par[i]].push_back(i);
    }

    // cerr << "B" << endl;

    MAP sals_map;
    for (int i = 0; i < N; ++i) {
      sals_map[S[i]].push_back(i);
    }
    vector<pair<int, Vi> > sals(sals_map.begin(), sals_map.end());

    int res = 0;

    // cerr << "C" << endl;

    reach = Vi(N, 0);
    int j = -1;
    for (int i = 0; i < int(sals.size()); ++i) {
      // cerr << "i=" << i << " " << N << endl;
      mini = sals[i].first;
      maxi = mini + D;
      if (i != 0) {
        // cerr << "IF" << endl;
        for (int k = 0; k < int(sals[i - 1].second.size()); ++k) {
          update(sals[i - 1].second[k]);
        }
      }
      while (j + 1 < int(sals.size()) and sals[j + 1].first <= maxi) {
        // cerr << "WHILE j=" << j << endl;
        ++j;
        for (int k = 0; k < int(sals[j].second.size()); ++k) {
          // cerr << "UPDATE" << endl;
          update(sals[j].second[k]);
          // cerr << "END UPDATE" << endl;
        }
        // cerr << "END WHILE" << endl;
      }

      res = max(res, reach[0]);
    }

    cout << "Case #" << cas << ": " << res << endl;
  }
}
