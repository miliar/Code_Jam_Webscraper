#include <cstdio>

using namespace std;

const double DELTA = 1e-6;
const char* INPUT_FILE = "B-large.in";
const char* OUTPUT_FILE = "b.out";

int main() {
  int test_cases;
  FILE* fin = fopen(INPUT_FILE, "r");
  FILE* fout = fopen(OUTPUT_FILE, "w");

  fscanf(fin, "%d\n", &test_cases);
  for (int ix = 1; ix <= test_cases; ix++) {
    double cost, factor, target;
    fscanf(fin, "%lf %lf %lf\n", &cost, &factor, &target);

    int farm_num = 0;
    double speed = 2;
    double min_time = 1e9;
    double farm_time = 0;
    int max_farm_num = target / cost + 1;
    for (int farm = 0; farm <= max_farm_num; farm++) {
      double this_time = farm_time + target / speed;
      if (min_time - this_time > DELTA)
        min_time = this_time;
      farm_time += cost / speed;
      speed += factor;
    }

    fprintf(fout, "Case #%d: ", ix);
    fprintf(fout, "%.7lf\n", min_time);
  }
  fclose(fin);
  fclose(fout);

  return 0;
}
