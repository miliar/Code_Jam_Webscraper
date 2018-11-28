#include <bits/stdc++.h>
#define MAX 1<<16
using namespace std;

typedef long long ll;
int t,n,j;
vector<ll> primes;

ll getnumber(string s, int base){
  ll ret = 0;
  ll b = 1;
  for(int i = s.size()-1; i >= 0; i--){
    ret += (s[i] == '1') ? b : 0;
    b *= 1LL*base;
  }
  return ret;
}

int isprime(ll n){

  if(n%2 == 0) return 2;

  ll sq = sqrt(n);
  for(ll i = 3; i <= sq; i += 2){
    if(n%i == 0)
      return i;
  }
  return 0;


  // for(int i = 0; primes[i] <= sq; i++){
  //   if(n%primes[i] == 0)
  //     return primes[i];
  // }
  // return 0;
}

void sieve(){
  bitset<MAX> prime;
  prime.set();
  prime[0] = prime[1] = 0;

  ll sq = sqrt(MAX);
  for(int i = 2; i <= sq; i++){
    if(!prime[i]) continue;
    for(int j = i*i; j < MAX; j+=i){
      prime[j] = 0;
    }
  }

  for(int i = 0; i < MAX; i++){
    if(prime[i]){
      primes.push_back(i);
    }
  }

}

void addone(string& s, int n){

  int carry = 1;
  int i = n-2;
  while(carry && i>=0){
    int sum = (s[i] == '0' ? 0 : 1) + carry;
    s[i] = (sum%2)+'0';
    carry = sum/2;
    i--;
  }

}

int main(){

  cin >> t;
  cin >> n >> j;
  //  sieve();

  cout << "Case #1:" << endl;
  string s(n, '0');
  s[0] = s[n-1] = '1';
  while(j){

    vector<ll> divs;
    for(int b = 2; b <= 10; b++){
      ll num = getnumber(s, b);
      //      cout << "s = " << s << " num = " << num << " base = " << b << endl;
      ll d = isprime(num);
      if(d == 0) break;
      divs.push_back(d);
    }

    if(divs.size() == 9){
      cout << s;
      for(int i = 0; i < 9; i++){
	cout << " " << divs[i];
      }
      cout << endl;
      j--;
    }
    addone(s, n);

  }

  return 0;
}
