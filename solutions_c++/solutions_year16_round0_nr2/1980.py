#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int to_num(string s) {
  int r = 0;
  for(int i = 0; i < s.size(); i++) {
    r *= 2;
    if(s[i] == '+') r += 1;
  }
  return r;
}

string from_num(int num, int n) { 
  string s;
  for(int i = 0; i < n; i++) {
    if(num % 2 == 1) {
      s = "+" + s;
    }else{
      s = "-" + s;
    }
    num /= 2;
  }
  return s;
}

int solve(string s) {
  vector<int> cost(1 << s.size(), -1);
  cost[to_num(s)] = 0;
  queue<string> que;
  que.push(s);
  while(!que.empty()) {
    s = que.front(); que.pop();
    int current = cost[to_num(s)];
    for(size_t i = 1; i <= s.size(); i++) {
      string t = s;
      reverse(t.begin(), t.begin() + i);
      for(size_t j = 0; j < i; j++) {
        t[j] = (t[j] == '+') ? '-' : '+';
      }
      if(cost[to_num(t)] == -1) {
        cost[to_num(t)] = current + 1;
        que.push(t);
      }
    }
  }
  return cost[cost.size() - 1];
}

int main() {
  int T;
  cin >> T;
  for(int caze = 1; caze <= T; caze++) {
    cout << "Case #" << caze << ": ";
    string s;
    cin >> s;
    cout << solve(s) << endl;
  }
}
