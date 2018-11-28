#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#include <complex>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <cassert>
using namespace std;

typedef long long ll;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
bool ISINT(double x){return fabs(x-(int)round(x))<EPS;}
bool ISEQ(double x,double y){return fabs(x-y)<EPS;}
string itos(ll x){stringstream ss;ss<<x;return ss.str();}
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin();itr!=c.end();itr++)

int main() {
  int T;
  cin >> T;

  for (int CASE = 1; CASE <= T; CASE++) {
    cout << "Case #" << CASE << ": ";

    int bit = 0;
    ll N, sum = 0;
    cin >> N;
    
    if (N == 0) {
      cout << "INSOMNIA" << endl;
      continue;
    }
    
    for (int i = 1; i <= 1000000; i++) {
      sum += N;

      ll tmp = sum;
      while (tmp > 0) {
        int d = tmp % 10;
        tmp /= 10;
        bit |= (1 << d);
      }
      if (bit == (1 << 10) - 1) {
        break;
      }
    }
    if (bit == (1 << 10) - 1) {
      cout << sum << endl;
    } else {
      cout << "INSOMNIA" << endl;
    }
  }
}
