#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int toint(char c) {
  return static_cast<int>(c - '0');
}

int solve(string s) {
  const int n = s.size();
  vector<int> sum(n);
  vector<int> num(n);

  for (int i=0; i<n; i++) {
    num[i] = toint(s[i]);
  }
  sum[0] = num[0];
  for (int i=1; i<n; i++) {
    sum[i] = sum[i-1] + num[i];
  }
  int ans = 0;
  for (int i=1; i<n; i++) {
    if (sum[i-1] < i) ans = max(ans, i - sum[i-1]);
  }
  return ans;
}

int main(){
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    string s;
    int n;
    cin >>n >> s;
    int ans = solve(s);
    cout << "Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}
