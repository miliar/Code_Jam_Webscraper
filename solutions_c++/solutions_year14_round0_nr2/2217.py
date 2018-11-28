#include <cstdio>
#include <cstdlib>

int main(int argc, char *argv[]) {
  int T;
  FILE *fin = fopen("in.txt", "r");
  FILE *fout = fopen("out.txt", "w");
  fscanf(fin, "%d", &T);

  for (int i = 0; i < T; i++) {
    double totalTime = 0;
    double cps = 2;

    double farmCost;
    double farmBonus;
    double goal;
    fscanf(fin, "%lf %lf %lf", &farmCost, &farmBonus, &goal);

    double optionFarm = (farmCost/cps) + (goal/(cps + farmBonus));
    double optionWin = goal/cps;
    printf("%lf vs %lf\n", optionFarm, optionWin);
    while (optionFarm < optionWin) {
      totalTime += farmCost/cps;
      cps += farmBonus;

      optionFarm = (farmCost/cps) + (goal/(cps + farmBonus));
      optionWin = goal/cps;
    }
    totalTime += optionWin;

    fprintf(fout, "Case #%d: %0.7lf\n", i + 1, totalTime);
  }

  return EXIT_SUCCESS;
}
