#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)

using namespace std;
typedef long long int ll;
typedef vector<int> VI;
typedef pair<int, int> PI;
const double EPS=1e-9;

int digits(ll a) {
  int acc = 0;
  while (a > 0) {
    acc |= 1 << (a % 10);
    a /= 10;
  }
  return acc;
}

ll calc(ll n) {
  int acc = 0;
  ll mul = n;
  while (1) {
    acc |= digits(mul);
    if (acc == 0x3ff) {
      return mul;
    }
    mul += n;
  }
}

int main(void){
  int t;
  cin >> t;
  REP(loop_cnt, 1, t + 1) {
    int n;
    cin >> n;
    cout << "Case #" << loop_cnt << ": ";
    if (n == 0) {
      cout << "INSOMNIA" << endl;
    } else {
      cout << calc(n) << endl;
    }
  }
}
