#include <bits/stdc++.h> 
using namespace std; 
 
#define fr first 
#define sc second 
#define mp make_pair
#define pb push_back
#define LN(A) strlen(A)
#define SZ(A) int(A.size()) 
#define All(A) A.begin(), A.end()
#define rAll(A) A.rbegin(), A.rend()
#define line puts("~~~~~~~~~~~~~~~~~~~~~~~~")
 
typedef long long ll;
typedef pair<int, int> ii;
const long double EPS = 1e-12;
const int MX = 3 * int(1e5) + 2;
const int MOD = int(1e9) + 7; 

ll V[11], C[11];  
bool is_prime(ll N, int j) {
  for(ll i = 2; i * i <= N; ++i) {
    if(N % i == 0) {
      V[j] = i; 
      return 0; 
    }
  }
  V[j] = -1; 
  return 1; 
}

int T, CS, J, N; 
void solve() {
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d:\n", ++CS); 
    scanf("%d %d", &N, &J); 
    for(ll i = (1LL<<(N - 1)) + 1; J && i < (1LL<<N); i += 2) {
      bool is_prm = 0; 
      for(int j = 2; j <= 10 && !is_prm; ++j) {
        V[j] = -1; ll cur_N = 0, b = 1; 
        for(int k = 0; k < N; k++) {
          cur_N += ((1LL<<k) & i) ? b : 0; 
          b *= j; 
        }
        is_prm |= is_prime(cur_N, j), C[j] = cur_N; 
      }
      if(!is_prm) { 
        --J; 
        for(int k = N - 1; k >= 0; --k) printf("%d%s", (((1LL<<k) & i) ? 1 : 0), (k ? "" : " "));
        for(int j = 2; j <= 10; j++) printf("%lld%s", V[j], (j == 10 ? "\n" : " ")); 
      }
    }
  }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("../in.txt", "r", stdin); 
  freopen("../out.txt", "w", stdout); 
#endif 
  solve(); 
} 