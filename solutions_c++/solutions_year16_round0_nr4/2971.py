#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;

int main(){
  ios_base::sync_with_stdio(0);
  ll t, k, c, s, block;
  cin >> t;
  for(int i = 1; i <= t; ++i){
    cin >> k >> c >> s;
    block = pow(k, c - 1);
    cout << "Case #" << i << ": ";
    for(int i = 0; i < s; ++i)
      cout << 1 + i*block << " \n"[i == s - 1];
  }

  return 0;
}
