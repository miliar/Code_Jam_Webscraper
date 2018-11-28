#include <bits/stdc++.h>

using namespace std;

#ifdef ACMTUYO
struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#else
struct RTC{};
#define DBG(X)
#endif

#define fast_io() ios_base::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long int number;
typedef unsigned long long ULL;
ULL mulmod(ULL a, ULL b, ULL c){
  ULL x = 0,y = a % c;
  while(b > 0){
    if(b & 1) x += y;
    y <<= 1;
    if(x >= c) x -= c;
    if(y >= c) y -= c;
    b >>= 1;
  }
  return x;
}

ULL pow(ULL a, ULL b, ULL c){
  ULL x = 1,y = a;
  while(b > 0){
    if(b & 1) x = mulmod(x,y,c);
    y = mulmod(y,y,c);
    b >>= 1;
  }
  return x;
}

bool miller_rabin(ULL p, int it){
  if(p < 2) return false;
  if(p == 2) return true;
  if((p & 1) == 0) return false;
  
  ULL s = p - 1;
  while(s % 2 == 0) s >>= 1;
  
  while(it--){
    ULL a = rand() % (p-1) + 1,temp = s;
    ULL mod = pow(a,temp,p);
    
    if(mod == ULL(-1) || mod == ULL(1)) continue;
    
    while(temp != p-1 && mod != p-1){
      mod = mulmod(mod,mod,p);
      temp <<= 1;
    } 
    if(mod != p-1) return false;
  }
  return true;
}

#define abs_val(a) (((a)>0)?(a):-(a))

number mulmod(number a, number b, number c) {
  number x = 0, y = a % c;
  while (b > 0) {
    if (b % 2 == 1) x = (x + y) % c;
    y = (y * 2) % c;
    b /= 2;
  }
  return x % c;
}
number gcd(number a,number b) { return !b ? a : gcd(b, a % b); }

number pollard_rho(number n) {
  int i = 0, k = 2;
  number x = 3, y = 3;
  while (1) {
    i++;
    x = (mulmod(x, x, n) + n - 1) % n;
    number d = gcd(abs_val(y - x), n);
    if (d != 1 && d != n) return d;
    if (i == k) y = x, k *= 2;
  }
}

ULL ans;
const int maxn = 8000000;
number is_prime[maxn];
vector<number> primos;
void criba() {
  memset(is_prime, -1LL, sizeof(is_prime));
  for (int i = 2; i < maxn; i++)
    if (is_prime[i] == -1LL) {
      primos.pb(i);
      for (int j = i + i; j < maxn; j += i)
        is_prime[j] = i;
    }
}
number IS_PRIME(number num) {//-1 si es primo, si no un factor del numero
  if (num < maxn)
    return is_prime[num];
  for (int i = 0; i < sz(primos) && primos[i] * primos[i] <= num; i++)
    if (num % primos[i] == 0)
      return primos[i];
  if (miller_rabin(num, 3))//es primo
    return -1LL;
  number a = pollard_rho(num);
  number b = num / a;
  assert(a * b == num);
  return a;
}
number pows[10][17];
number to_decimal(number num, number base_from) {
  int idx = 0;
  number ans = 0;
  while (num > 0) {
    if (num & 1LL)
      ans += pows[base_from][idx];
    num >>= 1LL;
    idx++;
  }
  return ans;
}
vector<number> solve(int mask, int n) {
  mask = (1 << n) | mask;
  mask = (mask << 1) | 1;
  vector<number> ans;
  ans.pb(mask);
  for (int i = 2; i <= 10; i++) {
    number num = to_decimal(mask, i);
    number x = IS_PRIME(num);
    if (x == -1LL)
      break;
    ans.pb(x);
  }
  return ans;
}
int main() {
  criba();
  for (number base = 2LL; base <= 10LL; base++) {
    pows[base][0] = 1LL;
    for (int p = 1; p < 17; p++)
      pows[base][p] = pows[base][p - 1] * base;
  }

  int casos;
  cin >> casos;
  for (int caso = 1; caso <= casos; caso++) {
    int n, j;
    cin >> n >> j; 
    cout << "Case #"<< caso << ":\n";
    int nn = n - 2, lim = 1 << nn;
    for (int mask = 0; mask < lim && j > 0;mask++) {
      vector<number> sol = solve(mask, nn);
      if (sz(sol) == 10) {
        number N = sol[0];
        for (int x = n - 1; x >= 0; x--)
          if (N & (1 << x))
            cout << 1;
          else
            cout << 0;
        for (int i = 1; i <= 9; i++)
          cout << " " << sol[i];
        cout << '\n';
        j--;
      }
    }
  }
  return 0;
}

