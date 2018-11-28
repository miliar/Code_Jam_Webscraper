#include <iostream>
using namespace std;

const int XXX = 110;
int N, M;
int a[XXX][XXX], b[XXX][XXX];
int rowmax[XXX], colmax[XXX];

string compare() {
  for (int i = 1; i <= N; i++)
    for (int j = 1; j <= M; j++)
      if (a[i][j] != b[i][j])
        return "NO";
  return "YES";
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> N >> M;
    for (int i = 1; i <= N; i++)
      for (int j = 1; j <= M; j++)
        cin >> a[i][j];
    for (int i = 1; i <= N; i++) {
      rowmax[i] = 0;
      for (int j = 1; j <= M; j++)
        if (a[i][j] > rowmax[i])
          rowmax[i] = a[i][j];
    }
    for (int j = 1; j <= M; j++) {
      colmax[j] = 0;
      for (int i = 1; i <= N; i++)
        if (a[i][j] > colmax[j])
          colmax[j] = a[i][j];
    }

    for (int i = 1; i <= N; i++)
      for (int j = 1; j <= M; j++)
        b[i][j] = 100;
    for (int i = 1; i <= N; i++)
      for (int j = 1; j <= M; j++)
        if (b[i][j] > rowmax[i])
          b[i][j] = rowmax[i];
    for (int j = 1; j <= M; j++)
      for (int i = 1; i <= N; i++)
        if (b[i][j] > colmax[j])
          b[i][j] = colmax[j];

    cout << "Case #" << t << ": " << compare() << endl;
  }
  return 0;
}

