#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int main() {
  int TC;
  scanf("%d", &TC);

  for (int TCi = 1; TCi <= TC; ++TCi) {
    printf("Case #%d: ", TCi);

    int ans1, ans2;
    int v1[4][4], v2[4][4];

    scanf("%d", &ans1);

    int i, j;

    for (i = 0; i < 4; ++i)
      for (j = 0; j < 4; ++j)
        scanf("%d", &v1[i][j]);

    scanf("%d", &ans2);

    for (i = 0; i < 4; ++i)
      for (j = 0; j < 4; ++j)
        scanf("%d", &v2[i][j]);

    --ans1, --ans2;

    // v1[ans1][0..3]
    // v2[ans2][0..3]

    vector<int> target;

    for (i = 0; i < 4; ++i) {
      int tmp = v1[ans1][i];
      for (j = 0; j < 4; ++j) {
        if (tmp == v2[ans2][j]) {
          target.push_back(tmp);
          break; // opt
        }
      }
    }

    if (target.size() == 1)
      printf("%d\n", target[0]);
    else if (!target.size())
      puts("Volunteer cheated!");
    else
      puts("Bad magician!");

  }

  return 0;
}
