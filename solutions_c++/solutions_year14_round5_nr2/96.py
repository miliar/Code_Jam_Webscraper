#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define MAXP 1111
#define MAXH 222

int DP[2][MAXP];
int DQ[11][MAXP][MAXH];

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    int mystr, towerstr, N;
    scanf("%d%d%d", &mystr, &towerstr, &N);
    vector<int> H(N), G(N);
    for (int i = 0; i < N; i++) scanf("%d%d", &H[i], &G[i]);

    for (int p = 0; p < MAXP; p++) DP[0][p] = DP[1][p] = -1;
    DP[0][1] = 0;

    for (int m = 0; m < N; m++) {
      int om = m%2; int nm = 1-om;

      for (int turn = 0; turn < 11; turn++) for (int p = 0; p < MAXP; p++) for (int h = 0; h < MAXH; h++) DQ[turn][p][h] = -1;

      for (int p = 0; p < MAXP; p++) if (DP[om][p] != -1) {
//        fprintf(stderr, "DP[%d][%d] = %d\n", m, p, DP[om][p]);
        for (int r = 0; r <= p; r++) {
          int uh = H[m] - mystr * r;
          if (uh <= 0) {
            DP[nm][p-r] = max(DP[nm][p-r], DP[om][p] + G[m]);
            break;
          }
          DQ[0][p-r][uh] = max(DQ[0][p-r][uh], DP[om][p]);
        }
      }

      for (int turn = 0; turn < 10; turn++) {
        for (int p = 0; p < MAXP; p++) for (int h = 0; h < MAXH; h++) if (DQ[turn][p][h] != -1) {
          int me = DQ[turn][p][h];
          int nh = h - towerstr;
          if (nh <= 0) {
            DP[nm][p+1] = max(DP[nm][p+1], me);
          } else {
            DQ[turn+1][p+1][nh] = max(DQ[turn+1][p+1][nh], me);
            if (nh-mystr <= 0) {
              DP[nm][p] = max(DP[nm][p], me + G[m]);
            } else {
              DQ[turn+1][p][nh-mystr] = max(DQ[turn+1][p][nh-mystr], me);
            }
          }
        }
      }
    }

    int result = 0;
    for (int p = 0; p < MAXP; p++) result = max(result, DP[N%2][p]);

    printf("Case #%d: %d\n", tc, result);
    fflush(stdout);
  }
}
