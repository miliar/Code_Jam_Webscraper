//God & me
#include <bits/stdc++.h>
#define int long long
using namespace std;
const int maxn=1e6;
int n;
bool have[10];
string s;
void f(){
  reverse(s.begin(),s.end());
  for(auto &c:s)
    c = c == '+' ? '-' : '+';
}
void trim(){
  while(s.size() && s.back() == '+')
    s.pop_back();
}
main(){
  //ios::sync_with_stdio(0),cin.tie(0);
  int t;cin>>t;
  int T=0;
  while(t--){
    cout<<"Case #"<<++T<<": ";
    cin>>s;
    int ans=0;
    trim();
    while(s.size()){
      int ptr=0;
      while(ptr < s.size() && s[ptr] == '+')
	s[ptr++]='-';
      if(ptr)
	ans++;
      ans++,f();
      trim();
    }
    cout<<ans<<'\n';
  }
  return 0;
}
