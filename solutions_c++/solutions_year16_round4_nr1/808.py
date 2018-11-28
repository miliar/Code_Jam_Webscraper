#include <iostream>

using namespace std;

string fill(char win, int lvl) {
  string res = "";
  if (lvl == 0) {
    res += win;
    return res;
  }
  string left = fill(win, lvl - 1);
  string right;
  if (win == 'R')
    right = fill('S', lvl - 1);
  else if (win == 'S')
    right = fill('P', lvl - 1);
  else if (win == 'P')
    right = fill('R', lvl - 1);
  res += min(left, right);
  res += max(left, right);
  return res;
}

bool can_rock(int n, int r, int p, int s) {
  int nr = 0, np = 0, ns = 0;
  nr = 1;
  for (int i = 0; i < n; ++i) {
    int _ns = ns + nr;
    int _nr = nr + np;
    int _np = np + ns;
    ns = _ns;
    nr = _nr;
    np = _np;
  }
  if (ns == s && nr == r && np == p) {
    string res = "";
    res = fill('R', n);
    cout << res;
    return true;
  } else {
    return false;
  }
}

bool can_sic(int n, int r, int p, int s) {
  int nr = 0, np = 0, ns = 0;
  ns = 1;
  for (int i = 0; i < n; ++i) {
    int _ns = ns + nr;
    int _nr = nr + np;
    int _np = np + ns;
    ns = _ns;
    nr = _nr;
    np = _np;
  }
  if (ns == s && nr == r && np == p) {
    string res = "";
    res = fill('S', n);
    cout << res;
    return true;
  } else {
    return false;
  }
}

bool can_pap(int n, int r, int p, int s) {
  int nr = 0, np = 0, ns = 0;
  np = 1;
  for (int i = 0; i < n; ++i) {
    int _ns = ns + nr;
    int _nr = nr + np;
    int _np = np + ns;
    ns = _ns;
    nr = _nr;
    np = _np;
  }
  if (ns == s && nr == r && np == p) {
    string res = "";
    res = fill('P', n);
    cout << res;
    return true;
  } else {
    return false;
  }
}

int main() {
  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string ans = "";
    cout << "Case #" << test << ": ";
    if (!can_rock(n, r, p, s))
      if (!can_sic(n, r, p, s))
        if (!can_pap(n, r, p, s))
          cout << "IMPOSSIBLE";

    cout << '\n';
  }
  return 0;
}
