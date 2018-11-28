#include <iostream>
#include <sstream>
#include <unordered_set>
#include <string>
#include <algorithm>
using namespace std;

int main() {
  cin.sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int N;
    cin >> N >> ws;
    unordered_set<string> eng, french;
    unordered_set<string> common;
    string engsen, frenchsen;
    getline(cin, engsen);
    getline(cin, frenchsen);
    istringstream sin1(engsen);
    string input;
    while(sin1 >> input) {
      eng.insert(input);
    }
    istringstream sin2(frenchsen);
    while(sin2 >> input) {
      unordered_set<string>::iterator it = eng.find(input);
      if(it != eng.end()) {
        eng.erase(it);
        common.insert(input);
      } else {
        french.insert(input);
      }
    }
    unordered_set<string> s[20][2];
    for (int i = 0; i + 2 < N; i++) {
      string sen;
      getline(cin, sen);
      istringstream sin3(sen);
      while(sin3 >> input) {
        //cout << i << ": " << input << endl;
        if (common.find(input) != common.end()) {
          continue;
        }
        if (eng.find(input) == eng.end()) {
          s[i][0].insert(input);
        }
        if (french.find(input) == french.end()) {
          s[i][1].insert(input);
        }
      }
    }
    cout << "Case #" << cas << ": ";
    if (N == 2) {
      cout << common.size() << endl;
      continue;
    }
    N -= 2;
    int ans = 1e8;
    for (int flag = 0; flag < (1 << N); flag++) {
      unordered_set<string> engs;
      unordered_set<string> fras;
      unordered_set<string> com = common;
      for (int i = 0; common.size() < ans && i < N; i++) {
        //cout << flag << ": " << i << endl;
        if (flag & (1 << i)) {
          //cout << "ENG" << endl;
          for(unordered_set<string>::iterator it = s[i][0].begin(); it != s[i][0].end(); it++) {
            engs.insert(*it);
          }
        } else {
          //cout << "FRA" << endl;
          for(unordered_set<string>::iterator it = s[i][1].begin(); it != s[i][1].end(); it++) {
            fras.insert(*it);
          }
        }
      }
      for (unordered_set<string>::iterator it = engs.begin(); it != engs.end(); it++) {
        if (fras.find(*it) != fras.end() || french.find(*it) != french.end()) {
          com.insert(*it);
        }
      }
      for (unordered_set<string>::iterator it = fras.begin(); it != fras.end(); it++) {
        if (engs.find(*it) != engs.end() || eng.find(*it) != eng.end()) {
          com.insert(*it);
        }
      }
      //cout << flag << ": " << common.size() << endl;
      ans = min(ans, (int)com.size());
    }
    cout << ans << endl;
  }
}
