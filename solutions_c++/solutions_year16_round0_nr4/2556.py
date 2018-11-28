#include <bits/stdc++.h>
typedef long long ll;

using namespace std;





int main() {
  ios_base::sync_with_stdio(false);
  ll k,c,s;
  int t;
  cin >> t;
  for (int i=0; i< t; i++) {
    cin >> k>> c >> s;
    cout << "Case #"<<i+1<<": ";
    ll pos =1;
    ll step = pow(k,c-1);
    for (int l= 0; l< s; l++)
    {
      cout << pos<<" ";
      pos += step;
    }
    cout <<endl;
  }    
  return 0;
}

