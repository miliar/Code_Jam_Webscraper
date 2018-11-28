#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long int lli;

static const lli MAX = 1e+14;

lli A, B;
vector<lli> num;

bool check(lli v) {
  stringstream ss;
  ss << v;
  string tmp = ss.str();
  int sz = tmp.size();
  for(int i = 0; i < sz / 2; i++) {
    if(tmp[i] != tmp[sz - 1 - i]) return false;
  }
  return true;
}

void init() {
  for(lli i = 1LL; i * i <= MAX; i++) {
    if(check(i) && check(i * i)) num.push_back(i * i);
  }
}

int solve() {
  return upper_bound(num.begin(), num.end(), B) - lower_bound(num.begin(), num.end(), A);
}

int main() {
  init();
  
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; tc++) {
    cin >> A >> B;
    cout << "Case #" << tc << ": " << solve() << endl;
  }
  return 0;
}
