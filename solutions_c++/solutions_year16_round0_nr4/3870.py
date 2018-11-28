#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

ll divs[11];

void pr(ll num) {
  vector<char> v;
  while (num > 0) {
    v.push_back((num % 2) + '0');
    num /= 2;
  }
  reverse(v.begin(), v.end());
  for(char c : v) cout << c;
}

ll conv(ll num, ll base) {
  ll mult = 1;
  ll res = 0;
  while (num > 0) {
    ll c = num % 2;
    num /= 2;
    res += c * mult;
    mult *= base;
  }
  return res;
}

bool test(ll num) {
  FOR(i, 2, 10) {
    ll cur = conv(num, i);
    bool good = false;
    FOR(j, 2, 10000) {
      if (cur % j == 0) {
        good = true;
        divs[i] = j;
        break;
      }
    }
    if (!good) return false;
  }
  return true;
}

void solve() {
  ll k, c, s;
  cin >> k >> c >> s;
  REP(i, s) {
    ll ind = i;
    REP(j,c-1) {
      ind *= s;
      ind += i;
    }
    cout << ind + 1 << ' ';
  }
}

int main() {
  int t;
  cin >> t;
  REP(i, t) {
    cout << "Case #" << (i+1) << ": ";
    solve();
    cout << endl;
  }
}