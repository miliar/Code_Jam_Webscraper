#include <iostream>
using namespace std;

int main()
{
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int ans = 0;
    int smax;
    string s;
    cin >> smax >> s;
    int curt_num = s[0] - '0';
    // cin >> curt_num;
    for (int j = 1; j <= smax; ++j) {
      if (s[j] != '0' && curt_num < j) {
        // cout << "::" << j << endl;
        // cout << j - curt_num << endl;
        ans += j - curt_num;
        curt_num = j;
      }
      curt_num += s[j]-'0';
    }
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  return 0;
}
