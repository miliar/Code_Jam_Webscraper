#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>

using namespace std;

int n;
int a[100][100];
vector <vector <int> > vv;

int ans[100];

inline bool check(){
  for (int col = 0; col < n; col ++){
    for (int raw = 1; raw < n; raw ++){
      if (vv[raw][col] <= vv[raw - 1][col]) return false;
    }
  }
  return true;
}

void brute(){
  for (int mask = 0; mask < (1 << (n + n)); mask ++) if (__builtin_popcount(mask) == n){
    vv.clear();
    for (int i = 0; i < n + n; i++) if ((mask >> i)&1){
      vector <int> v;
      for (int j = 0; j < n; j++) v.push_back(a[i][j]);
      vv.push_back(v);
    }
    sort(vv.begin(), vv.end());
    if (!check()) continue;
    
    int h[60] = {0};
    memset(h, 0, sizeof(h));

    for (int i = 0; i < n + n; i++) if (!((mask >> i)&1)){
      for (int col = 0; col < n; col++){
        bool flag = true;
        for (int raw = 0; raw < n; raw++)
          if (vv[raw][col] != a[i][raw]){
            flag = false; break;
          }
        if (flag && h[col] == 0){
          h[col] = 1; break;      
        }
      }
    }

    int cnt = 0;
    for (int i = 0; i < n; i++) if (h[i]) cnt++;
    if (cnt !=  n - 1) continue;
    
    vector <int> ans;
    for (int i = 0; i < n; i++) if (!h[i]){
      for (int j = 0; j < n; j++) ans.push_back(vv[j][i]);
    }
    //cout << ans.size() << endl;

    for (int i = 0; i < n; i++){
      if (i > 0) cout << ' ';
      cout << ans[i];
    }
    cout << endl;
    return;
  }
}

int main(){
  int t; cin >> t;
  for (int cas = 1; cas <= t; cas++){
    cin >> n;
    memset(a, 0, sizeof(a));
    //cout << n << endl;
    for (int i = 0; i < n + n - 1; i++){
      for (int j = 0; j < n; j ++){
        cin >> a[i][j]; 
        //cout << a[i][j] << ' ';
      }
      //cout << endl;
    }
    /*
    if (cas == 13){
      cout << n << endl;
      for (int i = 0; i < n + n - 1; i++){
          for (int j = 0; j < n; j++) cout << a[i][j] << ' ';
          cout << endl;
      }
    }
    */
    cout << "Case #" << cas << ": ";
    brute();
  } 
  return 0;
}
