#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
typedef long long ll;
typedef vector<ll> vll;

bool pal(ll i){
  if (i < 10) return true;
  ll c = i;
  ll p=0;
  while (i != 0) {
     p = p*10 + i%10;
     i /= 10;
  }
  return (p == c);
}


int main() {
  vll v;
  for (ll i = 1; i*i <= 10e14; ++i) {
    if (pal(i) and pal(i*i))
      v.push_back(i*i);
  }
  ll t, a, b;
  cin >> t;
  for (int cases = 1; cases <= t; ++cases) {
    cin >> a >> b;
    int ai = 0, bi = 0;
    while (a > v[ai])
      ++ai;
    while (b >= v[bi])
      ++bi;
    cout << "Case #" << cases << ": " << bi - ai << endl;
  }
}

