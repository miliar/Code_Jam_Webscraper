#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;
const int INF = 2e9;
typedef pair<int, int> ii;

const int N = 1e5 + 5; 

int main() { 
  int T;
  cin >> T;
  for(int qq = 1; qq <= T; ++qq) {
    printf("Case #%d: ", qq);
    string st;
    cin >> st;
    auto last = unique(st.begin(), st.end());
    st.erase(last, st.end());
    //cerr << st << "\n";
    reverse(st.begin(), st.end());
    int ans = 0;
    stack<char> s;
    for(char e : st) s.push(e);
    while(s.size() > 1) {
      char x, y;
      x = s.top();
      s.pop();
      y = s.top();
      if(x == y) continue;
      if(x == '+' && y == '-') {
        ans += 2;
        s.pop();
        s.push('+');
      } else if(x == '-' && y == '+') {
        ans++;
      }
    }
    if(s.top() == '-') ++ans;
    cout << ans << "\n";
  }
  
  return 0;
}

