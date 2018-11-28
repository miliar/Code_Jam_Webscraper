#include <cstdio>
#include <iostream>
#include <cstring>
#include <set>
using namespace std;

multiset< int, greater<int> > s;

bool possibles(int time, int splits) {
  int eatingTime = time - splits;

  for (multiset< int, greater<int> >::iterator it = s.begin(); it != s.end(); ++it) {
    int cur = *it;

    int splitsNeeded;
    if (cur <= eatingTime) splitsNeeded = 0;
    else if (cur % eatingTime == 0) splitsNeeded = cur/eatingTime - 1;
    else splitsNeeded = cur/eatingTime;

    if (splitsNeeded > splits) {
      return false;
    }
    splits -= splitsNeeded;
  }

  return true;
}

bool possible(int time) {
  for (int i = 0; i < time; ++i) {
    if (possibles(time, i)) {
      return true;
    }
  }
  return false;
}

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int n;
    cin >> n;

    s.clear();
    while (n--) {
      int p;
      cin >> p;
      s.insert(p);
    }

    int maxImpossible = 0;
    int minPossible = *(s.begin());

    while (minPossible > maxImpossible + 1) {
      int c = (maxImpossible + minPossible) / 2;
      if (possible(c)) {
        minPossible = c;
      } else {
        maxImpossible = c;
      }
    }

    cout << "Case #" << tt << ": " << minPossible << endl;
  }
}
