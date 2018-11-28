#include <bits/stdc++.h>

using namespace std;

int soln = 0;
string flip(string s, int i) {
  string go = "";
  for (int z = i; z >= 0; z--) {
    if (s[z] == '-') go += '+';
    else go += '-';
  }
  for (int z = i + 1; z < s.size(); z++) {
    go += s[z];
  }
  soln++;
  return go;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int N; cin >> N;
  for (int _ = 0; _ < N; _++) {
    soln = 0;
    string s; cin >> s;

    for (int i = s.size() - 1; i >= 0; i--) {
      if (s[i] == '-') {
        if (s[0] == '-') {
          s=flip(s, i);
        } else {
          int j = 0;
          while (s[j] == '+' && j < i) j++;
          s=flip(s, j - 1);
          s=flip(s, i);
        }
      }
    }
    cout << "Case #" << (_ + 1) << ": " << soln << endl;
  }

  return 0;
}
