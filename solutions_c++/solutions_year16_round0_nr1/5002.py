#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    long long N;
    cin >> N;
    unordered_set<char> digits ({'0','1','2','3','4','5','6','7','8','9'});
    if (N == 0) {
      cout << "INSOMNIA" << endl;
    } else {
      long long count = 1;
      long long ans;
      while (!digits.empty()) {
        ans = N * count;
        count++;
        string nstr = to_string(ans);
        // cout << "ans : " << ans << endl;
        for (int j = 0; j < nstr.size(); j++) {
          unordered_set<char>::const_iterator got = digits.find (nstr[j]);
          if (got != digits.end()) {
            digits.erase(got);
          }
        }
      }
      cout << ans << endl;
    }
  }
  return 0;
}
