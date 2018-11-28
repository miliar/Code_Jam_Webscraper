#include <algorithm>
#include <iostream>
#include <list>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
  int t, n, i = 1, aux;
  int lastN;
  bool changed;
  string str;
  char c;
  vector<bool> p;
  set<int> s;
  cin >> t;
  while (i <= t) {
    cin >> str;
    aux = 0;
    changed = false;
    p.clear();
    for (char c : str) {
      if (c == '+') {
        p.push_back(true);
      } else {
        p.push_back(false);
      }
    }
    int x = p.size();
    while (x > 0) {
      if (changed) {
        p[x - 1] = !p[x - 1];
      }
      if (p[x - 1] == false) {
        if (changed)
          changed = false;
        else
          changed = true;
        p[x - 1] = true;
        aux++;
      }
      x--;
    }
    cout << "Case #" << i << ": " << aux << endl;
    i++;
  }
}
