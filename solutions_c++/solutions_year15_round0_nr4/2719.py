#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <deque>
#include <sstream>
#include <utility>
#include <functional>
#include <numeric>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;
  for (int at = 1; at <= tt; at++) {
    int x, r, c;
    cin >> x >> r >> c;
    bool ok = true;
    if (x == 2) {
      if (r == 1 && (c == 1 || c == 3)) ok = false;
      if (r == 3 && (c == 1 || c == 3)) ok = false;
    }
    if (x == 3) {
      if (r == 1) ok = false;
      if (r == 2 && (c == 1 || c == 2 || c == 4)) ok = false;
      if (r == 3 && c == 1) ok = false;
      if (r == 4 && (c == 1 || c == 2 || c == 4)) ok = false;
    }
    if (x == 4) {
      if (r == 1) ok = false;
      if (r == 2) ok = false;
      if (r == 3 && (c == 1 || c == 2 || c == 3)) ok = false;
      if (r == 4 && (c == 1 || c == 2)) ok = false;
    }
    cout << "Case #" << at << ": " << (ok ? "GABRIEL\n" : "RICHARD\n");
  }
  return 0;
}