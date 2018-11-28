#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<double, int> di;
typedef vector<di> vdi;

#define NAOMI 0
#define KEN 1

int main() {
  int T; cin >> T;
  for (int x = 1; x <= T; ++x) {
    int N; cin >> N;
    vdi v(2*N);
    for (int p = 0; p < 2; ++p) {
      for (int i = 0; i < N; ++i) {
        double x; cin >> x;
        v[i+N*p] = di(x, p);
      }
    }
    sort(v.begin(), v.end());
    int nl = 0, nw = 0, kl = 0, kw = 0;
    for(int i = 0; i < 2*N; ++i) {
      if (v[i].second == NAOMI) {
        ++nl;
        if (kl) {
          ++nw;
          --kl;
        }
      }
      else {
        ++kl;
        if (nl) {
          ++kw;
          --nl;
        }
      }
    }
    cout << "Case #" << x << ": " << nw << ' ' << N - kw << endl;
  }
}
