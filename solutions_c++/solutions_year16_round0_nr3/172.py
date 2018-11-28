#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <bitset>

using namespace std;
typedef long long ll;
#define all(c)  (c).begin(),(c).end()
#define rep(var,n)  for(int var=0;var<(n);var++)

vector<int> primes;
char *is_prime = NULL;

void dealloc_sieve() {
  if (is_prime) { free((void*)is_prime); is_prime = NULL; }
}

int prepare_primes_until(int till) {
  is_prime = (char *)malloc(1+till);
  if (!is_prime) return -1;
  memset((void*)is_prime, 1, 1+till);
  primes.clear();

  for (int i=2; i<=till; i++){
    if (is_prime[i]) {
      primes.push_back(i);
      for (int j=i*2; j<=till; j+=i) is_prime[j] = false;
    }
  }
  return primes.size();
}

long long random(long long n)
{
  return (long long)rand() % n;
}

long long check_nontrivial_sqrt_1(long long m, long long a)
{
  long long r = (a * a) % m;
  return (1LL < a && a < m-1 && r == 1)? 0LL : r;
}

long long expmod(long long base, long long exp, long long m)
{
  if (exp == 0)
    return 1LL;
  else if (!(exp & 1))
    return check_nontrivial_sqrt_1(m,expmod(base,exp/2,m));
  else
    return (base*expmod(base,exp-1,m)) % m;
}

bool miller_rabin_test(long long n)
{
  return expmod((1LL+random(n-1)),n-1,n) == 1LL;
}

bool fast_prime(long long n, int times=3)
{
  if (n == 1) return false;
  if (n == 2) return true;
  else if (!(n & 1)) return false;

  for (int i=times; i>0; i--)
        if (!miller_rabin_test(n)) return false;
  return true;
}

ll nontrivial_divisor(ll n) {
  if ((n & 1LL) == 0LL) return 2LL;

  for (int i=1,c=primes.size(); i<c; ++i) {
    int prime = primes[i];
    if (prime >= n) return -1LL;
    if (n % primes[i] == 0) return primes[i];
  }
  // あきらめた
  return -1LL;
}

ll check(int N, int pat, vector<ll>& divisors) {
  // cout << bitset<16>(pat) << ":" << endl;

  for (int b=2; b<=10; ++b) divisors[b] = -1;

  ll n = 0, x;
  for (int b=2; b<=10; ++b) {
    n = 0; x = 1;
    for (int i=0,m=1; i<N; ++i,m<<=1) {
      if (pat & m) n += x;
      x *= b;
    }
    bool p = fast_prime(n, 4);
    if (p) {
      // printf("\tbase %d: %lld %s\n", b, n, p?"(prime)":"-");
      return -1;
    }

    divisors[b] = nontrivial_divisor(n); // bad
    if (divisors[b] == -1) return -1;
  }
  return n;
}

void solve(int N, int J) {
  // srand(0);
  int cnt = 0;

  vector<ll> divisors(11);

  ll pat_begin = (1LL << (N-1)) + 1, pat_end = (1LL << N) - 1;
  for (ll pat=pat_begin; pat<=pat_end; pat+=2) { // from 100..001 to 111..111
    ll n10 = check(N, pat, divisors);
    if (n10 > 0) {
      cout << n10;
      for (int b=2; b<=10; ++b) {
        cout << " " << divisors[b];
      }
      cout << endl;

      ++cnt;
      if (cnt == J) return;
    } else {
      //cout << "x " << bitset<16>(pat) << endl;
      // ++cnt;
    }
  }
}

int main(){
  prepare_primes_until(1000000);

  int _T; cin>>_T; // 1-100
  rep(_t,_T){
    cout << "Case #" << (1+_t) << ":" << endl;
    int N, J; cin >> N >> J;
    solve(N, J);
  }
}
