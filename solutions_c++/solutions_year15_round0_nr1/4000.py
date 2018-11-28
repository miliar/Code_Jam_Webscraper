#include <bits/stdc++.h>

using namespace std;

int main(){
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int t;
  cin >> t;
  int tc = 1;
  while(t--){
    int n;
    string s;
    cin >> n >> s;
    int ans = 0;
    int curr = 0;
    for(int i=0;i<=n;i++){
      if( s[i] == 0 ) continue;
      if( curr < i ){
        ans += i-curr;
        curr += (i-curr);
      }
      curr += (s[i]-'0');
    }
    cout << "Case #" << tc++ << ": " << ans << endl;
  }
}
