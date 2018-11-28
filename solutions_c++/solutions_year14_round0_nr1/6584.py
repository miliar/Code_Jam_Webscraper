#include <bits/stdc++.h>
using namespace std;
int grid1[10][10];
int grid2[10][10];
void solve() {
  int r1;
  scanf("%d", &r1);
  r1--;
  set<int> candidates;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      scanf("%d", &grid1[i][j]);
      if (i == r1) {
        candidates.insert(grid1[i][j]);
      }
    }
  }
  int r2;
  scanf("%d", &r2);
  r2--;
  vector<int> answers;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      scanf("%d", &grid2[i][j]);
      if (i == r2) {
        if (candidates.count(grid2[i][j])) {
          answers.push_back(grid2[i][j]);
        }
      }
    }
  }
  if (answers.size() == 0) {
    printf("Volunteer cheated!\n");
  } else if (answers.size() > 1) {
    printf("Bad magician!\n");
  } else {
    printf("%d\n", answers[0]);
  }
}
int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
