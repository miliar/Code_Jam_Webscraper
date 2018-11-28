#include <bits/stdc++.h>

using namespace std;

void solve() {
  string s; cin>>s;
  string t;
  for(int i = 0;i < s.length();i++) {
    string a = t;
    a+=s[i];
    string b = "";
    b+=s[i];
    b+=t;
    if(a > b) {
      t = a;
    }
    else t = b;
  }
  cout<<t<<endl;
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
