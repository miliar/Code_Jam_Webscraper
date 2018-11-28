#include <bits/stdtr1c++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  int t; cin >> t;
  for (int T = 1; T <= t; T++) {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string a = "Z";
    for (int i = 0; i < pow(3,pow(2,n)); i++) {
      int R = 0, P = 0, S = 0;
      int I = i;
      string x = "";
      for (int j = 0; j < pow(2,n); j++) {
        switch (I % 3) {
          case 0: R++; x.push_back('R'); break;
          case 1: P++; x.push_back('P'); break;
          case 2: S++; x.push_back('S'); break;
          default: break;
        }
        I /= 3;
      }
      if (R != r || P != p || S != s)
        continue;
      //cout << "test " << R << " " << P << " " << S << " " << x << endl;
      string xs = x;
      bool g = true;
      while (x.size() > 1) {
        string x2 = "";
        for (int j = 0; j < x.size()/2; j++) {
          if (x[2*j] == x[2*j+1]) {
            g = false;
            break;
          }
          if (x[2*j] == 'P' && x[2*j+1] == 'R')
            x2.push_back('P');
          if (x[2*j] == 'R' && x[2*j+1] == 'P')
            x2.push_back('P');
          if (x[2*j] == 'P' && x[2*j+1] == 'S')
            x2.push_back('S');
          if (x[2*j] == 'S' && x[2*j+1] == 'P')
            x2.push_back('S');
          if (x[2*j] == 'R' && x[2*j+1] == 'S')
            x2.push_back('R');
          if (x[2*j] == 'S' && x[2*j+1] == 'R')
            x2.push_back('R');
        }
        if (!g)
          break;
        x = x2;
      }
      if (g && a > xs)
        a = xs;
    }
    cout << "Case #" << T << ": ";
    if (a != "Z")
      cout << a << "\n";
    else
      cout << "IMPOSSIBLE\n";
  }
  return 0;
}
