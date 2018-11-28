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

int T, CS, K, C, S; 
void solve() {
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d: ", ++CS); 
    scanf("%d %d %d", &K, &C, &S); 
    for(int i = 1; i <= S; i++) printf("%d%s", i, (i == S ? "\n" : " ")); 
  }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("../in.txt", "r", stdin); 
  freopen("../out.txt", "w", stdout); 
#endif 
  solve(); 
} 