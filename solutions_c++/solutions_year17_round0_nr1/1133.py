#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pii pair<int,int>
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair

int Solve(){
  int n, k, ans = 0;
  string s;

  cin >> s >> k;
  n = s.size();

  for(int i = n - 1; i >= k - 1; i--){
    if(s[i] == '+')
      continue;

    ans++;

    for(int j = i, x = 0; j > -1 && x < k; j--, x++)
      if(s[j] == '+')
        s[j] = '-';
      else
        s[j] = '+';
  }

  for(int i = 0; i < n; i++)
    if(s[i] == '-'){
      ans = -1;
      break;
    }

  return ans;
}

int main(){
  int t;

  cin >> t;

  for(int k = 1; k <= t; k++){
    int ans = Solve();
    printf("Case #%d: ", k);
    if(ans == -1)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", ans);
  }

  return 0;
}
