#include <iostream>
#include <vector>
#include <string>

using namespace std;

int flip(int p) {
  if (p == 0) {
    return 1;
  } else {
    return 0;
  }
}

void flip(vector<int>& p, int index, int& flips) {
  if (index > 0 && p[0] != 0) {
    for (int i = 0; i < index && p[i] == 1; i++) {
      p[i] = 0;
    }
    flips++;
  }
  if (index == 0) {
    p[0] = 1;
  } else {
    for (int i = 0, j = index; i <= j; i++, j--) {
      if (i == j) {
        p[i] = flip(p[i]);
      } else {
        int t = p[i];
        p[i] = flip(p[j]);
        p[j] = flip(t);
      }
    }
  }
  flips++;
}

void solve() {
  string ps;
  cin >> ps;
  vector<int> p;
  for(string::iterator it = ps.begin(); it != ps.end(); ++it) {
    if (*it == '-') {
      p.push_back(0);
    } else {
      p.push_back(1);
    }
  }
  int flips = 0;
  for (int i = p.size() - 1; i >= 0; i--) {
    if (p[i] == 0) {
      flip(p, i, flips);
    }
  }
  cout << flips << endl;
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i ++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
