#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll pot(ll n, int k){
  if(k == 0) return 1LL;
  if(k == 1) return n;
  ll aux = pot(n,k>>1);
  if(k&1) return n*aux*aux;
  return aux*aux;
}

ll div(ll var){
  if(!(var&1)) return 2;

  ll d = 3;
  while(var){
    if(var % d == 0) return d;
    else d += 2;
  }
}

string base2(ll n){
  string s = "";
  while(n){
    if(n & 1LL) s = "1" + s;
    else s = "0" + s;
    n >>= 1;
  }
  return s;
}

bool prime(ll n){
  if(!(n&1)) return 0;

  ll d = 3;
  while(d*d <= n){
    if(n % d == 0) return 0;
    d += 2;
  }
  return 1;
}

bool testprime(string s, vector<ll> &v){
  int size = s.size();
  for(int i = 2; i < 11; ++i){
    ll var = 0;
    for(int k = 0; k < size; ++k)
      if(s[k] == '1')
        var += pot(i,size-1-k);
    if(prime(var)) return false;
    else v.push_back(var);
  }
  return 1;
}

int main(){
  ios_base::sync_with_stdio(false);
  ifstream ifs("C-small-attempt1.in");
  ofstream ofs("C-small-attempt1_output.txt");
  int t, tcase = 1;
  //cin >> t;
  ifs >> t;

  while(t--){
    int n,j;
    //cin >> n >> j;
    ifs >> n >> j;

    //cout << "Case #" << tcase++ << ":\n";
    ofs << "Case #" << tcase++ << ":\n";

    ll start = pot(2,n-1) + 1;
    ll limit = pot(2,n);
    int cont = 0;

    for(ll k = start; k < limit; k+=2){
      vector<ll> v;
      string s = base2(k);
      if(testprime(s,v)){
        //cout << s << " ";
        ofs << s << " ";

        for(int i = 2; i < 10; ++i){
          ll var = v[i-2];
          //cout << div(var) << " ";
          ofs << div(var) << " ";
        }
        ll var = v[8];
        //cout << div(var) << "\n";
        ofs << div(var) << "\n";

        if(++cont == j) break;
      }
    }
  }
  return 0;
}
