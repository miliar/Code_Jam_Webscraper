
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

#define ll long long

void find_primes(ll int n,  vector<ll> &primes)
{
  vector<bool> is_prime(n+1, false);
  is_prime[2] = true;
  is_prime[3] = true;
  ll int lim = ceil(sqrt(n));
  for (ll int x = 1; x <= lim; x++)
  {
    for (ll int y = 1; y <= lim; y++)
    {
      ll int num = (4 * x * x + y * y);
      if (num <= n && (num % 12 == 1 || num % 12 == 5))
        is_prime[num] = true;
      num = (3 * x * x + y * y);
      if (num <= n && (num % 12 == 7))
        is_prime[num] = true;
 
      if (x > y) {
        num = (3 * x * x - y * y);
        if (num <= n && (num % 12 == 11))
          is_prime[num] = true;
      }
    }
  }
  for (ll int i = 5; i <= lim; i++) {
    if (is_prime[i]) {
      for (ll int j = i * i; j <= n; j += i)
        is_prime[j] = false;
    }
  }
 
  for (ll int i = 2; i <= n; i++) {
    if (is_prime[i])
      primes.push_back(i);
  }
}



ll calc(vector<ll> &t, vector<int> coin) {
  ll num = 0;
  for (int i = 0; i < coin.size(); i++) {
    num += coin[i] * t[i];
  }
  return num;
}

bool ok(vector<int> &coin, vector<ll> &primes, vector<vector<ll> > &t) {
  vector<ll> factors(11, -1);
  for (int b = 2; b < 11; b++) {
    ll num = calc(t[b], coin);
    for (int i = 0; i < primes.size(); i++) {
      if (primes[i] * primes[i] > num) break;
      if ((num % primes[i]) == 0) {
        factors[b] = primes[i];
        break;
      }
    }
    if (factors[b] == -1) return false;
  }

  for (int i = coin.size() - 1; i >= 0; i--) {
    cout << coin[i];
  }
  for (int i = 2; i < 11; i++) {
    cout << " " << factors[i];
  }
  cout << endl;
  return true;
}

  
void find_coins(vector<ll> &primes) {
  int N, J; cin >> N >> J; 
  vector<vector<ll> > t(11, vector<ll>(N, 1));
  for (int i = 1; i < N; i++) {
    for (int b = 2; b < 11; b++) {
      t[b][i] = t[b][i-1] * b;
    }
  }

  int curr = 1;
  vector<int> coin(N, 0); coin[0] = 1; coin[N-1] = 1;
  while (J) {
    if (ok(coin, primes, t)) {
      J--;
      if (!J) break;
    }
    while (coin[curr] != 0) curr++;
    coin[curr] = 1;
    while (--curr > 0) {
      coin[curr] = 0;
    }
    curr++;
  }
}

int main() {
  vector<ll> primes;
  ll limit = 100000000; 
  find_primes(limit, primes);
  int T; cin >> T; 
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ":\n";
    find_coins(primes);
  }
}
