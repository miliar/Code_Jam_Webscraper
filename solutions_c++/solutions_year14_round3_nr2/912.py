#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int testcase = 1; testcase <= T; ++testcase) {
    int N;
    cin >> N;
    
    vector<int> idx(N);
    vector<string> c(N);
    for (int i = 0; i < N; ++i) {
      cin >> c[i];
      idx[i] = i;
    }

    long long ans = 0;
    do {
      string s;
      for (int i = 0; i < N; ++i)
        s += c[idx[i]];

      char c = '0';
      string t;
      for (unsigned int i = 0; i < s.size(); ++i) {
        if (s[i] != c) {
          c = s[i];
          t += string(1, c);
        }
      }

      vector<int> count(26, 0);
      for (unsigned int i = 0; i < t.size(); ++i)
        ++count[t[i] - 'a'];

      bool valid = true;
      for (unsigned int i = 0; i < count.size(); ++i) {
        if (count[i] > 1)
          valid = false;
      }

      if (valid)
        ++ans;

    } while (next_permutation(idx.begin(), idx.end()));

    cout << "Case #" << testcase << ": " << ans << endl;
  }
  return 0;
}
