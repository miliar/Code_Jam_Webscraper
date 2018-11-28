#include <bits/stdc++.h>

using namespace std;
string s;
int main() {
  ios::sync_with_stdio(false);
  int n, k, T, ans;
  cin >> T;
  for(int cs=1;cs<=T;cs++) {
    cin >> s >> k;
    n = s.length();
    ans = 0;
    for(int i=0;i<=n-k;i++) {
      if(s[i]=='-') {
	for(int j=i;j<i+k;j++) 
	  s[j] = ((s[j]=='-')?'+':'-');
	ans ++;
      }
    }
    bool f = false;
    for(int i=n-k;i<n;i++) {
      if(s[i]=='-') f = true; 
    }
    cout << "Case #" << cs << ": ";
    if(f) cout << "IMPOSSIBLE\n";
    else cout << ans << endl;
  }
}
