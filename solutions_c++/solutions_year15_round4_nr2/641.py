#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
 
#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
 
typedef long long int64;
 
using namespace std;

void solve() {
   int n;
   double V, X;
   cin >> n >> V >> X;
   vector<double> r(n), c(n);
   for (int i = 0; i < n; ++i) cin >> r[i] >> c[i];
   if (n == 1) {
       if (X - 1e-12 < c[0] && c[0] < X + 1e-12) {
           printf("%.10lf\n", (double)V / r[0]);
       } else {
           cout << "IMPOSSIBLE" << endl;
       }
       return;
   }
   if (c[0] > c[1]) {
       swap(r[0], r[1]);
       swap(c[0], c[1]);
   }
   double left = 0;
   double right = 1e12;
   for (int iter = 0; iter < 1000; ++iter) {
       double t = (left + right) / 2;
       double minx;
       if (r[0] * t > V) {
           minx = c[0];
       } else {
           double t2 = (V - r[0] * t) / r[1];
           if (t2 < t) {
               minx = (r[0] * t * c[0] + r[1] * t2 * c[1]) / V;
           } else {
               left = t;
               continue;
           }
       }
       double maxx;
       if (r[1] * t > V) {
           maxx = c[1];
       } else {
           double t1 = (V - r[1] * t) / r[0];
           if (t1 < t) {
               maxx = (r[0] * t1 * c[0] + r[1] * t * c[1]) / V;
           } else {
               left = t;
               continue;
           }
       }
       if (minx - 1e-10  < X && X < maxx + 1e-10) {
           right = t;
       } else {
           left = t;
       }
   }
   if (left > 1e11) {
       cout << "IMPOSSIBLE" << endl;
   } else {
       printf("%.10lf\n", (double)left);   
   }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
