#include <bits/stdc++.h>
#define forn(n, i) for (int i=0; i<n; i++)
typedef long long LL;
using namespace std;
void solve(){
  int R, C, W;
  int ans = 0;
  cin >> R >> C >> W;
  ans += C / W;
  if (C % W != 0) ans++;
  ans *= R;
  cout << ans + W -1  << std::endl;
  return;
}

int main(){
  int T, i;
  scanf("%d", &T);
  for (i = 1; i<=T; ++i ){
    std::cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
