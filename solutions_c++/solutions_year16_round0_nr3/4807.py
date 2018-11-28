#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int num_of_case = 1;

void output(string v){
  cout << "Case #" << num_of_case++ << ": " << v << endl;
}

string i2s(ll i){
  string res;
  stringstream a;
  a << i;
  a >> res;
  return res;
}

void output(ll v){
  cout << "Case #" << num_of_case++ << ": " << v << endl;
}

string int2binary(ll i){
  string res;
  while(i != 0){
    if(i % 2 == 0){
      res.append(1, '0');
    }else{
      res.append(1, '1');
    }
    i /= 2;
  }
  reverse(res.begin(), res.end());
  return res;
}

ll str2nbase(int base, string str){
  ll mul = 1;
  ll res = 0;
  for(ll i= str.length() - 1; i >= 0; i--){
    res += mul * (str[i] - '0');
    mul*=base;
  }
  return res;
}

bool isPrime(ll num){
  for(ll j = 2; j*j < num; j++){
    if(num%j == 0){
      return false;
    }
  }
  return true;
}

int main(void){
  int T; cin >> T;
  while(T--){

    int N, J; cin >> N >> J;
    vector<ll> divalue;
    for(ll i=1+pow(2, N-1); i < pow(2, N); i+=2){
      bool dividable = true;
      for(int base = 2; base <= 10; base++){
        ll num = str2nbase(base, int2binary(i));
        //cout << "int2bninary(" << i << ") = " << int2binary(i) << endl;
        //cout << "str2nbase(" << base << ", " << int2binary(i) << ") = " << str2nbase(base, int2binary(i)) << endl;
        if(isPrime(num)) {
          dividable = false;
          break;
        }
      }
      if(dividable == false) continue;
      if(dividable == true){
        divalue.push_back(i);
      }
      if(divalue.size() == J) break;
    }
    cout << "Case #1:" << endl;
    for(ll i=0; i < divalue.size(); i++){
      string ans;
      ans += int2binary(divalue[i]);
      for(int base = 2; base <= 10; base++){
        ll num = str2nbase(base, int2binary(divalue[i]));
        ll divisor = -1;
        for(ll j=2; j < num; j++){
          if(num % j == 0){
            divisor = j;
            break;
          }
        }
        ans += " " + i2s(divisor);
      }
      cout << ans << endl;
    }
  }
  return 0;
}
