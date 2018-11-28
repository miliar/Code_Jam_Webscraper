#include <bits/stdtr1c++.h>
using namespace std;

typedef long long ll;

const int N = 16, J = 50;
vector<int> primes;
const int G = 100000;
bool np[G];

int main() {
  for (int i = 4; i < G; i++)
    np[i] = true;
  primes.push_back(2);
  for (ll i = 3; i < G; i += 2) {
    if (!np[i]) {
      for (ll j = i*i; j < G; j += i)
        np[j] = true;
    }
    primes.push_back(i);
  }
  int d = 0;
  for (int i = 0; i < (1<<(N-2)); i++) {
    if ((__builtin_popcount(i)+2)%3)
      continue;
    vector<bool> v;
    vector<int> dv;
    v.push_back(1);
    for (int j = 0; j < N-2; j++)
      v.push_back((1<<j)&i);
    v.push_back(1);
    bool g = true;
    for (int j = 2; j < 10; j++) {
      ll b = 1;
      bool bg = true;
      for (ll k = 1, e = j; k < N; k++, e *= j)
        if (v[k])
          b += e;
      for (int k : primes) {
        if (k >= b)
          break;
        if (b % k == 0) {
          bg = false;
          dv.push_back(k);
          break;
        }
      }
      if (bg) {
        g = false;
        break;
      }
    }
    if (g) {
      for (int j = N-1; j >= 0; j--)
        cout << v[j];
      for (int j : dv)
        cout << " " << j;
      cout << " 3\n";
      d++;
    }
    if (d == J)
      break;
  }
  cout << d << endl;
  return 0;
}
