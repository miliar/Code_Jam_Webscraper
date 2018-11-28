#include <bits/stdc++.h>
using namespace std;
#define ll long long
int solve(string);
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin>>t;
  for (int i=0; i<t; i++) {
    string s;
    cin>>s;
    int ans = solve(s);
    cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }
  return 0;
}
string reduce(string s) {
  string ss = "";
  ss += s[0];
  for (int i=1; i<s.size(); i++) {
    if (s[i] != s[i-1]) {
      ss += s[i];
    }
  }
  if (*(ss.rbegin()) == '+') ss.pop_back();
  return ss;
}
int solve(string s) {
  int i,j,k;
  string ss = reduce(s);
  if (ss.size() == 0) return 0;
  return ss.size();
}
