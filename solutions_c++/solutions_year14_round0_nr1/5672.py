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

int main() {
  ifstream cin("A-small-attempt0.in");
  ofstream cout("out.txt");
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; ++tt) {
    int r1, r2;
    cin >> r1;
    --r1;
    vi row1(4);
    int d;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cin >> d;
        if (i != r1)
          continue;

        row1[j] = d;
      }
    }

    cin >> r2;
    --r2;
    int cnt = 0;
    int v = -1;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cin >> d;
        if (i != r2)
          continue;

        if (std::count(all(row1), d) > 0) {
          ++cnt;
          v = d;
        }
      }
    }

    cout << "Case #" << tt << ": ";
    if (cnt == 1) {
      cout << v << endl;
      assert(v > 0);
    } else if (cnt > 1) {
      cout << "Bad magician!" << endl;
    } else {
      cout << "Volunteer cheated!" << endl;
    }
  }
  return 0;
}
