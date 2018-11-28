#include <cstdio>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;

#define dbg(x) cout << #x << " = " << x << endl; 

const int N = 110;
const double eps = 1e-9;

int n;
double v, x;
double r[N], c[N];

int main()
{
    //freopen("in", "r", stdin);
    //freopen("out", "w", stdout);
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cout << "Case #" << tc << ": ";

        cin >> n >> v >> x;
        for (int i = 0; i < n; i++) {
          cin >> r[i] >> c[i];
        }
        //if (tc == 8 || tc == 47) {
          //cout << std::endl << fixed << setprecision(9) << n << std::endl << v << ' ' << x << std::endl << r[0] << ' ' << c[0] << std::endl << r[1] << ' ' << c[1] << std::endl;
        //}
        //continue;
        if (n == 1 || abs(c[0] - c[1]) < eps) {
          if (n == 2) {
            r[0] = r[0] + r[1];
          }
          if (abs(c[0] - x) < eps) {
            cout << fixed << setprecision(9) << v / r[0]; 
          } else {
            cout << "IMPOSSIBLE";
          }
        } else if (n == 2) {
          double v0 = v * (x - c[1]) / (c[0] - c[1]);
          double v1 = v - v0;
          if (x + eps < min(c[0], c[1]) || x - eps > max(c[0], c[1])) {
              cout << "IMPOSSIBLE";
          } else if (v0 < -eps || v1 < -eps) {
            //if (!(x - eps < min(c[0], c[1]) || x + eps > max(c[0], c[1]))) {
              //cout << std::endl << fixed << setprecision(9) << v << ' ' << x << std::endl << r[0] << ' ' << c[0] << std::endl << r[1] << ' ' << c[1] << std::endl;
              cout << "IMPOSSIBLE";
            //}
          } else {
            //if (abs(v0 + v1 - v) > 1e-6 || abs((v0 * c[0] + v1 * c[1]) / v - x) > 1e-6) {
              cout << fixed << setprecision(9) << max(v0 / r[0], v1 / r[1]);
            //}
          }
        }

        cout << endl;
    }
    return 0;
}
