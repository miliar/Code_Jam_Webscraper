#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;

ll digits[20];
vector <ll> divi;

ll factor(ll x){
  if(x == 1) return -1;
  if(x == 2)  return -1;
  if(x%2 == 0)  return 2;
  for(ll i = 3; i*i <= x; i += 2)
    if(x % i == 0)  return i;
  return -1;
}

int main(){
  ios_base::sync_with_stdio(0);
  ll n, j, aux, ex, cont = 0;
  cin >> n >> j;
  cout << "Case #1:\n";
  for(int i = 0; i < (1 << (n - 2)); ++i){
    divi.assign(16, 0);
    memset(digits, 0, sizeof digits);
    aux = 2*i + 1 + (1 << (n - 1));

    for(int q = 0; q < n; ++q)
      if(aux & (1 << q))
        digits[q] = 1;

    for(ll b = 2; b < 11; ++b){
      ex = 1;
      aux = 0;
      for(int i = 1; i <= n; ++i){
        if(digits[n - i]) aux += ex;
        ex *= b;
      }
      divi[b] = factor(aux);
      if(divi[b] == -1) break;
      if(b == 10){
        ++cont;
        cout << aux << " ";
        for(int q = 2; q < 11; ++q) cout << divi[q] << " \n"[q == 10];
      }
    }
    if(cont == j) break;
  }

  return 0;
}
