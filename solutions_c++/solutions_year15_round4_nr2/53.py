#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
//#include <set>
//#include <map>
#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int main()
{
  int tcase = 0;
  ifstream fin("z.in");
  ofstream fout("z.out");
  fin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    // temp, rate
    vector<pair<ld, ld> > hot, cold;
    ld rate = 0;
    int n;
    ld V, T;
    fin >> n >> V >> T;
    ld extraRate = 0;
    ld diff = 0;
    for (int i = 0; i < n; i++) {
      ld r, t;
      fin >> r >> t;
      if (t == T) {
        rate += r;
      } else if (t < T) {
        cold.push_back(make_pair(T - t, r));
        extraRate += r;
        diff += (t-T)*r;
      } else {
        hot.push_back(make_pair(t - T, r));
        extraRate += r;
        diff += (t-T)*r;
      }
    }
    if (rate == 0 && (hot.empty() || cold.empty())) {
      fout << "Case #" << tind << ": IMPOSSIBLE" << endl;
      continue;
    }
    if (!hot.empty() && !cold.empty()) {
      if (diff < 0) {
        diff = -diff;
        swap(hot, cold);
      }
      sort(hot.begin(), hot.end());
      for (int i = hot.size() - 1; i >= 0; i--) {
        if (hot[i].first * hot[i].second >= diff) {
          extraRate -= diff / hot[i].first;
          break;
        }
        diff -= hot[i].first * hot[i].second;
        extraRate -= hot[i].second;
      }
      if (extraRate > 0) rate += extraRate;
      else cerr << "extraRate = " << extraRate << endl;
    }
    fout << "Case #" << tind << ": " << setprecision(15) << V / rate << endl;
  }
  return 0;
}
