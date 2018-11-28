#include <cstdio>
#include <bitset>

using namespace std;

int main() {

  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    bitset<16> res;
    for (int r = 0; r < 2; r++) {
      int ans;
      scanf("%d", &ans);
      for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) {
          int cur;
          scanf("%d", &cur);
          if (r == 0 && i == ans)
            res[cur-1] = true;
          else if (r == 1 && i != ans)
            res[cur-1] = false;
        }
    }
    printf("Case #%d: ", t);
    if (res.none())
      puts("Volunteer cheated!");
    else if (res.count() > 1)
      puts("Bad magician!");
    else
      for (int i = 0; i < 16; i++)
        if (res[i])
          printf("%d\n", i+1);
  }

  return 0;
}
