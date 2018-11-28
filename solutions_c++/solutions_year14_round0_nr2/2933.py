#include <cstdio>
using namespace std;

int main() {
  FILE *fin = fopen("B-large.in", "r");
  FILE *fout = fopen("B-large.out", "w");
  int testnum; 
  fscanf(fin, "%d", &testnum);
  for (int test = 1; test <= testnum; ++test) {
    //printf("\n%d\n", test);
    double farm = 0, speed = 2, final = 0, delta = 0;
    double elapsed = 0;
    fscanf(fin, "%lf%lf%lf", &farm, &delta, &final);
    while (true) {
      //printf("%lf, %lf\n", (final - farm) / speed, final / (speed + delta));
      if (final > farm && (final - farm) / speed > final / (speed + delta)) {    
        elapsed += farm / speed;
        speed += delta;
      } else {
        elapsed += final / speed;
        break;
      }
    }
    fprintf(fout, "Case #%d: %.7lf\n", test, elapsed);
  }
}