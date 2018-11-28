/*
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            pass System Test!
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template <typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<T> &v) {
  if (!v.empty()) {
    out << '[';
    std::copy(v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
    out << "\b\b]";
  }
  return out;
}
template <typename T1, typename T2>
std::ostream &operator<<(std::ostream &out, const std::pair<T1, T2> &p) {
  out << "[" << p.first << ", " << p.second << "]";
  return out;
}
template <class T, class U>
void chmin(T &t, U f) {
  if (t > f) t = f;
}
template <class T, class U>
void chmax(T &t, U f) {
  if (t < f) t = f;
}
template <typename T>
void uniq(vector<T> &v) {
  v.erase(unique(v.begin(), v.end()), v.end());
}

const vector<string> str_nums = {"ZERO", "ONE", "TWO",   "THREE", "FOUR",
                                 "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool dfs(string &S, int prev, vector<int> &cnt) {
  if (*max_element(cnt.begin(), cnt.end()) == 0) return true;
  for (int i = prev; i < 10; ++i) {
    bool ok = true;
    for (char c : str_nums[i])
      if (cnt[c - 'A'] == 0) ok = false;
    if (!ok) continue;

    for (char c : str_nums[i]) cnt[c - 'A']--;
    char digit = i + '0';
    S.push_back(digit);
    if (dfs(S, i, cnt)) return true;
    for (char c : str_nums[i]) cnt[c - 'A']++;
    S.pop_back();
  }
  return false;
}

string solve(const string &S) {
  vector<int> cnt(26, 0);
  for (int i = 0; i < S.size(); ++i) cnt[S[i] - 'A']++;

  string T = "";
  dfs(T, 0, cnt);
  return T;
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    string S;
    cin >> S;

    cout << "Case #" << testcase << ": ";
    cout << solve(S) << endl;
  }
}
