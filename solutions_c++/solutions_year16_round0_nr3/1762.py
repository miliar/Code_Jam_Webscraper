#include <bits/stdc++.h>
#include <bitset>

using namespace std;
#define ll long long

bool check(ll x, int b){
  ll m=0;
  for (int i = 0; i < 16; ++i) if(x>>i&1)m+=pow(b,i);
  vector<int>d={3, 2, 3, 2, 7, 2, 3, 2, 3};
  return m%d[b-2]==0;
}

int main(){
  #ifdef MY_PC
  freopen("i", "r", stdin); freopen("o", "w", stdout);
  #endif
  int T;cin>>T;
  for (int t = 1; t <= T; ++t)
  {
    printf("Case #%d:\n", t);
    ll n,k,start=1; cin>>n>>k;
    for (int i = 0; i < n-1; ++i) start*=2;
    if(start!=1)start++;
    while(k) {
      bool f=0;
      for (int j = 2; j <= 10; ++j) if(!check(start,j)){f=1;break;}
      if(!f){
        k--;
        cout<<(bitset<16>(start).to_string()).substr(16-n,n)<<" "<<"3 2 3 2 7 2 3 2 3\n";
      }
      start+=2;
    }
  }
}
  