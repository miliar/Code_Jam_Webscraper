#include <iostream>
#include <string>

using namespace std;

//The very smallest value needs to go at the front. if you get a 

int main() {
  ios::sync_with_stdio(false);
  
  int k;
  cin >> k;
  int m = k;
  
  while (k--) {
    string x;
    cin >> x;
    
    string ans;
    
    for (char c : x) {
      // cout << c << endl;
      
      if (ans.length() == 0) {
        ans += c;
      } else {
        if (c >= ans[0]) {
          ans = c + ans;
        } else {
          ans = ans + c;
        }
      }
    }
    
    cout << "Case #" << m-k << ": " << ans << endl;
  }
  
  return 0;
}