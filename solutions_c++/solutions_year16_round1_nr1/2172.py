#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (size_t t = 0; t < T; ++t) {
    string S;
    cin >> S;
    vector<char> out;
    out.reserve(S.length());

    out.push_back(S[0]);

    for (size_t i = 1; i < S.length(); ++i) {
      if (S[i] >= out[0]) {
        out.insert(out.begin(), S[i]);
      } else {
        out.push_back(S[i]);
      }
    }

    cout << "Case #" << t + 1 << ": ";
    for (const auto &it : out) {
      cout << it;
    }
    cout << endl;
  }
  return 0;
}
