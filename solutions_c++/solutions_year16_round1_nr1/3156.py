#include <iostream>

using namespace std;

int main() {
  int T; cin>>T;
  for (int t=1; t <= T; ++t) {
    string s; cin >> s;
    string ans = s.substr(0,1);

    for (size_t i = 1; i < s.size(); ++i) {
      if (s[i] >= ans[0]) ans = s[i] + ans;
      else ans += s[i];
    }
    printf("Case #%d: %s\n", t, ans.c_str());
  }

  return 0;
}
