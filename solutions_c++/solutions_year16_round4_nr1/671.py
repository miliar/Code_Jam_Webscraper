#include <iostream>
#include <string>
using namespace std;

int get_winner(int r, int p, int s) {
  int rr, pp, ss;
  while (true) {
    int total = r + p + s;
    rr = pp = ss = 0;
    if (total == 1) break;
    while (total > 0) {
      if (r >= p && r >= s) {
        r--;
        if (p >= s) {
          p--;
          pp++;
        } else {
          s--;
          rr++;
        }
      } else if (p >= r && p >= s) {
        p--;
        if (r >= s) {
          r--;
          pp++;
        } else {
          s--;
          ss++;
        }
      } else {
        s--;
        if (r >= p) {
          r--;
          rr++;
        } else {
          p--;
          ss++;
        }
      }
      total -= 2;
      if (r < 0 || p < 0 || s < 0) return -1;
    }
    r = rr;
    p = pp;
    s = ss;
  }
  if (r == 1) return 0;
  if (p == 1) return 1;
  if (s == 1) return 2;
  return -1;
}

string build(int step, int winner) {
  if (step == 1) {
    if (winner == 0) return "RS";
    if (winner == 1) return "PR";
    if (winner == 2) return "PS";
    return "-";
  }
  string s1, s2;
  if (winner == 0) {
    s1 = build(step-1, 0);
    s2 = build(step-1, 2);
  } else if (winner == 1) {
    s1 = build(step-1, 0);
    s2 = build(step-1, 1);
  } else {
    s1 = build(step-1, 1);
    s2 = build(step-1, 2);
  }
  if (s1+s2<s2+s1)
    return s1+s2;
  return s2+s1;
}

int main() {
  int t;
  cin >> t;
  for (int ti = 0; ti < t; ti++) {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    int winner = get_winner(r, p, s);
    cout << "Case #" << ti + 1 << ": ";
    if (winner == -1)
      cout << "IMPOSSIBLE";
    else {
      cout << build(n, winner);
    }
    cout << endl;
  }
}
