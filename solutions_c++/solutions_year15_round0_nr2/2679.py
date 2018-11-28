#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;


int solve() {
  int n;
  cin >> n;
  vector<int> input;
  for(int i=0; i<n; i++) {
    int p;
    cin >> p;
    input.push_back(p);
  }
  int ans = 10000;
  
  for(int z=1; z<=1010; z++) {
    int cnt = 0;
    for(int i=0; i<n; i++) {
      cnt += input[i] / z + ( (input[i] % z) > 0);
    }
    ans = min(ans, z+cnt-n);
  }
  return ans;
  
}

int main() {
  int n;
  cin >> n;
  for(int i=0; i<n; i++) {
    int ans = solve();
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  
  return 0;
}
