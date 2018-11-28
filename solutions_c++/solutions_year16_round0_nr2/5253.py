#include <bits/stdc++.h>
using namespace std;

int t;
string s;

int main(){

  cin >> t;
  for(int c = 1; c <= t; c++){
    cin >> s;
    s += '+';

    int i = 0, ans = 0;
    int n = s.size();
    if(s[0] == '-'){
      ans = 1;
      while(i < n && s[i] == '-') i++;
    }

    while(i < n){
      while(i < n && s[i] == '+') i++;
      if(i == n) break;

      while(i < n && s[i] == '-') i++;
      ans+=2;
    }
    cout << "Case #" << c << ": " << ans << endl;
  }

  return 0;
}
