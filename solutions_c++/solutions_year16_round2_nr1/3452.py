#include <bits/stdc++.h>

using namespace std;
string mas[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int main() {
    freopen("A-small-attempt3.in", "r", stdin);
    freopen("A-small-attempt3.out", "w", stdout);
  int T;
  string s;
  cin >> T;
  int massive[10] = {0, 6, 8, 2, 4, 3, 7, 5, 1, 9};
  for (int q = 0; q < T; q++) {
    cin >> s;
    vector<int> used(s.size(), 0);
    vector<int> ans;
    int ind = 0;
   while(ind <= 9) {int i = massive[ind];
        vector<int> Us(mas[i].size(), 0);
        vector<int> Vr(s.size(), 0);
        int cnt = 0;
     for (int j = 0; j < s.size(); j++) {
            if (used[j]) {continue;}
       for (int k = 0; k < mas[i].size(); k++) {
          if (mas[i][k] == s[j] && !Us[k]) {
             Us[k] = 1;
             Vr[j] = 1;
             cnt++;
             break;
          }
       }
       if (cnt == mas[i].size()) {break;}
        }
       // cout << cnt << endl;
        if (cnt == mas[i].size()) {
            ans.push_back(i);
            for (int j = 0; j < Vr.size(); j++) {
                if(Vr[j] == 1){used[j] = Vr[j];}
            }
        } else {ind++;}
     }
     cout << "Case #" << q + 1 << ":" << " ";
     sort(ans.begin(), ans.end());
     for (int t = 0; t < ans.size(); t++) {
        cout << ans[t];
     }
     cout << endl;
}

  return 0;
}
