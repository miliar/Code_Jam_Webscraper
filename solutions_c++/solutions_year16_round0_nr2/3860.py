#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main() {
  int n;
  cin>>n;
  for (int cas = 1; cas <= n; cas++) {
    string s;
    cin>>s;

    int ans = 0;

    string t;
    for (int i = 0; i < s.size(); i++) {
      if ((t.size() == 0) || (t.back() != s[i])) {
        t += s[i];
      }
    }

    ans += t.size();
    if (t.back() == '+') {
      ans -= 1;
    }

    cout << "Case #" << cas << ": " << ans << endl;
  }
}
