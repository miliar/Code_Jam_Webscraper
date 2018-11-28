#pragma comment(linker, "/STACK:256000000")
#include <stdio.h>
#include <iostream>
#include <cmath>
#include <math.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;



int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  std::ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) { 
    int D, standart_minut, special_minut, min_minut = 1009;
    cin >> D;
    vector<int> P(D);
    for (int i = 0; i < D; ++i) {
      cin >> P[i];
    }
    for (int standart_minut = 1 ; standart_minut < min_minut; ++standart_minut) {
      special_minut = 0;
      for (int i = 0; i < D; ++i) {
        special_minut += (P[i] - 1) / standart_minut;
      }
      min_minut = min( min_minut, special_minut + standart_minut);
    }

    cout << "Case #" << t << ": ";
    cout << min_minut << "\n";
  }
}
