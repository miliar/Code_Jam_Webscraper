#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <numeric>

using namespace std;

map<int, int> MAP;

int main() {
  int nTC, tc = 0;
  cin >> nTC;
  while (++tc && nTC--) {
    int ctr = 0;
    int aw;
    MAP.clear();
    for (int k = 0; k < 2; k++) {
      int ans;
      cin >> ans;
      ans--;
      for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
          int x;
          cin >> x;
          if (i == ans) {
            MAP[x]++;
            if (MAP[x] == 2) {
              aw = x;
              ctr++;
            }
          }
        }
      }
    }
    cout << "Case #" << tc << ": ";
    if (ctr == 1) {
      cout << aw << endl;
    } else if (ctr == 0) {
      cout << "Volunteer cheated!" << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}

