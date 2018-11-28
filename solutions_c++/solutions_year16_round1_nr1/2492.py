#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define DEBUG(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long double ld;
typedef long long ll;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

string solve(string s) {
  if (s.size() == 0) return s;

  int best_ind = int(s.size()) - 1;
  char best = s[int(s.size()) - 1];
  for (int i = int(s.size()) - 1; i >= 0; --i) {
    if (s[i] > best) {
      best = s[i];
      best_ind = i;
    }
  }
  return s[best_ind] + solve(s.substr(0, best_ind)) + s.substr(best_ind + 1);
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    string s;
    cin >> s;
    cout << "Case #" << ca << ": " << solve(s) << endl;
  }
}
