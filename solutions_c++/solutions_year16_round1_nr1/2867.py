#include <iostream>
#include <deque>

using namespace std;

int main() {
  int T;
  freopen("./A-large.in", "r", stdin);
  freopen("./A-large.out", "w+", stdout);
  cin >> T;
  for(int i = 1; i <= T; i++) {
    string s;
    cin >> s;
    deque<char> answer;
    answer.push_back(s[0]);
    for(int j = 1, len = s.length(); j < len; j++) {
      if ((int) s[j] >= (int) answer[0]) {
        answer.push_front(s[j]);
      } else {
        answer.push_back(s[j]);
      }
    }
    string ans;
    for(int j = 0, len = answer.size(); j < len; j++) {
      ans += answer[j];
    }
    printf("Case #%d: ", i);
    cout << ans << endl;
  }
}
