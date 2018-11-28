#include<fstream>
#include<iostream>
#include<cstdio>

using namespace std;

#define FL(i, a, b) for(int i = a; i < b; i++)
#define MIN(a, b) ((a > b)? b : a)
#define MAX(a, b) ((a > b)? a : b)

int main(int argc, char *argv[]) {
  if (argc != 2)
    return -1;

  ifstream fin(argv[1]);

  int T, N, M;
  int lawn[110][110];
  int row_max[110];
  int col_max[110];
  fin>>T;
  FL(t, 0, T) {
    fin>>N>>M;
    FL(i, 0, N)
    FL(j, 0, M)
      fin>>lawn[i][j];

    FL(i, 0, N) {
      row_max[i] = -1;
      FL(j, 0, M)
        row_max[i] = MAX(row_max[i], lawn[i][j]);
    }
    FL(j, 0, M) {
      col_max[j] = -1;
      FL(i, 0, N)
        col_max[j] = MAX(col_max[j], lawn[i][j]);
    }

    bool ok = true;
    FL(i, 0, N) {
      FL(j, 0, M) {
        if (lawn[i][j] != MIN(row_max[i], col_max[j])) {
          ok = false;
          break;
        }
      }
      if (!ok)
        break;
    }

    printf("Case #%d: %s\n", t + 1, ok ? "YES": "NO");
  }
  return 0;
}
