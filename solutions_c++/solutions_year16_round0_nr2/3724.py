#include<bits/stdc++.h>

using namespace std;

int t;
string s;

int main(){
  cin.sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  
  ofstream cout ("output.txt");
  
  cin >> t;
  for(int T = 1; T <= t; T++){
    cin >> s;
    int n = s.size();
    int id = n-1, ans = 0;
    while(id >= 0 && s[id] == '+') id--;
    while(id >= 0){
      int p1 = 0, p2 = 0;
      while(id >= 0 && s[id] == '-') id--, p1++;
      while(id >= 0 && s[id] == '+') id--, p2++;
      ans += ((p1 != 0) + (p2 != 0));
    }
    cout << "Case #" << T << ": " << ans << '\n';
  }
  
  return 0;
}
