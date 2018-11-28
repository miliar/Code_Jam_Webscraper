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

set<int> S; 
int chk(ll n) {
  while(n) { S.insert(n%10); n /= 10; } 
  return SZ(S) == 10; 
}

int T, CS;  
ll N, n; 
void solve() {
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d: ", ++CS); 
    scanf("%lld", &N); 
    n += N;
    if(!n) { puts("INSOMNIA"); continue; }
    while(!chk(n)) n += N; 
    printf("%lld\n", n); 
    S.clear(); n = 0;  
  }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("../in.txt", "r", stdin); 
  freopen("../out.txt", "w", stdout); 
#endif 
  solve(); 
} 