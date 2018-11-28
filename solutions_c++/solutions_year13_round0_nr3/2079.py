#include <iostream>
#include <vector>
#include <cmath>

typedef long long ll;

using namespace std;

// Check fair
bool isfair(ll x) {
  bool ans = true;
  vector<int> digits;
  while (x > 0) {
    digits.push_back(x % 10);
    x /= 10;
  }
  for (int n = 0; n < digits.size(); n++) {
    if (digits[n] != digits[digits.size() - 1 - n])
      ans = false;
  }
  return ans;
}

// Create palindrone
ll makefair1(ll x) {
  vector<int> digits;
  while (x > 0) {
    digits.push_back(x % 10);
    x /= 10;
  }
  int ans = 0;
  for (int s = digits.size() -1; s >= 0; s--)
    ans = ans * 10 + digits[s];
  for (int s = 1; s < digits.size(); s++)
    ans = ans * 10 + digits[s];
  return ans;
}
ll makefair2(ll x) {
  vector<int> digits;
  while (x > 0) {
    digits.push_back(x % 10);
    x /= 10;
  }
  int size0 = digits.size();
  int ans = 0;
  for (int s = digits.size() -1; s >= 0; s--)
    ans = ans * 10 + digits[s];
  for (int s = 0; s < digits.size(); s++)
    ans = ans * 10 + digits[s];
  return ans;
}
void makefair_help(vector<ll> &table, ll x1, ll x2, bool which) {
  for (ll x = x1; x < x2; x++) {
    ll y = which ? makefair1(x) : makefair2(x);
    if (isfair(y*y))
      table.push_back(y * y);
  }
}

// Make a list of all fair and square numbers' sqrts
int main() {

  vector<ll> table;

/*
  // 1 Brute Force - check all numbers's squares
  for (ll x = 1; x < 1000000; x++) {
    if (isfair(x) && isfair(x * x))
      cout << x * x << endl;
  }
*/
  // 2 Brute Force Skip - check all palindrone's squares
  makefair_help(table, 1, 10, true);
  makefair_help(table, 1, 10, false);
  makefair_help(table, 10, 100, true);
  makefair_help(table, 10, 100, false);
  makefair_help(table, 100, 1000, true);
  makefair_help(table, 100, 1000, false);
  makefair_help(table, 1000, 10000, true);
  makefair_help(table, 1000, 10000, false);
  makefair_help(table, 10000, 100000, true);
  makefair_help(table, 10000, 100000, false);
  makefair_help(table, 100000, 1000000, true);
  makefair_help(table, 100000, 1000000, false);

  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    ll A, B;
    cin >> A >> B;

    cout << "Case #" << t+1 << ": ";
    int ans = 0;
    for (auto elem: table) {
      if ( (A <= elem) && (B >= elem) )
        ans++;
    }
    cout << ans << endl;
  }

  return 0;

}
