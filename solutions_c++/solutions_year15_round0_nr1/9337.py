#include <iostream>
#include <string>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  
  for (int i = 0; i < T; i++) {
    int Smax;
    cin >> Smax;
        
    string s;
    cin >> s;

    int sum = 0, ans = 0;


    //cout << "\n\nCase " <<  i+1 << ":" << "\n";
    
    for (int j = 0; j < s.length(); j++) {
      if ( (s[j]-'0') == 0) continue;
      
      //cout << j << ": " << " sum: " << sum << ", ans " << ans << "\n";
      if (sum >= j) {
        sum  += s[j] - '0';
      } else {
        ans = ans + j - sum;
        sum = j + s[j] - '0';
      }
      //cout << j << ": " << " sum: " << sum << ", ans " << ans << "\n";
    }
    cout << "Case #" << i+1 << ": " << ans << "\n";
  }
  return 0;
}
