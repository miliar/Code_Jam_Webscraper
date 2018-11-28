#include <bits/stdc++.h>

using namespace std;

int main(){
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    int n, q;
    cin >> n >> q;
    cout << "Case #" << tc << ": " << endl;
    for (int i = 0; i < (1 << 16); i++) {
      if ((i & (1 << 0))  == 0) continue;
      if ((i & (1 << 15)) == 0) continue;
      int valid = 0;
      long long cnt = 0;
      string s = "";
      vector<long long> bin;
      for (int j = 0; j < 16; j++) 
        if (i & (1 << j)) s += "1";
        else s += "0";
      reverse(s.begin(), s.end());
      for (long long j = 2; j <=10; j++) {
        long long f = 1;
        for (int k = 0; k < 16; k++) {
          if (i & (1 << k)) cnt += f;
          f *= j;
        }
        for (long long k = 2; k <= sqrt(cnt); k++) {
          if (cnt % k == 0) {
            bin.push_back(k);
            break;
          }
        }
      }
      if (bin.size() == 9) {
        q--;
        cout << s << " ";
        for (int i = 0; i < 9; i++) cout << bin[i] << " ";
        cout << endl;
      }
      if (q == 0) break;
    }
  }
  return 0;
}
