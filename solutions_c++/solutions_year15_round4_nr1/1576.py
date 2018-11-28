#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

vector<string> table;

int check(int i, int j) {
   if (table[i][j] == '^') {
      for (int k = i - 1; k >= 0; --k) if (table[k][j] != '.') return 0;

      for (int k = i + 1; k < table.size(); ++k) if (table[k][j] != '.') return 1;
      for (int k = j + 1; k < table[i].size(); ++k) if (table[i][k] != '.') return 1;
      for (int k = j - 1; k >= 0; --k) if (table[i][k] != '.') return 1;
   }
   else if (table[i][j] == 'v') {
      for (int k = i + 1; k < table.size(); ++k) if (table[k][j] != '.') return 0;
      
      for (int k = i - 1; k >= 0; --k) if (table[k][j] != '.') return 1;
      for (int k = j + 1; k < table[i].size(); ++k) if (table[i][k] != '.') return 1;
      for (int k = j - 1; k >= 0; --k) if (table[i][k] != '.') return 1;
   }
   else if (table[i][j] == '>') {
      for (int k = j + 1; k < table[i].size(); ++k) if (table[i][k] != '.') return 0;
      
      for (int k = i - 1; k >= 0; --k) if (table[k][j] != '.') return 1;
      for (int k = i + 1; k < table.size(); ++k) if (table[k][j] != '.') return 1;
      for (int k = j - 1; k >= 0; --k) if (table[i][k] != '.') return 1;
   }
   else if (table[i][j] == '<') {
      for (int k = j - 1; k >= 0; --k) if (table[i][k] != '.') return 0;
      
      for (int k = i - 1; k >= 0; --k) if (table[k][j] != '.') return 1;
      for (int k = i + 1; k < table.size(); ++k) if (table[k][j] != '.') return 1;
      for (int k = j + 1; k < table[i].size(); ++k) if (table[i][k] != '.') return 1;
   }
   return -1;
}

int solve() {
   // check infeasibility
   int ans = 0, C = table[0].size() - 1;
   for (int i = 0; i < table.size(); ++i)
      for (int j = 0; j < table[i].size(); ++j)
         if (table[i][j] != '.') {
            int sol = check(i, j);
            if (sol == -1) return -1;
            else ans += sol;
         }
   /*
   if (table[0][0] == '^' || table[0][0] == '<') ++ans;
   if (C && (table[0][C] == '^' || table[0][C] == '>')) ++ans;
   for (int i = 1; i < C; ++i) if (table[0][i] == '^') ++ans;
   for (int i = 1; i < (table.size() - 1); ++i) {
      if (table[i][0] == '<') ++ans;
      if (C && table[i][C] == '>') ++ans;
   }
   if (table.size() > 1) {
      if (table[table.size() - 1][0] == 'v' || table[table.size() - 1][0] == '<') ++ans;
      if (C && (table[table.size() - 1][C] == 'v' || table[table.size() - 1][C] == '>')) ++ans;
      for (int i = 1; i < C; ++i) if (table[table.size() - 1][i] == 'v') ++ans;
   }
   */
   return ans;
}

int main() {
   int T; cin >> T;
   for (int i = 1; i <= T; ++i) {
      int R, C; cin >> R >> C;
      table.clear(); table.reserve(R);
      for (int j = 0; j < R; ++j) {
         string str; cin >> str;
         assert (C == str.size());
         table.push_back(str);
      }
      int ans = solve();
      cout << "Case #" << i << ": ";
      if (ans < 0) cout << "IMPOSSIBLE";
      else cout << ans;
      cout << endl;
   }
   return 0;
}

