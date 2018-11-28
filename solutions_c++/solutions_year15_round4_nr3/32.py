#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

main() {
  int T, prob=1;
  string line;
  getline(cin, line);
  T = atoi(line.c_str());
  while (T--) {
    getline(cin, line);
    int N = atoi(line.c_str());
    map<string, vector<int> > m;
    for (int i = 0; i < N; i++) {
      getline(cin, line);
      istringstream sin(line);
      string s;
      while (sin >> s) {
        m[s].push_back(i);
      }
    }
    int ret = 0;
    for (int b = 0; b < (1<<N); b++) if (!(b&1) && (b&2)) {
      int cur = 0;
      for (auto it = m.begin(); it != m.end(); ++it) {
        bool at = false, bt = false;
        for (int i = 0; i < it->second.size(); i++) {
          if (b&(1<<it->second[i])) {
            at = true;
          } else {
            bt = true;
          }
        }
        cur += (!at || !bt);
      }
      ret = max(ret, cur);
    }
    cout << "Case #" << prob++ << ": " << m.size()-ret << endl;
  }
}
