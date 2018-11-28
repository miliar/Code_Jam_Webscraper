#include <bits/stdc++.h>

using namespace std;

int check(string s) {
  for(int i = 0;i < s.length();i++) {
    if(s[i] == '-')
      return 0;
  }
  return 1;
}

void solve() {
  string s; cin>>s;
  int ans = 0;
  while(!check(s)) {
    if(s[0] == '+') {
      int flag = 0;
      int e = 0;
      for(int i = s.length() - 1;i >= 0;i--) {
        if(s[i] == '-')
          flag = 1;
        else if(flag) {
          e = i;
          break;
        }
      }
      int st = 0;
      while(st <= e) {
        swap(s[st],s[e]);
        s[st] = s[st] == '+' ? '-' : '+';
        if(e > st)s[e] = s[e] == '+' ? '-' : '+';
        st++;
        e--;
      }
    }
    else {
      int e = 0;
      for(int i = s.length() - 1;i >= 0;i--) {
        if(s[i] == '-') {
          e = i;
          break;
        }
      }
      int st = 0;
      while(st <= e) {
        swap(s[st],s[e]);
        s[st] = s[st] == '+' ? '-' : '+';
        if(e > st) s[e] = s[e] == '+' ? '-' : '+';
        st++;
        e--;
      }
    }
    ans++;
  }
  cout<<ans<<endl;
}

int main() {
  assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
  int t; cin>>t;
  for(int i = 1;i <= t;i++) {
    cerr<<"Executing Case #"<<i<<endl;
    cout<<"Case #"<<i<<": ";
    solve();
  }

}
