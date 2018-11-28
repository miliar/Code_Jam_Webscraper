/*
 * d-small.cpp
 *
 *  Created on: May 31, 2014
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
#include <unordered_set>
#include <unordered_map>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

int get(const vector<string>& a) {
  unordered_set<ll> prefs;


  for (int i = 0; i < (int)a.size();++i) {
    ll pref = 0;
    if (!a[i].empty()) {
      prefs.insert(0);
    }
    for (int j = 0; j < (int)a[i].size(); ++j) {
      pref = pref * 27LL + (ll)(a[i][j] - 'A' + 1);
      prefs.insert(pref);
    }
  }
  return prefs.size();
}
pair<int, int> solve(const vector<string>& a, int m) {
  int n = (int)a.size();
  int val =1;
  for (int i = 0; i < n; ++i) {
    val *= m;
  }
  int bres = -1;
  int bcount = 0;
  for (int i = 0; i < val; ++i) {
    int mask = i;
    vector<vector<string> > temp(m);
    for (int j = 0; j < n; ++j) {
      temp[mask % m].push_back(a[j]);
      mask /= m;
    }
    int res = 0;
    for (int l = 0; l < (int)temp.size(); ++l) {
      res += get(temp[l]);
    }
    if (bres == res) {
      bcount++;
    } else if (bres == -1 || bres < res) {
      bres = res;
      bcount = 1;
    }
  }
  return make_pair(bres, bcount);
}
int main() {
  freopen("google.in", "r", stdin);
  freopen("google.out", "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {

    int n, m;
    scanf("%d %d", &m, &n);
    vector<string> a(m);
    getline(cin, a[0]);
    for (int i = 0; i < (int)a.size(); ++i) {
      getline(cin, a[i]);
    }
    pair<int, int> temp = solve(a, n);
    cout << "Case #" << it << ": " << temp.first << " " << temp.second << endl;
  }

  return 0;
}


