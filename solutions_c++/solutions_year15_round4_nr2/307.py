#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long int64;

const double EPS = 1e-6;

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int testCount;
  cin >> testCount;
  for (int t = 1; t <= testCount; ++t) {
    int n;
    double reqTemp, reqV;
    cin >> n >> reqV >> reqTemp;
    vector<double> temp(n), rate(n);
    for (int i = 0; i < n; ++i)
      cin >> rate[i] >> temp[i];
    cout << "Case #" << t << ": ";
    if (n == 1) {
      if (temp[0] - EPS <= reqTemp && reqTemp <= temp[0] + EPS)
        cout << fixed << setprecision(9) << reqV / rate[0] << "\n";
      else
        cout << "IMPOSSIBLE\n";
    } else if (n == 2) {
      if (min(temp[0], temp[1]) - EPS <= reqTemp && reqTemp <= max(temp[0], temp[1]) + EPS) {
        double V0, V1;
        if (abs(temp[1] - temp[0]) > EPS) {
          V1 = (reqTemp - temp[0]) * reqV / (temp[1] - temp[0]);
          V0 = reqV - V1;
          cout << fixed << setprecision(9) << max(V1 / rate[1], V0 / rate[0]) << "\n";
        } else {
          cout << fixed << setprecision(9) << reqV / (rate[0] + rate[1]) << "\n";
        }
      } else {
        cout << "IMPOSSIBLE\n";
      }
    } else {
      cout << "IMPOSSIBLE\n";
    }
  }
  cin.close();
  cout.close();
  return 0;
}
