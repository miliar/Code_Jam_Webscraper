#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cassert>

using namespace std;

const string G = "GABRIEL";
const string R = "RICHARD";

string doit() {
  int x, r, c;
  cin >> x >> r >> c;
  int mi = min(r, c);
  int ma = max(r, c);

  if (x == 1) return G;
  if (x == 2) {
    switch (mi) {
      case 1: return (ma % 2) == 0 ? G : R;
      case 2: return G;
      case 3: return ma == 3 ? R : G;
      case 4: return G;
    }
  }
  if (x == 3) {
    switch (mi) {
      case 1: return R;
      case 2: return ma == 3  ? G : R;
      case 3: return G;
      case 4: return R;
    }
  }
  if (x == 4) {
    switch (mi) {
      case 1: return R;
      case 2: return R;
      case 3: return ma == 4 ? G : R;
      case 4: return G;
    }
  }
  assert(false);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i)
    printf("Case #%d: %s\n", i, doit().c_str());
}
