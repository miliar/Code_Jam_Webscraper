#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long double ld;

ld w[100][2];

int main() {
  ios::sync_with_stdio(0);
  cout << fixed << setprecision(9);
  int t; cin >> t;
  for (int T = 1; T <= t; T++) {
    cout << "Case #" << T << ": ";
    int n; ld v, x;
    cin >> n >> v >> x;
    //cout << n << " " << v << " " << x <<endl;
    for (int i = 0; i < n; i++)
      cin >> w[i][0] >> w[i][1];
    //for (int i = 0; i < n; i++)
    //  cout << w[i][0] << " " << w[i][1]<<endl;
    //cout << endl;
    if (n == 1) {
      if (w[0][1] == x)
        cout << v/w[0][0];
      else
        cout << "IMPOSSIBLE";
    }
    else if (n == 2) {
      int a = 0, b = 0, c = 0;
      for (int i = 0; i < n; i++) {
        if (w[i][1] < x)
          a++;
        else if (w[i][1] > x)
          b++;
        else
          c++;
      }
      if ((a && !b && !c) || (!a && b && !c)) {
        cout << "IMPOSSIBLE";
        goto VELOCIRAPTOR;
      }
      if (c && ((a && !b) || (!a && b) || (!a && !b))) {
        ld tr = 0;
        for (int i = 0; i < n; i++)
          if (w[i][1] == x)
            tr += w[i][0];
        cout << v/tr;
        goto VELOCIRAPTOR;
      }
      // TODO include case where there is a and b and c
      // otherwise, at this point we have a and b
      ld v1 = v*(w[0][1]-x)/(w[0][1]-w[1][1]);
      ld v0 = v-v1;
      ld t1 = v1/w[1][0], t0 = v0/w[0][0];
      cout << max(t0,t1);
    }
    else {
      //TODO
    }
    VELOCIRAPTOR:
    cout << "\n";
  }
  return 0;
}
