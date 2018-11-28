#include <iostream>
#include <cstdio>
using namespace std;
int main() {
  FILE *fin = fopen("A-large.in", "r");
  FILE *fout = fopen("Qua-A.out", "w");
  int case_num = 0;
  fscanf(fin, "%d", &case_num);
  for (int c = 0; c < case_num; ++c) {
    char ch;
    int maxshy;
    fscanf(fin, "%d%c", &maxshy, &ch);
    int stand_num = 0;
    int friend_num = 0;
    for (int i = 0; i <= maxshy; ++i) {
      char tmp;
      int num;
      fscanf(fin, "%c", &tmp);
      num = tmp - '0';
      if (num > 0 && i > stand_num) {
        friend_num += i - stand_num;
        stand_num += i - stand_num;
      }
      stand_num += num;
    }
    fprintf(fout, "Case #%d: %d\n", c + 1, friend_num);
  }
  fclose(fout);
}