#include <iostream>
#include <stack>

using namespace std;


int check_plus_suffix(string s) {
  int res = s.size();
  while(res > 0) {
    if (s[res-1] == '+') {
      res--;
    } else {
      break;
    }
  }
  return res;
}

int check_minus_prefix(string s){
  int i = 0;
  for(int len = s.size(); i < len && s[i] == '-'; i++);
  return i;
}

int check_plus_prefix(string s){
  int i = 0;
  for(int len = s.size(); i < len && s[i] == '+'; i++);
  return i;
}

string flip_top_n(string s, int n) {
  string tmp = s.substr(n);
  stack<char> st;
  for(int i = 0; i < n; i++) {
    st.push(s[i]);
  }
  string rev = "";
  while(st.size()) {
    char c = st.top();
    st.pop();
    c = c == '-' ? '+' : '-';
    rev.push_back(c);
  }
  return rev + tmp;
}

int main() {
  freopen("./B-large.in", "r", stdin);
  freopen("./B-large.out", "w+", stdout);
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    string s;
    cin >> s;
    uint64_t cnt = 0;
    //All characters are "+"
    while(s.size()) {
      int suffix = check_plus_suffix(s);
      if (!suffix) {
        printf("Case #%d: %llu\n", i, cnt);
        s = "";
      }
      if (suffix != s.size() - 1) {
        s = s.substr(0, suffix);
      }
      int prefix = check_minus_prefix(s);
      if (prefix != 0) {
        s = flip_top_n(s, prefix);
      } else {
        s = flip_top_n(s, check_plus_prefix(s));
      }
      cnt++;
    }
  }
  return 0;
}
