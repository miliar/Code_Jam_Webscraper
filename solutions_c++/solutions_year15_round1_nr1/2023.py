#include <bits/stdc++.h>
using namespace std;

const int INF = 1 << 29;

int n;
vector<int> v;
int ans[2];

void solve1(){
  ans[0] = 0;
  for(int i=0;i<n-1;i++){
    ans[0] += max(0, v[i]-v[i+1]);
  }
}

void solve2(){
  int maxv = 0;
  ans[1] = 0;
  for(int i=0;i<n-1;i++){
    maxv = max(maxv, v[i]-v[i+1]);
  }
  for(int i=0;i<n-1;i++){
    if(v[i] < maxv) ans[1] += v[i];
    else ans[1] += maxv;
  }
}

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    v.clear();
    cin >> n;
    for(int i=0;i<n;i++){
      int x;
      cin >> x;
      v.push_back(x);
    }
    solve1();
    solve2();
    cout << "Case #" << t << ": " << ans[0] << ' ' << ans[1] << endl;
  }
}
