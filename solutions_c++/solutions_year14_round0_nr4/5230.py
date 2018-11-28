#include <algorithm>
#include <assert.h>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <numeric>
#include <limits>
#include <iomanip>
using namespace std;

#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define LL long long
#define LD long double
#define vi vector<int>
#define vl vector<LL>
#define vs vector<string>
#define vb vector<bool>
#define ii pair<int, int>
#define vii vector<ii>
#define SET(v, i) (v | (1 << i))
#define TEST(v, i) (v & (1 << i))
#define TOGGLE(v, i) (v ^ (1 << i))

int GetScoreWar(vector<double>& naomi, vector<double>& ken) {
  int ret = sz(naomi), j = 0;
  for (int i = 0; i < sz(naomi); ++i) {
    while (j < sz(ken) && ken[j] < naomi[i]) {
      ++j;
    }

    if (j < sz(ken))
      --ret;
    ++j;
  }

  return ret;
}

int main() {
  ifstream cin("D-small-attempt0.in");
  ofstream cout("out.txt");
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int n;
    cin >> n;
    vector<double> naomi(n);
    for (int i = 0; i < n; ++i)
      cin >> naomi[i];

    vector<double> ken(n);
    for (int i = 0; i < n; ++i)
      cin >> ken[i];

    sort(all(naomi));
    sort(all(ken));

    int i = 0, j = 0;
    int cnt = 0;
    while (i < n) {
      if(naomi[i] > ken[j]) {
        ++cnt;
        ++j;
      }

      ++i;
    }

    int score_war = GetScoreWar(naomi, ken);
    cout << "Case #" << tt << ": " << cnt << " " << score_war << endl;
  }
  return 0;
}
