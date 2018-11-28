#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    set<double> naomi, ken;

    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
      double d;
      cin >> d;
      naomi.insert(d);
    }
    for (int i = 0; i < N; i++) {
      double d;
      cin >> d;
      ken.insert(d);
    }

    set<double> naomiWar = naomi;
    set<double> kenWar = ken;

    // play war
    int nPointsWar = 0;
    for (auto n = naomiWar.rbegin(); n != naomiWar.rend(); n++) {
      auto ken_block = kenWar.upper_bound(*n);
      if (ken_block == kenWar.end()) {
        nPointsWar++;
        kenWar.erase(kenWar.begin());
      } else {
        kenWar.erase(ken_block);
      }
    }

    int nPointsDeceit = 0;

    for (auto n = naomi.begin(); n != naomi.end(); n++) {
      if (*n > *(ken.begin())) {
        nPointsDeceit++;
        ken.erase(ken.begin());
      } else {
        auto highest = ken.end();
        highest--;
        ken.erase(highest);
      }
    }

    cout << "Case #" << t << ": ";

    cout << nPointsDeceit << " " << nPointsWar;

    cout << endl;
  }
}
