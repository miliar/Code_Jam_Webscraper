#include <iostream>
#include <cstring>
using namespace std;

int main() {
  int T; cin >> T;
  int N, M;
  int heights[100][100];
  int rowMax[100], colMax[100];
  for (int caseNum = 1; caseNum <= T; ++caseNum) {
    memset(rowMax, 0, sizeof(rowMax));
    memset(colMax, 0, sizeof(colMax));
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        cin >> heights[i][j];
        rowMax[i] = max(rowMax[i], heights[i][j]);
        colMax[j] = max(colMax[j], heights[i][j]);
      }
    }
    bool works = true;
    for (int i = 0; i < N && works; ++i) {
      for (int j = 0; j < M && works; ++j) {
        if (heights[i][j] != rowMax[i] && heights[i][j] != colMax[j]) {
          works = false;
        }
      }
    }
    cout << "Case #" << caseNum << ": " << (works ? "YES" : "NO") << endl;
  }
}
