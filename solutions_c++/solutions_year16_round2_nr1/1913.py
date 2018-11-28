#include <iostream>
#include <vector>

using namespace std;

int idx(char c) { return c - 'A'; }

void solve(string s) {
   vector<int> count(26, 0), num(10, 0);
   for (int i = 0; i < s.size(); ++i) ++count[idx(s[i])];
   // 0
   num[0] = count[idx('Z')];
   count[idx('Z')] -= num[0]; count[idx('E')] -= num[0]; count[idx('R')] -= num[0]; count[idx('O')] -= num[0];
   // 2
   num[2] = count[idx('W')];
   count[idx('T')] -= num[2]; count[idx('W')] -= num[2]; count[idx('O')] -= num[2];
   // 4
   num[4] = count[idx('U')];
   count[idx('F')] -= num[4]; count[idx('O')] -= num[4]; count[idx('U')] -= num[4]; count[idx('R')] -= num[4];
   // 6
   num[6] = count[idx('X')];
   count[idx('S')] -= num[6]; count[idx('I')] -= num[6]; count[idx('X')] -= num[6];
   // 8
   num[8] = count[idx('G')];
   count[idx('E')] -= num[8]; count[idx('I')] -= num[8]; count[idx('G')] -= num[8]; count[idx('H')] -= num[8]; count[idx('T')] -= num[8];
   // 1
   num[1] = count[idx('O')];
   count[idx('O')] -= num[1]; count[idx('N')] -= num[1]; count[idx('E')] -= num[1];
   // 3
   num[3] = count[idx('R')];
   count[idx('T')] -= num[3]; count[idx('H')] -= num[3]; count[idx('R')] -= num[3]; count[idx('E')] -= num[3]; count[idx('E')] -= num[3];
   // 5
   num[5] = count[idx('F')];
   count[idx('F')] -= num[5]; count[idx('I')] -= num[5]; count[idx('V')] -= num[5]; count[idx('E')] -= num[5];
   // 7
   num[7] = count[idx('V')];
   count[idx('S')] -= num[7]; count[idx('E')] -= num[7]; count[idx('V')] -= num[7]; count[idx('E')] -= num[7]; count[idx('N')] -= num[7];
   // 9
   num[9] = count[idx('I')];
   for (int i = 0; i < num.size(); ++i)
      for (int j = 0; j < num[i]; ++j) cout << i;
}

int main() {
   int T; cin >> T;
   for (int i = 1; i <= T; ++i) {
      string s; cin >> s;
      cout << "Case #" << i << ": ";
      solve(s); cout << endl;
   }
   return 0;
}

