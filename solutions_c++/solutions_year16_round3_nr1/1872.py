#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool check(vector<int> p, int j, int k, int sum) {
  if (p[k] == 0 && p[j] == 0) return false;
  if (p[j] > 0) {
    p[j]--;
    sum--;
  }
  if (p[k] > 0) {
    p[k]--;
    sum--;
  }
  if (p[j] == 1 && sum == 1) return true;
  if (p[k] == 1 && sum == 1) return true;
  bool t = true;
  for (int i = 0; i < p.size(); i++) {
    if (p[i] > (sum/2)) {
      t = false;
    }
  }
  return t;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n;
    cin >> n;
    vector<int> p(n);
    int sum = 0;
    for (int j = 0; j < n; j++) {
      cin >> p[j];
      sum += p[j];
    }
    string ans = "";
    while(true) {
      bool finish = false;
      for (int k = 0; k < n; k++) {
        for (int l = 0; l < n; l++) {
          if (check(p, k, l, sum)) {
            if (p[k] != 0) {
              sum--;
              p[k]--;
              ans.push_back('A' + k);
            }
            if (p[l] != 0) {
              sum--;
              p[l]--;
              ans.push_back('A' + l);
            }
            ans.push_back(' ');
            if (sum == 0) finish = true;
          }
        }
      }
      if (finish) break;
    }
    cout << "Case #" << i+1 << ": " << ans << endl;
    
  }
  
  


  return 0;
}
