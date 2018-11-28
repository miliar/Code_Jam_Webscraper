#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

int main(){ IO;
  int t;
  cin >> t;

  for(int ncase = 1; ncase <= t; ++ncase){
    int smax;
    string audience;
    cin >> smax >> audience;

    int ans = 0;
    int accum = 0;

    for(int k = 0; k <= smax; ++k){
      int cnt = audience[k] - '0';
      if(cnt > 0 and accum < k){
        int friends = k - accum;
        accum += friends;
        ans += friends;
      }
      accum += cnt;
    }

    cout << "Case #" << ncase << ": " << ans << endl;
  }

  return 0;
}
