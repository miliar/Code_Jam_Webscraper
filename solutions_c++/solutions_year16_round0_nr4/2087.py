#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

int main(){
  #ifdef MY_PC
  freopen("i", "r", stdin); freopen("o", "w", stdout);
  #endif
  int T;cin>>T;
  for (int t = 1; t <= T; ++t)
  {
    ll k,c,s,total=1,step=1;cin>>k>>c>>s;
    for (int i = 0; i < c; ++i) total*=k;
    if(k>1){
      step=total/(k-1);
      if(total%(k-1)==0)step--;
    }
    printf("Case #%d: ", t);
    ll cur=1;
    for (ll i = 0; i < k; ++i){
      cout<<cur<<" \n"[i==k-1];
      cur+=step;
    }
  }
}
  