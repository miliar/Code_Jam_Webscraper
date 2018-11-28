#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
  int T;
  string S;

  cin >> T;
  for (int k = 1; k <= T; k++) {
    cin >> S;
    vector<string> str;
    vector<string> q;
    string h = "";

    str.push_back(h + S[0]);

    for (int i = 1; i < S.length(); i++) {
      q.clear();
      for (int j = 0; j < str.size(); j++) {
        if (str[j].length() == i) {
          q.push_back(str[j] + S[i]);
          q.push_back(S[i] + str[j]);
        }
      }
      str.clear();
      for (int i =0; i < q.size(); i++) str.push_back(q[i]);
    }

    sort(str.begin(), str.end());
    cout << "Case #" << k << ": " << str[str.size() - 1] << endl;

  }



  return 0;
}