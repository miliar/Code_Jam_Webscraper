/*
 * d.cpp
 *
 *  Created on: Apr 9, 2016
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

vector<ll> solve(ll k, ll c) {
  if (c > k) {
    c = k;
  }

  ll remaining = k;
  ll offset = 0;

  vector<ll> res;
  while (remaining > 0) {
    ll add = offset;

    int lim = c;
    if (lim > remaining) {
      lim = remaining;
    }
    for (ll i = 0; i < lim - 1; ++i) {
      add = add * k + (i + 1LL + offset);
    }

    res.push_back(add);
    offset += lim;
    remaining -= lim;
  }

  return res;
}

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    ll k, c, s;
    cin >> k >> c >> s;
    vector<ll> res = solve(k, c);
    cout << "Case #" << it << ":";
    if ((int)res.size() > s) {
      cout << "IMPOSSIBLE\n";
    } else {
      for (int i = 0; i < (int)res.size(); ++i) {
        cout << " " << res[i] + 1;
      }
      cout << endl;
    }
  }

  return 0;
}


