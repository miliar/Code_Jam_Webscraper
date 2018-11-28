#include <cstdio>
#include <algorithm>

/**
 * 运行老出错！！
 * 运行CalcWar时，修改了数组的内容！！
 */
using namespace std;

const char* INPUT_FILE = "D-large.in";
const char* OUTPUT_FILE = "d.out";

const int MAXN = 1000;

int CalcWar(double naomi[], double ken[], int size);
int CalcDecWar(double naomi[], double ken[], int size);

int main() {
  int test_cases;
  FILE* fin = fopen(INPUT_FILE, "r");
  FILE* fout = fopen(OUTPUT_FILE, "w");

  double naomi[MAXN];
  double ken[MAXN];

  fscanf(fin, "%d\n", &test_cases);
  for (int ix = 1; ix <= test_cases; ix++) {
    int N;
    fscanf(fin, "%d\n", &N);
    for (int i  = 0; i < N; i++)
      fscanf(fin, "%lf", &naomi[i]);
    std::sort(naomi, naomi + N);
    for (int i  = 0; i < N; i++)
      fscanf(fin, "%lf", &ken[i]);
    std::sort(ken, ken + N);

//    for (int i = 0; i < N; i++)
//      printf("%lf ", naomi[i]);
//    printf("\n");
//    for (int i = 0; i < N; i++)
//      printf("%lf ", ken[i]);
//    printf("\n");

    int dec_score = CalcDecWar(naomi, ken, N);
    int war_score = CalcWar(naomi, ken, N);
    fprintf(fout, "Case #%d: %d %d\n", ix, dec_score, war_score);
  }
  fclose(fin);
  fclose(fout);

  return 0;
}

/*
int CalcDecWar(double naomi[], double ken[], int size) {
  int score = 0;
  int chosen_naomi = 0;
  int chosen_ken = size - 1;
  while (chosen_naomi < size && naomi[chosen_naomi] < ken[chosen_ken]) {
    chosen_naomi++;
    chosen_ken--;
  }
  return size - chosen_naomi;
}
*/

int CalcDecWar(double naomi[], double ken[], int size) {
  int score = 0;
  int chosen_naomi = size - 1;
  int chosen_ken = size - 1;
  while (chosen_naomi >= 0 && chosen_ken >= 0) {
    if (naomi[chosen_naomi] > ken[chosen_ken]) {
      score++;
      chosen_naomi--;
      chosen_ken--;
    } else {
      chosen_ken--;
    }
  }
  return score;
}

int CalcWar(double naomi[], double ken[], int size) {
  int score = 0;
  for (int i = 0; i < size; i++) {
    int chosen_ken = -1;
    for (int j = 0; j < size; j++) {
      if (ken[j] > naomi[i] && (chosen_ken == -1 || ken[chosen_ken] > ken[j])) {
        chosen_ken = j;
      }
    }
    if (chosen_ken == -1) {
      score++;
    } else {
      ken[chosen_ken] = 0;
    }
  }
  return score;
}
