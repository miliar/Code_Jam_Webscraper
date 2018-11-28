#include <bits/stdc++.h>
using namespace std;



int main() {
  cout << fixed << setprecision(20);

  int Z;
  cin >> Z;
  for (int z=1; z<=Z; ++z) {
    int n;
    cin >> n;
    long double vt, tt;
    cin >> vt >> tt;
    vector<long double> v(n), t(n);
    for (int i = 0; i < n; ++i)
      cin >> v[i] >> t[i];

    vector<long double> results;

    for (int i = 0; i < n; ++i) {
      if (t[i] == tt)
        results.push_back(vt / v[i]);
    }

    

    if (n == 2) {
      if ((t[0] < tt and t[1] > tt) or (t[0] > tt and t[1] < tt)) {
        long double v0 = vt * (tt - t[1]) / (t[0] - t[1]);
        long double v1 = vt - v0;
        results.push_back(max(v0 / v[0], v1 / v[1]));
        assert(v0 > 0 && v1 > 0);

      }
      if (t[0]==tt and t[1]==tt)
        results.push_back(vt / (v[0]+v[1]));
    }


    if (results.empty()) {
      cout << "Case #" << z << ": " << "IMPOSSIBLE" << endl;
    } else {
     long double result = *min_element(results.begin(), results.end());
     
     cout << "Case #" << z << ": " << result << endl;
    }
  }
}
