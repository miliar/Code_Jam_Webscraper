#include <bits/stdc++.h>
using namespace std;
map<int, long long>mp;
void solve(int tc){
  printf("Case #%d: ", tc);
  int n;
  scanf("%d", &n);
  if(n == 0)printf("INSOMNIA\n");
  else if(mp.count(n))printf("%lld\n", mp[n]);
  else{
    unordered_set<int>st;
    int cnt = 0;
    long long ans;
    int x;
    int now = 1;
    while(cnt < 10){
      long long cur = n*now++;
      ans = cur;
      while(cur){
        x = cur%10;
        cur/=10;
        if(!st.count(x)){
          cnt++;
          st.insert(x);
        }
      }
    }
    mp[n] = ans;
    printf("%lld\n", ans);
  }
}
int main(){
  int tc;
  scanf("%d", &tc);
  for(int i = 1; i <= tc; i++)solve(i);
}