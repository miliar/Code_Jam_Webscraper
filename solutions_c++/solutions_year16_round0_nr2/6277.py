#include <bits/stdc++.h>
using namespace std;
void solve(int tc){
  string s;
  cin >> s;
  int cnt = 0;
  for(int i = 1; i < s.size(); i++){
    if(s[i] == '-' && s[i-1] == '+')cnt++;
  }
  int ans;
  if(s[0] == '-')ans = 1;
  else ans = 0;
  ans+=cnt*2;
  printf("Case #%d: %d\n", tc, ans);
}
int main(){
  int tc;
  scanf("%d", &tc);
  for(int i = 1; i <= tc; i++)solve(i);
}