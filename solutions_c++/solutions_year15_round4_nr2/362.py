/*
 * b-small.cpp
 *
 *  Created on: May 30, 2015
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

struct tube {
  double v;
  double x;
};

double sign(double x) {
  if (x < -epsylon) {
    return -1;
  }
  if (x > epsylon) {
    return 1;
  }

  return 0;
}

bool nula(double x) {
  return sign(x) == 0;
}

double solve(ld x0, ld v0, ld x1, ld v1, ld tx, ld tv) {
  if (sign(x0 - tx) != 0 && sign(x0 - tx) == sign(x1 - tx)) {
    return -1.0;
  }

  if (sign(x0 - tx) > 0) {
    return solve(x1, v1, x0, v0, tx, tv);
  }

  if (sign(x0 - tx) == 0) {
    if (sign(x1 - tx) == 0) {
      return tv / (v0 + v1);
    } else {
      return tv / v0;
    }
  }

  if (sign(x1 - tx) == 0) {
    return tv / v1;
  }

  ld beg = 0, end = tv;
  for (int step = 0; step < 100; ++step) {
    ld mid = (beg + end) * 0.5;

    ld tt = (mid * x0 + (tv - mid) * x1) / tv;
    if (tt > tx) {
      beg = mid;
    } else {
      end = mid;
    }
  }

  return max(beg / v0, (tv  - beg) / v1);
}

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    int n;
    double tv, tx;
    cin >> n >> tv >> tx;
    vector<tube> a(n);
    for (int i = 0; i < (int)a.size(); ++i) {
      cin >> a[i].v >> a[i].x;
    }
    if (n == 1) {
      cout << "Case #" << it << ": ";
      if (!nula(tx - a[0].x)) {
        cout << "IMPOSSIBLE" << endl;
      } else {
        printf("%.9lf\n", tv / a[0].v);
      }
      continue;
    }

    if (n > 2) {
      cout << "Case #" << it << ": ?\n";
      continue;
    }


    cout << "Case #" << it << ": ";
    double ans = solve(a[0].x, a[0].v, a[1].x, a[1].v, tx, tv);
    if (sign(ans) < 0) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      printf("%.9lf\n", ans);
    }
  }
  return 0;
}

