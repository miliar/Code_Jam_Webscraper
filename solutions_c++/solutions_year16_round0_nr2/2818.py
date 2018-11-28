#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "B"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

int MinFlipsRec(string s, map<string, int>& cache, int depth) {
  if (cache.find(s) != cache.end()) {
    return cache[s];
  }
  if (count(s.begin(), s.end(), '-') == 0) {
    return cache[s] = 0;
  }
  if (depth > 10) {
    return depth;
  }
  int& result = cache[s];
  result = 2 * s.length();
  for (int i = 0; i < s.length(); ++i) {
    string t = s;
    for (int j = 0; j <= i; ++j) {
      t[j] = ('+' + '-') - s[i - j];
    }
    int curres = MinFlipsRec(t, cache, depth + 1);
    if (result > curres + 1) {
      result = curres + 1;
    } 
  }
  return cache[s] = result;
}

int MinFlipsStupid(string s) {
  //map<string, int> cache;
  //return MinFlipsRec(s, cache, 0);
  int mask = 0;
  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == '-') {
      mask += (1 << i);
    }
  }
  int n = s.length();
  vi dist(1 << n, 1 << n);
  vb done(1 << n, false);
  dist[mask] = 0;
  for (int i = 0; i < (1 << n); ++i) {
    int min_dist = 1 << n;
    int min_index = -1;
    for (int j = 0; j < (1 << n); ++j) {
      if (!done[j] && dist[j] < min_dist) {
        min_dist = dist[j];
        min_index = j;
      }
    }
    if (min_index == -1) {
      break;
    }
    done[min_index] = true;
    for (int k = 0; k < n; ++k) {
      int new_mask = (min_index >> (k + 1)) << (k + 1);
      for (int l = 0; l <= k; ++l) {
        new_mask += (!((min_index >> (k - l)) & 1)) << l;
      }
      if (!done[new_mask] && dist[new_mask] > dist[min_index] + 1) {
        dist[new_mask] = dist[min_index] + 1;
      }
    }
  }
  return dist[0];
}

int MinFlipsFast(string s) {
  int res = 0;
  while (count(s.begin(), s.end(), '-') > 0) {
    ++res;
    if (s[0] == '+') {
      ++res;
      int i = 0;
      while (s[i] == '+') {
        s[i] = '-';
        ++i;
      }
    }
    int i = s.length() - 1;
    while (s[i] == '+') {
      --i;
    }
    string t = s;
    for (int j = 0; j <= i; ++j) {
      s[j] = ('+' + '-') - t[i - j];
    }
  }
  return res;
}

int main() {
  /*while (true) {
    int n = rand() % 10 + 1;
    string s = "";
    for (int i = 0; i < n; ++i) {
      s += (rand() % 2 ? '-' : '+');
    }
    cerr << s << endl;
    int res1 = MinFlipsStupid(s);
    int res2 = MinFlipsFast(s);
    if (res1 != res2) {
      cerr << "Wrong answer: " << res1 << ' ' << res2 << endl;
      break;
    } else {
      cerr << "OK " << res1 << endl;
    }
  }*/
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    string s;
    cin >> s;
    cout << "Case #" << (test_index + 1) << ": ";
    cerr << "Case #" << (test_index + 1) << ": ";
    int res = MinFlipsFast(s);
    cout << res << endl;
    cerr << res << endl;
  }
  return 0;
}
