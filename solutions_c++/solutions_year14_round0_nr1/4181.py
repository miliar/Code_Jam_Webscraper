#include <cstdio>
#include <set>

void test(int caseNum) {
  int r1, r2;
  int b1[16], b2[16];
  scanf("%d", &r1);
  for (int i = 0; i < 16; ++i) scanf("%d", &b1[i]);
  scanf("%d", &r2);
  for (int i = 0; i < 16; ++i) scanf("%d", &b2[i]);
  std::set<int> cards;
  --r1; --r2;
  for (int i = r1 * 4; i < r1 * 4 + 4; ++i) {
    for (int j = r2 * 4; j < r2 * 4 + 4; ++j) {
      if (b2[j] == b1[i]) {
        cards.insert(b1[i]);
      }
    }
  } 
  printf("Case #%d: ", caseNum);
  if (cards.size() == 0) {
    printf("Volunteer cheated!\n");
  } else if (cards.size() == 1) {
    printf("%d\n", *cards.begin());
  } else {
    printf("Bad magician!\n");
  }
}
int main() {
  int numTest;
  scanf("%d", &numTest);
  for (int i = 0; i < numTest; ++i) {
    test(i+1);
  }
  return 0;
}