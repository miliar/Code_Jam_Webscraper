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

int T, CS, c, ans, ln, f; 
char S[123]; 

void solve() {
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d: ", ++CS); 
    scanf("%s", S); ln = LN(S); 
    int i = 0; 
    while(i < ln && S[i] == '-') ++i; 
    if(i) ans = 1; 
    for(; i < ln; i++) {
      if(S[i] == '-') c++; 
      else ans += (c ? 2 : 0), c = 0; 
    }
    printf("%d\n", ans + (c ? 2 : 0)); 
    ans = c = f = 0;  
  }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("../in.txt", "r", stdin); 
  freopen("../out.txt", "w", stdout); 
#endif 
  solve(); 
} 