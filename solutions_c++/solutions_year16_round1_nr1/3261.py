#include <iostream>
#include <string>
using namespace std;

void solve(string x, int last) {
  if (last == 0) {
    return;
  }
  int mp = 0;

  for (int i = 0; i < last; ++i) {
    if (x[i] >= x[mp]) {
      mp = i;
    }
  }

  cout << x[mp];
  solve(x, mp);
  for (int i = mp + 1; i < last; ++i) {
    cout << x[i];
  }
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    string a;
    cin >> a;

    solve(a, a.size());
    cout << endl;
  }
}
