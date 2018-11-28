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
int moves[4][2] = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
int rev[256];
int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;

  rev['^'] = 0;
  rev['>'] = 1;
  rev['v'] = 2;
  rev['<'] = 3;
  for (int it = 1; it <= nt; it++) {
    int n,m;
    cin >> n >> m;

    vector<string> a(n,string(m, ' '));
    getline(cin, a[0]);
    for (int i = 0; i < (int)a.size(); ++i) {
      getline(cin, a[i]);
    }

    int answer = 0;
    bool possible = true;
    for (int i = 0; i< n && possible; ++i) {
      for (int j = 0; j < (int)a[i].size() && possible; ++j) {
        if (a[i][j] == '.') {
          continue;
        }
        int dir = rev[a[i][j]];
        int cx = i + moves[dir][0];
        int cy = j + moves[dir][1];
        while (cx >= 0 && cx < n && cy >= 0 && cy < m && a[cx][cy] == '.') {
          cx += moves[dir][0];
          cy += moves[dir][1];
        }

        if (cx >= 0 && cx < n && cy >= 0 && cy < m) {
          continue;
        }

        answer++;

        bool found = false;
        for (int ad = 1; ad < 4; ++ad) {
          int ndir = (dir + ad) % 4;
          int ncx = i + moves[ndir][0];
          int ncy = j + moves[ndir][1];
          while (ncx >= 0 && ncx < n && ncy >= 0 && ncy < m && a[ncx][ncy] == '.') {
            ncx += moves[ndir][0];
            ncy += moves[ndir][1];
          }

          if (ncx >= 0 && ncx < n && ncy >= 0 && ncy < m) {
            found = true;
            break;
          }
        }

        if (found == false) {
          possible = false;
          break;
        }
      }
    }
    cout << "Case #" << it << ": ";

    if (!possible) {
      cout << "IMPOSSIBLE"<< endl;
    } else {
      cout << answer << endl;
    }
  }
  return 0;
}
