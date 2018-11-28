#pragma comment(linker, "/STACK:256000000")
#include <stdio.h>
#include <iostream>
#include <cmath>
#include <math.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

const double EPS = 1e-8;

class push_water {
public:
  double rate, temperature;
  bool operator < (push_water another) {
    return temperature < another.temperature;
  }
};


int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  std::ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) { 
    int n;
    double V, X;
    cin >> n;
    cin >> V >> X;
    vector<push_water> data(n+2);
    for (int i = 1; i < n + 1; ++i) {
      cin >> data[i].rate >> data[i].temperature;
    }
    sort(data.begin()+1, data.end()-1);
    if (X + EPS < data[1].temperature || X > EPS + data[n].temperature) {
      cout << "Case #" << t << ": ";
      cout << "IMPOSSIBLE" << "\n";
      continue;
    }
    double VY = 0, Y = 0, res = 0;
    for (int i = 1; i < n+1; ++i) {
      Y = (VY * Y + data[i].rate * data[i].temperature) / (VY + data[i].rate);
      VY += data[i].rate;
    }
    if (Y > X) {
      VY = 0;
      Y = data[1].temperature;
      double r1 = 0, t1 = 0;
      int i = 1;
      while (Y < X + EPS && i < n+1) {
        t1 = Y;
        r1 = VY;
        Y = (VY * Y + data[i].rate * data[i].temperature) / (VY + data[i].rate);
        VY += data[i].rate;
        i++;
      }
      double rate = r1 + data[i-1].rate;
      if ((data[i-1].temperature - X) > EPS) { 
        rate = r1 * (X - t1) / (data[i-1].temperature - X) + r1;
      }
      res = V / rate;
    } else {
      VY = 0;
      Y = data[n].temperature;
      double r1 = 0, t1 = 0;
      int i = n;
      while (Y + EPS > X && i > 0) {
        t1 = Y;
        r1 = VY;
        Y = (VY * Y + data[i].rate * data[i].temperature) / (VY + data[i].rate);
        VY += data[i].rate;
        i--;
      }
      double rate = r1 + data[i+1].rate;
      if (abs(data[i+1].temperature - X) > EPS) {
       rate = r1 * (X - t1) / (data[i+1].temperature - X) + r1;
      }
      res = V / rate;

    }

    cout.precision(22);
    cout << "Case #" << t << ": ";
    cout << res << "\n";
  }
}
/*
5
4 4
>>v<
..v.
..v.
^<<.
*/