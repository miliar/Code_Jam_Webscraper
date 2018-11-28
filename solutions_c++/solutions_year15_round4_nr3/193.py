#include<cstdio>
#include<fstream>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<bitset>
#include<deque>
#include<queue>
#include<set>
#include<map>
#include<cmath>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<unordered_map>
#include<iostream>
using namespace std;

char board[110][110];
int cnt[110][110];
int n;
int main() {
  cin >> n;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) {
      cin >> board[i][j];
      if (board[i][j] == 'o') {
        if (i - 1 >= 0) cnt[i - 1][j]++;
        if (i + 1 < n) cnt[i + 1][j]++;
        if (j - 1 >= 0) cnt[i][j - 1]++;
        if (j + 1 < n) cnt[i][j + 1]++;
      }
    }
  bool ans = true;
  for (int i = 0; ans && i < n; i++)
    for (int j = 0; j < n; j++) {
      if (i - 1 >= 0) if (cnt[i - 1][j] & 1) ans = false;
      if (i + 1 < n) if (cnt[i + 1][j] & 1) ans = false;
      if (j - 1 >= 0) if (cnt[i][j - 1] & 1) ans = false;
      if (j + 1 < n) if (cnt[i][j + 1] & 1) ans = false;
      if (!ans) break;
    }
  cout << (ans ? "YES" : "NO") << endl;
  return 0;
}
