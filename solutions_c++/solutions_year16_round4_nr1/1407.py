// C++ 11
#include <cstdio>
#include <cstring>
#include <cassert>
#include <string>
#include <algorithm>
using namespace std;

int main() {
  static char strs[13][3][(1<<12)+1];
  strcpy(strs[0][0], "P");
  strcpy(strs[0][1], "R");
  strcpy(strs[0][2], "S");
  for(int i = 0; i < 12; ++i) {
    if(i & 1) {
      strcpy(strs[i + 1][0], strs[i][2]);
      strcat(strs[i + 1][0], strs[i][1]);
      strcpy(strs[i + 1][1], strs[i][2]);
      strcat(strs[i + 1][1], strs[i][0]);
      strcpy(strs[i + 1][2], strs[i][1]);
      strcat(strs[i + 1][2], strs[i][0]);
    } else {
      strcpy(strs[i + 1][0], strs[i][1]);
      strcat(strs[i + 1][0], strs[i][2]);
      strcpy(strs[i + 1][1], strs[i][0]);
      strcat(strs[i + 1][1], strs[i][2]);
      strcpy(strs[i + 1][2], strs[i][0]);
      strcat(strs[i + 1][2], strs[i][1]);
    }
  }
  int T; scanf("%d", &T);
  for(int ti = 0; ti < T; ++ti) {
    int N, R, P, S;
    scanf("%d%d%d%d", &N, &R, &P, &S);
    int avg = (1 << N) / 3;
    if(P < avg || R < avg || S < avg || P > avg+1 || R > avg+1 || S > avg+1) {
      printf("Case #%d: IMPOSSIBLE\n", ti + 1);
    } else if(R == S) {
      printf("Case #%d: %s\n", ti + 1, strs[N][0]);
    } else if(P == S) {
      printf("Case #%d: %s\n", ti + 1, strs[N][1]);
    } else {
      printf("Case #%d: %s\n", ti + 1, strs[N][2]);
    }
  }
  return 0;
}
