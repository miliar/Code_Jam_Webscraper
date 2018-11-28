#include <iostream>
#include <array>
#include <string>
#include <algorithm>
using namespace std;

int solve(int Smax, string str) {
  int sum = 0, ptr = 0, ans = 0;
  for(auto c: str) {
    const int i = c - '0';
    if(sum<ptr) {
      ans += ptr - sum;
      sum += ptr - sum;
    }
    sum += i;
    ptr++;
  }
  return ans;
}

int main() {
  int T; cin >> T;
  for(int t=1;t<=T;++t) {
    int Smax; cin >> Smax;
    string str; cin >> str;
    const int ans = solve(Smax, str);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
