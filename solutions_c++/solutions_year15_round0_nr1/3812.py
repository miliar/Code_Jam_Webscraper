#include <bits/stdc++.h>
using namespace std;

#define INF 2000000000
#define MOD 1000000007

typedef long long LL;
typedef pair<int, int> ii;

const int N = 1005; 

int main() { 
  int T, qq;
  for(cin >> T, qq = 1; qq <= T; ++qq) {
    printf("Case #%d: ", qq);
    int req, idx, ans = 0, sum;
    string sshy;
    vector<int> shy;
    cin >> req;
    cin >> sshy;
    for(char c : sshy) shy.push_back(c - '0');
    while(req > 0) {
      for(idx = 0, sum = 0; idx < req && sum < req; ++idx) {
        sum += shy[idx];
      }
      if(sum < req) {
        ans += req - sum;
        shy[0] += req - sum;
      }
      //cerr << "\n" << req << " " << idx << " " << sum  << " ans = " << ans;
      req = idx - 1;
    }
    cout << ans << "\n";
  }
  
  return 0;
}

