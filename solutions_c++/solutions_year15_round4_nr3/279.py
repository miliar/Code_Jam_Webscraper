#include <iostream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    map<string, int> mp;

    int N; cin >> N;
    string ln;
    getline(cin, ln);
    vector<vector<int> > A(N);
    for (int i = 0; i < N; i++) {
      getline(cin, ln);
      istringstream sin(ln);
      string word;
      while (sin >> word) {
        if (mp.find(word) == mp.end()) {
          int id = mp.size();
          mp[word] = id;
        }
        A[i].push_back(mp[word]);
      }
    }

    int result = mp.size();
    for (int i = 1; i < 1 << N; i += 4) {
      vector<int> R(mp.size());
      for (int j = 0; j < N; j++) {
        int v = i & 1 << j ? 1 : 2;
        for (int k = 0; k < A[j].size(); k++) {
          R[A[j][k]] |= v;
        }
      }
      int res = 0;
      for (int j = 0; j < R.size(); j++) {
        if (R[j] == 3) {
          res++;
        }
      }
      result = min(result, res);
    }

    cout << "Case #" << t << ": " << result << endl;
  }
  return 0;
}
