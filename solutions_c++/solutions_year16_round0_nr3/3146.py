#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll bases[11][16];

int N, J;

ll convert(ll num, int base) {
  ll ans = 0;
  for(int i = 0; i < N; i++) {
    if((num >> i) & 1) {
      ans += bases[base][i];
    }
  }
  return ans;
}
bool isPrime(ll num, ll & div_out) {
  if(num % 2 == 0) {
    div_out = 2;
    return false;
  }
  for(ll i = 3; i * i <= num; i += 2) {
    if(num % i == 0) {
      div_out = i;
      return false;
    }
  }
  return true;
}
bool isJamcoin(ll num, ll arr[11]) {
  ll div;
  if(isPrime(num, div)) {
    return false;
  }
  arr[2] = div;
  for(int i = 3; i < 11; i++) {
    ll d;
    ll n = convert(num, i);
    //cout << "converted to base " << i << " = " << n << "\n";
    if(isPrime(n, d)) {
      return false;
    }
    arr[i] = d;
  }
  return true;
}

void binary(ll n) {
  for(int i = N-1; i >= 0; i--) {
    cout << ((n>>i) & 1);
  }
  cout << " ";
}
int main() {
  //freopen("B-small-attempt1.in", "r" , stdin);
  //freopen("B-large.in", "r" , stdin);
  //freopen("in", "r" , stdin);
  //freopen("Blarge.out", "w" , stdout);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> N >> J;

    for(ll i = 3; i < 11; i++) {
      bases[i][0] = 1;
      ll ans = 1;
      for(int j = 1; j < N; j++) {
        ans *= i;
        bases[i][j] = ans;
      }
    }

    ll curr = (1 << (N-1));
    curr = curr | 1;
    //cout << curr << endl;

    cout << "Case #" << t << ":" << "\n";
    ll arr[11];
    while(J) {
    //for(int a = 0 ; a < 10; a++){
      //binary(curr);
      if(isJamcoin(curr, arr)) {
        //cout<<"YAY";
        J--;
        binary(curr);
        for(int i = 2; i < 11; i++) {
          cout << arr[i] << " ";
        }
        cout <<"\n";
      }
      //else {
      //  cout<<"NEY";
      //}
      curr += 2;
    }

  }
}
