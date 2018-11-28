#include <gmpxx.h>
//#include <gtk/gtk.h>
//#include <cairo.h>

#include "shelly.hpp"

using namespace std;
using namespace shelly;

int main(int argc, char **argv) {
  freopen("input.txt", "r", stdin);
//  gtk_init(&argc, &argv);
  int T;
  cin >> T;
  for (int TT = 1; TT <= T; TT++) {
    int N, X;
    cin >> N >> X;
    vector<int> all;
    for (int i = 0; i < N; i++) {
      int t;
      cin >> t;
      all.push_back(t);
    }
    Sort(all);
    int res = 0;
    while (all.size()) {
      int f = all.front();
      all.erase(all.begin());
      res++;
      long long k = -1;
      for (long long i = all.size() - 1; i >= 0; i--) {
        if (all[i] + f <= X) {
          k = i;
          break;
        }
      }
      if (k != -1) {
        all.erase(all.begin() + k);
      }
    }
    cout << Format("Case #%0: %1", TT, res) << endl;
  }
  return 0;
}
