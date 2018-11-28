#include <bits/stdc++.h>
using namespace std;

string s;
int t;

int main(){

  cin >> t;
  for(int c = 1; c <= t; c++){
    cin >> s;
    string ans = "";

    ans += s[0];
    for(int i = 1; i < s.size(); i++){
      if(s[i] >= ans[0]){
	ans = s[i]+ans;
      } else{
	ans += s[i];
      }
    }
    cout << "Case #"<< c << ": " << ans << endl;
  }

  return 0;
}
