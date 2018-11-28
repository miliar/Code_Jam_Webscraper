#include <bits/stdc++.h>

using namespace std;


int a[10][10];
int M[10][10];
int visited[10][10], revealed[10][10];
int n, m;

int dx[8] = {0, 0, -1, -1, -1, 1, 1, 1};
int dy[8] = {-1, 1, -1, 0, 1, -1, 0, 1};

int valid (int x, int y) {
      return (x >= 0 && x < n && y >= 0 && y < m);
}

void dfs (int x, int y) {
      if (M[x][y] != 0) return;

      visited[x][y] = true;
      revealed[x][y] = true;

      for (int d = 0; d < 8; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (valid (nx, ny) && a[nx][ny] == 0 && !visited[nx][ny]) {
                  dfs (nx, ny);
                  revealed[nx][ny] = true;
            }
      }
}

int main() {
      freopen ("input.txt", "r", stdin);
      freopen ("output.txt", "w", stdout);


      int T, caseNo = 1;
      cin >> T;

      while (T--) {
            cout << "Case #" << caseNo ++ << ":" << endl;

            int stars, sz;
            cin >> n >> m >> stars;

            sz = n * m;
            int done = false;

            for (int mask = 0; mask < (1 << sz); mask++) {
                  int tot = 0;
                  for (int j = 0; j < sz; j++) {
                        if (mask & (1 << j)) tot ++;
                  }

                  if (tot == stars) {
                        vector <int> values;
                        for (int i = 0; i < sz; i++) {
                              if (mask & (1 << i))
                                    values.push_back(1);
                              else values.push_back(0);
                        }

                        int cnt = 0;
                        for (int i = 0; i < n; i++)
                              for (int j = 0; j < m; j++)
                                    a[i][j] = values[cnt++];

                        // cal stars
                        memset (M, 0, sizeof (M));

                        for (int i = 0; i < n; i++)
                              for (int j = 0; j < m; j++) {
                                    int mines = 0;
                                    for (int d = 0; d < 8; d++) {
                                          int ni = i + dx[d];
                                          int nj = j + dy[d];

                                          if (valid (ni, nj) && a[ni][nj] == 1) {
                                                mines ++;
                                          }
                                    }

                                    M[i][j] = mines;
                              }

                        // do a dfs for each 0 cell
                        for (int i = 0; i <  n; i++)
                              for (int j = 0; j < m; j++) {
                                    if (a[i][j] == 0) {
                                          memset (visited, 0, sizeof (visited));
                                          memset (revealed, 0, sizeof (revealed));

                                          revealed[i][j] = true;
                                          dfs (i, j);

                                          int ok = true;

                                          for (int k = 0; k < n; k++) {
                                                for (int l = 0; l < m; l++)
                                                      if (revealed[k][l] == 0 && a[k][l] == 0) {
                                                            ok = false;
                                                            break;
                                                      }

                                                if (!ok) {
                                                      break;
                                                }
                                          }

                                          if (ok) {
                                                a[i][j] = 2;
                                                done = true;
                                                goto bpp;
                                          }
                                    }
                              }

                  }
            }

            bpp:
                  if (done) {
                        for (int i = 0; i < n; i++) {
                              for (int j = 0; j < m; j++) {
                                    if (a[i][j] == 1)
                                          cout << "*";
                                    else if (a[i][j] == 0)
                                          cout << ".";
                                    else cout << "c";
                              }

                              cout << endl;
                        }
                  } else {
                        cout << "Impossible" << endl;
                  }
      }

      return 0;
}
