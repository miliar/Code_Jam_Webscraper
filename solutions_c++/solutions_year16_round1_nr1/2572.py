#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <queue>

using namespace std;

int T;
deque<char> ans;
int main() {
  ios::sync_with_stdio(0);
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    string s;
    cin >> s;
    for(int i= 0; i < s.size(); ++i) {
      if(ans.empty()) {
        ans.push_back(s[i]);
      } else if(ans.front()<=s[i])
        ans.push_front(s[i]);
      else ans.push_back(s[i]);
    }
    cout << "Case #" << t << ": ";
    while(!ans.empty()) {
      cout << ans.front();
      ans.pop_front();
    }
    cout << "\n";
  }
  return 0;
}