#include <bits/stdc++.h>
using namespace std;

string s;
bool check(){
  for(auto i:s)if(i=='-')return 1;
  return 0;
}

void change(int idx){
  if(idx==-1)idx=s.size();
  reverse(s.begin(),s.begin()+idx);
  for (int i = 0; i < idx; ++i) s[i]=s[i]=='-'?'+':'-';
}

int main(){
  #ifdef MY_PC
  freopen("i", "r", stdin); freopen("o", "w", stdout);
  #endif
  int T,ans;cin>>T;
  for (int t = 1; t <= T; ++t)
  {
    cin>>s;
    for (ans = 0; check(); ++ans)
      if(s[0]=='+') change(s.find('-'));
      else change(s.find('+'));
    printf("Case #%d: %d\n", t,ans);
  }
}
  