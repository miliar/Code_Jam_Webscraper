#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int main() {
  int casos;
  cin >> casos;
  for (int cas = 1; cas <= casos; ++cas) {
    cout << "Case #" << cas << ": ";
    ll n, p;
    cin >> n >> p;
    
    ll ini = 0, fin = (1LL << n) - 1;
    while (ini <= fin) {
      ll m = (ini + fin)/2;
      ll aux = 0, pot = 1;
      while (pot <= m + 1) {
        ++aux;
        pot *= 2;
      }
      --aux;
      ll aux2 = 0;
      for (int i = n - 1; i >= 0 and aux > 0; --i, --aux) aux2 += (1LL << ll(i));
      if (aux2 < p) ini = m + 1;
      else fin = m - 1;
    }
    ll res1 = ini - 1;
    
    ini = 0; fin = (1LL << n) - 1;
    while (ini <= fin) {
      ll m = (ini + fin)/2;
      ll aux = 0, pot = 1;
      while (pot <= (1LL << n) - m) {
        ++aux;
        pot *= 2;
      }
      --aux;
      ll aux2 = (1LL << n) - 1;
//       cerr << m << " " << aux << endl;
      for (int i = n - 1; i >= 0 and aux > 0; --i, --aux) aux2 ^= (1LL << ll(i));
//       cerr << aux2 << endl;
      if (aux2 < p) ini = m + 1;
      else fin = m - 1;
    }
    ll res2 = ini - 1;
    
    cout << res1 << " " << res2 << endl;
  }
}
