#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;
int main(int argc, char* argv[]) {
  freopen ("A-large.in", "r", stdin);
  freopen ("file.out", "w", stdout);
  int T;
  string w;
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    list<char> res;
    cout << "Case #" << t << ": "; // << "CAB";
    cin >> w;
    res.push_back(w[0]);
    for(int i = 1; i < w.size(); ++i) {
      if(w[i] >= res.front()) {
        res.push_front(w[i]);
      } else
        res.push_back(w[i]);
    }
    cout << string(res.cbegin(), res.cend()) << endl;
  }
  return 0;
}