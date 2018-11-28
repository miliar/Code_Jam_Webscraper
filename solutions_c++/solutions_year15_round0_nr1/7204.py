#include<bits/stdc++.h>

using namespace std;

int main(){
  int T; cin >> T;
  for(int x = 1; x <= T; x++){
    int n; cin >> n;
    string s; cin >> s;
    int sum = 0, ans = 0;
    for(int i = 0; i < (int)s.length(); i++){
      if(s[i] == '0') continue;
      if(sum >= i){
        sum += s[i]-'0';
      }else{
        ans += i-sum;
        sum = i + s[i]-'0';
      }
    }
    cout << "Case #" << x << ": " << ans << endl;
  }
  return 0;
}
