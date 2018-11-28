#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

#define pb push_back
#define pf push_front

#define fori(n)  for(int i=0;i<n;i++)
#define forj(n)  for(int j=0;j<n;j++)
#define fork(n)  for(int k=0;k<n;k++)
#define forit(v) for(it = v.begin();it != v.end();it++)

#define trace(x...) x
#define print(x...) trace(printf(x))
#define watch(x) trace(cout << #x" = " << x << "\n")

#define INF 0x3F3F3F3F // Signed int
//#define INF 0x3F3F3F3F3F3F3F3FLL // Signed int64
#define EPS 1e-10
#define PI 3.14159265358979323846

int cmpD(double a, double b){
	return (a <= b + EPS) ? (a + EPS < b) ? -1 : 0 : 1;
}

using namespace std;

typedef pair<int,int> pairii;
typedef vector<int> vint;
typedef vector<char> vchar;
typedef vector<bool> vbool;
typedef vector<string> vstring;
typedef long long int64;
typedef unsigned long long Uint64;
typedef unsigned int Uint;
typedef unsigned char Uchar;

// N = 10^5 (0.011s)
// N = 10^6 (0.056s)
// Optimized Sieve - O(?) Wtf!
const int MAXN = 10000001, SIZE = MAXN/16+1;
const int MAX_PRIMES = 685000; // 1.26 * MAXN / log(MAXN);
char mark[SIZE]; // ( mark[n>>4]&(1<<((n>>1)&7)) ) == 0 se 2*n+1 eh primo
int primes[MAX_PRIMES], cnt_primes;
bool is_prime[MAXN];
void sieve(int N) {
	int i, j;
	for ( i = 3; i*i <= N; i += 2 ) if ( ( mark[i>>4] & (1<<((i>>1)&7)) ) == 0 )
		for ( j = i*i; j <= N; j += i<<1 ) mark[j>>4] |= ( 1<<((j>>1)&7) );
	cnt_primes = 0;
	primes[cnt_primes++] = 2;
	for ( i = 3; i <= N; i += 2 ) if ( (mark[i>>4]&(1<<((i>>1)&7))) == 0 )
		primes[cnt_primes++] = i;
	fori(N) is_prime[i] = false; fori(cnt_primes) is_prime[primes[i]] = true;
}

long long getBase(int t, int base_factor) {
  long long base = 1;
  long long total = 0;

  while (t) {
    total += base * (t & 1);
    base *= base_factor;
    t >>= 1;
  }

  return total;
}

void printBin(int t) {
  int mask = 1 << 15;
  while (mask) {
    cout << ((mask & t) > 0 ? 1 : 0);
    mask >>= 1;
  }
}

int divisor(long long t, int base) {
  for (auto prime : primes) {
    if (prime <= 0 || prime >= t) break;
    int temp = base % prime;;
    for (int i = 1;i < 31;i++) {
      temp *= base;
      temp %= prime;
    }
    if (((t % prime) + (temp % prime)) % prime == 0)
      return prime;
  }
  return 1;
}

int main() {
  sieve(MAXN);

  int t;

  int n;
  int j;

  cin >> t >> n >> j;

  int mask = 0;
  mask |= 1;

  cout << "Case #1:" << endl;
  vector<int> divisors(11);
  int counter = 0;
  for (int i = 0;i < 1 << (16 - 2);i++) {
    if (counter == j) break;
    int num = (mask | (i << 1));
    bool ok = true;
    for (int j = 2;j <= 10;j++) {
      auto base = getBase(num, j);
      divisors[j] = divisor(base, j);
      if (divisors[j] == 1) {
        ok = false;
        break;
      }
    }
    if (ok) {
      counter++;
      cout << "1000000000000000";
      printBin(num);
      for (int j = 2;j <= 10;j++) cout << " " << divisors[j];
      cout << endl;
    }
  }

/*
  int num1 = getBase(mask, 2);
  int num2 = getBase(mask, 3);
  int num3 = getBase(mask, 4);
  int num4 = getBase(mask, 5);
  int num5 = getBase(mask, 6);
  int num6 = getBase(mask, 7);
  int num7 = getBase(mask, 8);
  int num8 = getBase(mask, 9);
  int num9 = getBase(mask, 10);

  cout << num1 << " = " << divisor(num1) << endl;
  cout << num2 << " = " << divisor(num2) << endl;
  cout << num3 << " = " << divisor(num3) << endl;
  cout << num4 << " = " << divisor(num4) << endl;
  cout << num5 << " = " << divisor(num5) << endl;
  cout << num6 << " = " << divisor(num6) << endl;
  cout << num7 << " = " << divisor(num7) << endl;
  cout << num8 << " = " << divisor(num8) << endl;
  cout << num9 << " = " << divisor(num9) << endl;
  */

  return 0;
}
