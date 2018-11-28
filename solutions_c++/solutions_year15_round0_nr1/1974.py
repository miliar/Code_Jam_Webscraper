#include<bits/stdc++.h>
using namespace std;

int go() {
  int sMax;
  string s;
  cin >> sMax >> s;
  vector<int> v;
  int sum = 0;
  int ans = 0;
  for(int i = 0; i < s.size(); ++i) {
    int x = s[i] - '0';
    for(int j = 0; j < x; ++j) {
      v.push_back(i);
    }
  }
  for(int x : v) {
    while(x > sum) {
      ++ans;
      ++sum;
    }
    ++sum;
  }
  return ans;
}

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; ++i) {
    printf("Case #%d: %d\n", i + 1, go());
  }
}
