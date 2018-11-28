
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll power(ll a,ll b) {
  ll res = 1;
  while(b) {
    if(b&1) res = res*a;
    a = a*a;
    b >>= 1;
  }
  return res;
}

int main() {
  freopen("D-small-attempt0.in","r",stdin);
  freopen("ans.txt","w",stdout);
  int TC;
  ll K,C,S;
  cin >> TC;
  for(int cas=1;cas<=TC;cas++) {
    printf("Case #%d: ",cas);
    cin >> K >> C >> S;
    cout << 1 << " ";
    for(ll i=1;i<K;i++) {
        cout << i*power(K,C-1)+1 << " ";
    }
    cout << endl;
  }
  return 0;
}
