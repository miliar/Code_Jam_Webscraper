#include <stdio.h>
#include <math.h>
#include <string.h>

long int from, to;

bool check_palindrome(long int x) {
    char s[128];
    sprintf(s, "%lu", x);
    int i =0;
    int len = strlen(s);
    for(i=0; i < len/2; i++) {
        if (s[i] != s[len-1-i]) {
            return false;
        }
    }
    return true;
}

bool check_fair_square(long int x) {
    long int y = x*x;
    if (y<from) return false;
    return check_palindrome((long int) y);
}

int main() {
  FILE *fp = fopen("input.dat", "r");
  FILE *fout = fopen("output.dat", "w");
  int cases;
  fscanf(fp, "%d\n", &cases);

  int case_count =0;
  for (case_count=0; case_count<cases; case_count++) {
    fscanf(fp, "%lu %lu\n", &from, &to);
    to = (long int) sqrt(to);
    int count =0;
    long int sfrom = sqrt(from);
    long int i = sfrom;
    for(i = sfrom; i <= to; i++) {
        if (!check_palindrome(i)) continue;
        if (!check_fair_square(i)) continue;
        count++;
    }
    fprintf(fout, "Case #%d: %d\n", case_count+1, count);
  }
  fclose(fp);
  fclose(fout);

  return 1;
}
