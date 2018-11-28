#include <iostream>
#include <sstream>
#include <vector>
#include <map>
using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N; cin >> N;
    map<string, int> wordID;
    vector<int> sentences[211];
    string s; getline(cin, s);
    for (int i = 0; i < N; i++) {
      getline(cin, s);
      istringstream ss(s);
      string str;
      while (ss >> str) {
        auto it = wordID.find(str);
        if (it == wordID.end()) {
          it = wordID.insert(make_pair(str, wordID.size())).first;
        }
        sentences[i].push_back(it->second);
      }
    }

    int ans = 0;
    bool e[3111];
    bool f[3111];
    for (int i = 0; i < (1<<(N-2)); i++) {
      memset(e, 0, sizeof e);
      memset(f, 0, sizeof f);
      for (auto it : sentences[0]) {
        e[it] = true;
      }
      for (auto it : sentences[1]) {
        f[it] = true;
      }
      for (int j = 2; j < N; j++) {
        bool use = i & (1<<(j-2));
        for (auto it : sentences[j]) {
          if (use) {
            e[it] = true;
          } else {
            f[it] = true;
          }
        }
      }
      int cnt = 0;
      for (int j = 0; j < wordID.size(); j++)
        if (e[j] ^ f[j]) cnt++;
      ans = max(ans, cnt);
    }
    printf("Case #%d: %d\n", t, wordID.size() - ans);
  }
}
