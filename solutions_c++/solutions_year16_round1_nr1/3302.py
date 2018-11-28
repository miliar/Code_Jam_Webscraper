#include <iostream>
#include <cstring>

using namespace std;

int main()
{
  int T;
  string S, sf;

  cin >> T;

  for (int i = 0; i < T; ++i) {
    sf.clear();
    cin >> S;

    for (int j = 0; j < S.size(); ++j) {
      if (sf.size() == 0) {
        sf.push_back(S[j]);
      } else {
        if (sf[0] <= S[j]) {
          sf.insert(sf.begin(), S[j]);
        } else {
          sf.push_back(S[j]);
        }
      }
    }

    cout << "Case #" << i+1 << ": " << sf << endl;
  }

  return 0;
}
