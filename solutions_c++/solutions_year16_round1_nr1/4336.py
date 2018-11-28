#include <stdio.h>
#include <string.h>
#include <stack>
using namespace std;

int main(void)
{
  int t, i, j;
  char s[1001], buf1[1001], buf2[1001];
  int max;
  stack<char> stk1, stk2;

  FILE *fin = fopen("A-large.in", "rt");
  if (fin == NULL) {
    return -1;
  }
  FILE *fout = fopen("output.txt", "wt");
  if (fout == NULL) {
    return -1;
  }

  fscanf(fin, "%d", &t);
  for (i = 1; i <= t; i++) {
    fscanf(fin, "%s", s);
    
    //init
    max = s[0];
    buf1[0] = buf2[0] = '\0';

    for (j = 0; j < strlen(s); j++) {
      if (s[j] >= max) {
        max = s[j];
        stk1.push(s[j]);
      } else {
        stk2.push(s[j]);
      }
    }

    j = 0;
    while (!stk1.empty()) {
      buf1[j] = stk1.top();
      buf1[j + 1] = '\0';
      j++;
      stk1.pop();
    }
    j = 0;
    while (!stk2.empty()) {
      buf2[j] = stk2.top();
      buf2[j + 1] = '\0';
      stk2.pop();
      j++;
    }

    _strrev(buf2);
    strcat(buf1, buf2);

    fprintf(fout, "Case #%d: %s\n", i, buf1);
    //printf("Case #%d: %s\n", i, buf1);
  }

  fclose(fin);
  fclose(fout);

  return 0;
}