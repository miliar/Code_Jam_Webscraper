#include <bits/stdc++.h>
using namespace std;
string s;

int main(){
   int t, y, ans;
   cin >> t;
   y = t;
   while(t--){
      cin >> s;
      int n = s.length();
      int x = n;
      for(int i=n-1;i>=0;i--){
         if(s[i] == '+')
            x--;
         else
            break;
      }
      s  = s.substr(0, x);
      ans = 0;
      for(int i=0;i<x-1;i++){
         if(s[i]!=s[i+1])
            ans++;
      }
      ans++;
      if(s.length() == 0)
         ans = 0;
      cout << "Case #" << y-t << ": " << ans << endl;
   }
   return 0;
}