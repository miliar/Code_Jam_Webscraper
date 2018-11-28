#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <cmath>
#include <bitset>
#include <list>
#include <queue>
#include <sstream>

using namespace std;

#define e '\n'
#define INF 1023456789
#define ll long long

//#define FILE "data"

#ifdef FILE
ifstream f(string (string(FILE) + ".in").c_str());
ofstream g(string (string(FILE) + ".out").c_str());
#endif
#ifndef FILE
#define f cin
#define g cout
#endif

#ifdef CLION
#undef f
#undef g
ifstream f("data.in");
#define g cout
#endif

ll mul_inv(ll a, ll b) {
  ll b0 = b, t, q;
  ll x0 = 0, x1 = 1;
  if (b == 1) return 1;
  while (a > 1) {
    q = a / b;
    t = b, b = a % b, a = t;
    t = x0, x0 = x1 - q * x0, x1 = t;
  }
  if (x1 < 0) x1 += b0;
  return x1;
}

ll t, n, rez, x, m, k, r, p, s;
int i, j, ii;
string s1, s2;

string pp[15];
string rr[15];
string ss[15];
ll v[15][4];


string subdivide(string str, long long gap) {
  if (gap < 2) {
    return str;
  }

  string ret = "";
  string part1, part2;

  for (long long i = 0; i < str.size(); i += gap * 2) {
    part1 = str.substr(i, gap);
    part2 = str.substr(i + gap, gap);
    if (part1 < part2) {
      ret += part1 + part2;
    } else {
      ret += part2 + part1;
    }
  }

  return subdivide(ret, gap / 2);
}


int main() {
  v[0][1] = 1;

  for (int i = 1; i <= 12; i++) {
    v[i][1] = v[i - 1][1] + v[i - 1][3];
    v[i][2] = v[i - 1][2] + v[i - 1][1];
    v[i][3] = v[i - 1][3] + v[i - 1][2];
  }

  pp[0] += "P";
  rr[0] += "R";
  ss[0] += "S";

  for (int i = 1; i <= 12; i++) {
    for (char c : pp[i - 1]) {
      if (c == 'P') {
        pp[i] += "PR";
      } else if (c == 'R') {
        pp[i] += "RS";
      } else {
        pp[i] += "PS";
      }
    }
    pp[i] = subdivide(pp[i], pp[i].size() / 2);
  }


  for (int i = 1; i <= 12; i++) {
    for (char c : rr[i - 1]) {
      if (c == 'P') {
        rr[i] += "PR";
      } else if (c == 'R') {
        rr[i] += "RS";
      } else {
        rr[i] += "PS";
      }
    }
    rr[i] = subdivide(rr[i], rr[i].size() / 2);
  }


  for (int i = 1; i <= 12; i++) {
    for (char c : ss[i - 1]) {
      if (c == 'P') {
        ss[i] += "PR";
      } else if (c == 'R') {
        ss[i] += "RS";
      } else {
        ss[i] += "PS";
      }
    }
    ss[i] = subdivide(ss[i], ss[i].size() / 2);
  }

  f >> t;

  for (int ii = 1; ii <= t; ii++) {

    f >> x >> r >> p >> s;

    if ((v[x][1] == p && v[x][2] == r && v[x][3] == s)) {
      g << "Case #" << ii << ": " << pp[x] << e;

    } else if ((v[x][1] == r && v[x][2] == s && v[x][3] == p)) {
      g << "Case #" << ii << ": " << rr[x] << e;

    } else if ((v[x][1] == s && v[x][2] == p && v[x][3] == r)) {
      g << "Case #" << ii << ": " << ss[x] << e;

    } else {
      g << "Case #" << ii << ": " << "IMPOSSIBLE" << e;
    }

  }
}
