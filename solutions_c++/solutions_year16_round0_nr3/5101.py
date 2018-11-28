#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second
#define vi vector<int>
#define vii vector< pii >

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

#define maxN 37
int N, J;

#define maxNum 100000005
bool is_not_prime[maxNum];
int divisor[maxNum];
int primes[maxNum], pr;

int arr[maxN];
long long interpret(int base) {
  long long ans = 0;
  REP(i, N) {
    ans = ans * base + arr[i];
  }
  return ans;
}

int get_divisor(long long x) {
  REP(i, pr) {
    if (primes[i] >= x) return 0;
    if (x % primes[i] == 0) return primes[i];
  }
  return 0;
}

int main() {
  is_not_prime[0] = is_not_prime[1] = true;
  FOR(i, 2, maxNum - 1) {
    if (!is_not_prime[i]) {
      primes[pr++] = i;
      for (int j = 2 * i; j < maxNum; j += i) {
        is_not_prime[j] = true;
        divisor[j] = i;
      }
    }
  }
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%d%d", &N, &J);
    printf("Case #%d:\n", t);
    REP(bm, (1 << N)) {
      if (J == 0) break;
      if (!(bm & (1 << (N-1)))) continue;
      if (!(bm & 1)) continue;
      REP(i, N) arr[i] = ((bm & (1 << i))) ? 1 : 0;
      bool ok = true;
      FOR(b, 2, 10) {
        if (get_divisor(interpret(b)) == 0) { ok = false; break; }
      }
      if (ok) {
        REP(i, N) printf("%d", arr[i]);
        FOR(b, 2, 10) {
          printf(" %d", get_divisor(interpret(b)));
        }
        printf("\n");
        --J;
      }
    }
  }

  return 0;
}
