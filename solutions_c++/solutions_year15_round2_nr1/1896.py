#include <bits/stdc++.h>

using namespace std;

#define SZ(A) (int)A.size()
#define fr first
#define pb push_back
#define sc second
#define mp make_pair
#define _map unordered_map
#define _set unordered_set
#define pr_q priority_queue
#define pb push_back

typedef pair<int, int> ii;
typedef unsigned long long ll;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<bool> vb;

int N;
const int INF = int(1e9);
int rev(int n) {
  int r = 0;
  while (n) {
    r = r * 10 + (n % 10);
    n /= 10;
  }
  return r;
}
bool vis[1000010];
int memo[1000010];
int dp(int n) {
  vis[n] = 1;
  int R = rev(n);
  if (n == N) return memo[n] = 1;
  if (n > N) return memo[n] = INF;
  if (memo[n] + 1) return memo[n];
  int a, b;
  if (!vis[R] && R > n) a = dp(R);
  else {
    if (memo[R] != -1) a = memo[R]; 
    else a = INF; 
  }
  if (!vis[n + 1]) b = dp(n + 1);
  else {
    if (memo[n + 1] != -1) b = memo[n + 1];
    else b = INF;
  }
  return memo[n] = 1 + min(a, b);
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("in.txt", "r", stdin); 
  freopen("out.txt", "w", stdout); 
#endif
   int t; 
   scanf("%d", &t); 
   for(int cs = 1; t--; cs++) {
    memset(vis, 0, sizeof vis); 
    memset(memo, -1, sizeof memo); 
    cin >> N; 
    printf("Case #%d: %d\n", cs, dp(1)); 
   }
} 