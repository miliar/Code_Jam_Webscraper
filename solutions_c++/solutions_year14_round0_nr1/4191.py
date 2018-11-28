#include <iostream>
#include <set>

using namespace std;

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int Case = 1; Case <= nCases; ++Case) {
    set<int> candidates;
    int row;
    scanf("%d", &row);
    for (int r = 1; r <= 4; ++r) {
      for (int c = 1; c <= 4; ++c) {
        int x;
        scanf("%d", &x);
        if (r == row) {
          candidates.insert(x);
        }
      }
    }
    set<int> answer;
    scanf("%d", &row);
    for (int r = 1; r <= 4; ++r) {
      for (int c = 1; c <= 4; ++c) {
        int x;
        scanf("%d", &x);
        if (r == row) {
          if (candidates.find(x) != candidates.end()) {
            answer.insert(x);
          }
        }
      }
    }
    printf("Case #%d: ", Case);
    if (answer.size() == 0) {
      printf("Volunteer cheated!\n");
    } else if (answer.size() > 1) {
      printf("Bad magician!\n");
    } else {
      printf("%d\n", *answer.begin());
    }
  }
  return 0;
}
