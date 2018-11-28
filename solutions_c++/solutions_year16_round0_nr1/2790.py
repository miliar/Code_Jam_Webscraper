#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main() {
  freopen("A-large (1).in","r",stdin);
  freopen("ans1.txt","w",stdout);
  int tc;
  ll N;
  cin >> tc;
  for(int cas=1;cas<=tc;cas++) {
    cin >> N;
    set<int> st;
    ll pos = -1;
    if(N == 0) {
        printf("Case #%d: %s\n",cas,"INSOMNIA");
        continue;
    }
    for(ll i=1;i<=1000100;i++) {
        ll n = N*i;
        while(n) {
          int d = n%10;
          n = n/10;
          st.insert(d);
        }
        if(st.size() == 10) {
            pos = i;
            break;
        }
    }
    if(pos != -1) {
      printf("Case #%d: %lld\n",cas,pos*N);
    }
    else {
      printf("Case #%d: %s\n",cas,"INSOMNIA");
    }

  }
  return 0;
}
