#include <algorithm>
#include <cstdio>
#include <string>
using namespace std;

int main() {
  int nb_tests;
  scanf("%d", &nb_tests);
  for (int test = 1; test <= nb_tests; ++test) {
    int nb_carres, nb_lins, nb_cols;
    scanf("%d%d%d", &nb_carres, &nb_lins, &nb_cols);
    printf("Case #%d: ", test);
    string ans = "<null>";
    if ((nb_lins * nb_cols) % nb_carres != 0) ans = ("RICHARD");
    else if (nb_carres <= 2) ans = ("GABRIEL");
    else if (nb_carres == 3) {
      if (nb_lins == 3 && nb_cols == 1) ans = ("RICHARD");
      else if (nb_lins == 1 && nb_cols == 3) ans = ("RICHARD");
      else ans = ("GABRIEL");
    }
    else if (nb_carres == 4) {
      if (nb_lins == 4 && nb_cols == 3) ans = ("GABRIEL");
      else if (nb_lins == 3 && nb_cols == 4) ans = ("GABRIEL");
      else if (nb_lins == 4 && nb_cols == 4) ans = ("GABRIEL");
      else ans = ("RICHARD");
    }
    puts(ans.c_str());
  }
  return 0;
}


