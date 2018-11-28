/*
 * c-small.cpp
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
#include <unordered_set>
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
    unordered_set<string> english;
    unordered_set<string> french;

    string temp;
    int n;
    cin >> n;
    vector<vector<string> > sentences(n - 2);
    getline(cin, temp);
    getline(cin, temp);
    istringstream eng(temp);
    while (eng >> temp) {
      english.insert(temp);
    }
    getline(cin, temp);
    istringstream fre(temp);
    while (fre >> temp) {
      french.insert(temp);
    }
    for (int i = 0; i < n - 2; ++i) {
      getline(cin, temp);
      istringstream iss(temp);
      while (iss >> temp) {
        sentences[i].push_back(temp);
      }
    }

    int base = 0;
    for (unordered_set<string>::iterator it = english.begin(); it != english.end(); ++it) {
      if (french.count(*it)) {
        base++;
      }
    }

    int best = -1;
    for (int mask = 0; mask < 1 << (n - 2); ++mask) {
      unordered_set<string> f;
      unordered_set<string> e;
      int broi = base;

      for (int i = 0; i < n - 2; ++i) {
        if (mask & (1 << i)) {
          for (int j = 0; j < (int)sentences[i].size(); ++j) {
            if (french.count(sentences[i][j]) != 0) {
              continue;
            }
            if (english.count(sentences[i][j])) {
              broi++;
            }
            f.insert(sentences[i][j]);
          }
        }
      }
      for (int i = 0; i < n - 2; ++i) {
        if ((mask & (1 << i)) == 0) {
          for (int j = 0; j < (int)sentences[i].size(); ++j) {
            if (e.insert(sentences[i][j]).second) {
              if (english.count(sentences[i][j]) == 0 &&
                  (f.count(sentences[i][j]) || french.count(sentences[i][j]))) {
                broi++;
              }
            }
          }
        }
      }

      if (best == -1 || broi  < best) {
        best = broi;
      }
    }
    cout << "Case #" << it << ": " << best << endl;
  }
  return 0;
}

