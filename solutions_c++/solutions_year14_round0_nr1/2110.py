#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXK = 20;
const int R = 4;

int used[MAXK];

void solve(int t) {
  int r;
  cin >> r;
  --r;
  memset(used, 0, sizeof used);

  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < R; ++j) {
      int temp;
      cin >> temp;
      if (i == r) {
        used[temp] = 1;
      }
    }
  }

  cin >> r;
  --r;
  bool found = false;
  bool rep = false;
  int best = -1;

  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < R; ++j) {
      int temp;
      cin >> temp;
      if (i == r) {
        if (used[temp]) {
          if (found) {
            rep = true;
          } else {
            found = true;
            best = temp;
          }
        }
      }
    }
  }

  cout << "Case #" << t << ": ";
  if (!found) {
    cout << "Volunteer cheated!\n";
  } else if (rep) {
    cout << "Bad magician!\n";
  } else {
    cout << best << "\n";
  }
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
      solve(t);
    }
    return 0;
}
