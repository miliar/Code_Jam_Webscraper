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

int main() {
  freopen((PROGRAM_NAME + ".in").c_str(), "r", stdin);
  freopen((PROGRAM_NAME + ".out").c_str(), "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    string s;
    int k;
    cin >> s >> k;
    int answer = 0;
    for (int i = 0; i <= (int)s.size() - k; ++i) {
      if (s[i] == '+') {
        continue;
      }
      answer++;
      for (int j = i; j < i + k; ++j) {
        s[j] = (s[j] == '+' ? '-' : '+');
      }
    }
    cout << "Case #" << it << ": ";
    if (s == string(s.size(), '+')) {
      cout << answer << endl;
    } else {
      cout << "IMPOSSIBLE\n";
    }
  }
  return 0;
}
