#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int ctoi(char c) {
  return c - '0';
}

bool canWin(int x, int r, int c) {
  if (x > c) {
    return false;
  } else if (r == 1 && x == 2 && c % 2 == 0) {
    return true;
  } else if (x >= 2*r) {
    return false;
  } else if ((r*c) % x != 0) {
    return false;
  }

  return true;
}

string solve(int x, int r, int c) {
  if (canWin(x, min(r, c), max(r, c))) {
    return "GABRIEL";
  } else {
    return "RICHARD";
  }
}


int main(int argc, char *argv[]) {
 
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    int x, r, c;
    cin >> x >> r >> c;
    cout << "Case #" << i << ": " << solve(x, r, c) << endl;
  }
}
