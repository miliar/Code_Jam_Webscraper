#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
  int nb_tests;
  scanf("%d", &nb_tests);
  for (int test = 1; test <= nb_tests; ++test) {
    int niveau_max;
    scanf("%d", &niveau_max);
    int nb_avant = 0;
    int nb_amis = 0;
    for (int niveau = 0; niveau <= niveau_max; ++niveau) {
      int nb_type;
      scanf("%1d", &nb_type);
      if (nb_avant < niveau) {
        nb_amis += niveau - nb_avant;
        nb_avant = niveau;
      }
      nb_avant += nb_type;
    }
    printf("Case #%d: %d\n", test, nb_amis);
  }
  return 0;
}
