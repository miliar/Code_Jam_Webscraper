/*
 * b.cpp
 *
 *  Created on: May 28, 2016
 *      Author: istrandjev
 */

#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

const string PROGRAM_NAME = "google";

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    int n, k;
    cin >> n >> k;
    vector<double> a(n);
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    double best = 0.0;
    for (int mask = 0; mask < (1 << n); ++mask) {
      int num = 0;
      for (int j = 0; j < n; ++j) {
        if (mask & (1 << j)) {
          num++;
        }
      }
      if (num != k) {
        continue;
      }

      double p = 0.0;
      for (int sm = mask; sm > 0; sm = ((sm-1)&mask)) {
        int broi = 0;
        for (int j = 0; j < n; ++j) {
          if (sm & (1 << j)) {
            broi++;
          }
        }
        if (broi * 2 != k) {
          continue;
        }

        ld tprob = 1.0;
        for (int j = 0; j < n; ++j) {
          if (mask & (1 << j)) {
            if (sm & (1 << j)) {
              tprob *= a[j];
            } else {
              tprob *= 1.0 - a[j];
            }
          }
        }
        p += tprob;
      }
      if (p > best) {
        best = p;
      }
    }
    cout << "Case #" << it << ": ";
    printf("%.9lf\n", best);
  }
  return 0;
}


