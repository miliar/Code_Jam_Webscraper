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

string solve(int r, int p, int s) {
  if ((r + p - s) % 2 != 0 || (r + s - p) % 2 != 0 || (p + s - r) % 2 != 0 || r > p + s || s > p + r || p > s + r) {
    return "";
  }
  if (r + p + s == 2) {
    string res;
    if (r == 2 || p == 2 || s == 2) {
      return "";
    }
    if (p) {
      res += "P";
    }

    if (r) {
      res += "R";
    }

    if (s) {
      res += "S";
    }

    return res;
  }
  int pr = (p + r - s) / 2;
  int rs = (r + s - p) / 2;
  int sp = (s + p - r) / 2;
  string temp = solve(rs, pr, sp);
  string res;
  for (int i = 0; i < (int)temp.size(); ++i) {
    if (temp[i] == 'P') {
      res += "PR";
    } else if (temp[i] == 'R') {
      res += "RS";
    } else {
      res += "PS";
    }
  }
  return res;
}

void optimize(string& r) {
  for (int size = 1; size < (int)r.size(); size *= 2) {
    for (int i = 0; i + size < (int)r.size(); i += size * 2) {
      string a = r.substr(i, size);
      string b = r.substr(i + size, size);
      if (a > b) {
        for (int j = 0; j < size; ++j) {
          r[i + j] = b[j];
          r[i + size + j] = a[j];
        }
      }
    }
  }
}
int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string res = solve(r, p, s);
    if (res != "") {
      optimize(res);
    } else {
      res = "IMPOSSIBLE";
    }
    cout << "Case #" << it << ": "  << res << endl;
  }
  return 0;
}
