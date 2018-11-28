#include <iostream>

using namespace std;

const char *solve(int x, int r, int c) {
  if (x == 1) return "GABRIEL";
  if (r < c) swap(r, c);
  if (x > r) return "RICHARD";
  if ((x - 1) > c) return "RICHARD";
  if ((r * c) % x) return "RICHARD";
  return "GABRIEL";
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    int x, r, c;
    cin >> x >> r >> c;

    cout << "Case #" << t << ": " << solve(x, r, c) << endl;
  }
}
