#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll, ll> ii;
typedef pair<ll, ll> pll;

const ll N = 4e3 + 5;
// string ans[N];

ll _sieve_size;
bitset<100000100> bs;   // 10^7 should be enough for most cases
vi primes;
vector<string> res;
map<string, vi> v;
map<ll, string> ans;

void sieve(ll upperbound) {          // create list of primes in [0..upperbound]
  _sieve_size = upperbound + 1;                   // add 1 to include upperbound
  bs.set();                                                 // set all bits to 1
  bs[0] = bs[1] = 0;                                     // except index 0 and 1
  for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
    // cross out multiples of i starting from i * i!
    for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
    primes.push_back((ll)i);  // also add this vector containing list of primes
  }
}                                           // call this method in main method

ll isPrime(ll N) {                 // a good enough deterministic prime tester
  // if (N <= _sieve_size) return bs[N];                   // O(1) for small primes
  for (ll i = 0; i < (ll)primes.size(); i++)
  if (N % primes[i] == 0 and N != primes[i]) return primes[i];
  return false;                    // it takes longer time if N is a large prime!
}


bool check(string s){
  ll n = 32;
  for(ll b = 2; b <= 10; b++){
    bool ok = 0;
    for (ll i = 0; i < (ll)primes.size(); i++){
      ll num = 0;
      ll  num2 = 0;
      for(ll j = 0; j < n; j++){
        num = (num * b + (s[j] - '0'))%primes[i];
        if(num2 <= primes[i]){
          num2 = (num2 * b + (s[j] - '0'));
        }
      }
      if (num == 0 and num2 != primes[i]){
        ok = 1;
        v[s].push_back(primes[i]);
        break;
      }
    }
    if(!ok) return false;
  }
  return true;
}

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  ll t;
  ll cs = 0;
  cin >> t;
  sieve(100000);
  while(t--){
    cs++;
    cout <<"Case #" << cs << ":\n";
    ll n, k;
    cin >> n >> k;
    for(ll i = 1; i < 1 << 16; i++){
      ans[i] = "1";
      for(ll j = 0; j < n - 2; j++){
        if((i & (1 << j))) ans[i] = '1' + ans[i];
        else ans[i] = '0' + ans[i];
      }
      ans[i] = '1' + ans[i];
    }
    for(ll i = 1; i < 1 << 16; i++){
      if(res.size() >= 500 ) break;
      if(check(ans[i])) res.push_back(ans[i]);
    }
    for(auto x: res){
      cout << x << " ";
      for(auto y : v[x]){
        cout << y <<" ";
      }
      cout <<endl;
    }
  }
  return 0;
}
