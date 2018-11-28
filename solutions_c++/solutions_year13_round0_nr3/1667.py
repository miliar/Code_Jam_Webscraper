#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

#define rep(i, n) for(int i = 0; i < n; i++)
#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long ll;

vector<ll> sq;
vector<ll> square;
int accum[10000005];

bool palindrome(ll x) {
  stringstream ss;
  ss << x;
  string s = ss.str();
  string t = s;
  reverse(all(t));
  return s == t;
}

int init() {
  int cnt = 0;
  for(ll i = 1; i <= 10000000; i++) {
    if(palindrome(i) && palindrome(i * i)) cnt++;
    accum[i] = cnt;

    sq.push_back(i);
    square.push_back(i * i);
  }
}

int search(ll X) {
  auto it = lower_bound(all(square), X);

  return (*it == X) ? (it - square.begin()) : (-1);
}

int solve(ll A, ll B) {
  ll a, b;
  ll ix;

  if((ix = search(A)) != -1) {
    a = sq[ix] - 1;
  }
  else {
    a = (ll)sqrt(A);
  }

  if((ix = search(B)) != -1) {
    b = sq[ix];
  }
  else {
    b = (ll)sqrt(B);
  }

  return accum[b] - accum[a];
}

int main() {

  init();

  int T;
  cin >> T;

  rep(t, T) {
    ll a, b;
    cin >> a >> b;

    cout << "Case #" << (t + 1) << ": " << solve(a, b) << endl;
  }

  return 0;
}
