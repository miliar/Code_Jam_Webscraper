#include <iostream>
#include <string>
using namespace std;

int T = 0;
void solve(){
  cin >> T;
  for (size_t k = 0; k < T; k++) {
    int ans = 0;
    int Smax = 0;
    string s;
    cin >> Smax;
    cin >> s;
    int sum = 0;
    for (size_t i = 0; i < s.size(); i++) {
      if (sum >= i) {
        //enough
      }
      else {
        ans += i - sum;
        sum = i;
      }
      sum += s[i] - '0';
    }
    cout << "Case #" << k+1 << ": " << ans << endl;
  }
}