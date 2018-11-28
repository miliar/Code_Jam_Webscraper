#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

const int maxn = 1005;

int main(){ IO;
  int t;
  cin >> t;

  for(int ncase = 1; ncase <= t; ++ncase){
    int d;
    cin >> d;

    int ans = 0;
    vector<int> cnt(maxn);

    for(int i = 0; i < d; ++i){
      int pi;
      cin >> pi;
      cnt[pi]++;
      ans = max(ans, pi);
    }

    for(int k = 1; k < maxn; ++k){
      int time = k;
      for(int i = 1; i < maxn; ++i){
        if(cnt[i]){
          time += cnt[i] * ((i + k - 1) / k - 1);
        }
      }

      ans = min(ans, time);
    }

    cout << "Case #" << ncase << ": " << ans << endl;
  }

  return 0;
}
