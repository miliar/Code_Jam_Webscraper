#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

int main() {
  int ncases;
  cin >> ncases;

  int g, r1, r2;
  map<int, int> guesses;
  for (int caseno = 1; caseno <= ncases; caseno++) {
    guesses.clear();
    cin >> r1;
    for (int i = 1; i <= 4; i++)
      for (int j = 1; j <= 4; j++) {
        cin >> g;
        if (i == r1) {
          guesses[g]++;
        }
      }
    cin >> r2;
    for (int i = 1; i <= 4; i++)
      for (int j = 1; j <= 4; j++) {
        cin >> g;
        if (i == r2) {
          guesses[g]++;
        }
      }

    bool bad = false;
    int ans = -1;
    for (map<int, int>::iterator it = guesses.begin(); it != guesses.end(); ++it) {
      if (it->second > 1) {
        if (ans == -1) {
          ans = it->first;
        } else {
          bad = true;
        }
      }
    }

    printf("Case #%i: ", caseno);
    if (ans == -1) {
      printf("Volunteer cheated!\n");
    } else if (bad) {
      printf("Bad magician!\n");
    } else {
      printf("%i\n", ans);
    }
  }
}
