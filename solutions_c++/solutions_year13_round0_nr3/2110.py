#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#define MAX 1024
int s[MAX], p[MAX];

int main(void)
{
  int T;
  int A,B;

  memset(p, 0, sizeof(p));
  for(int i = 1; i < MAX; i++)
  {
    char x[12];
    sprintf(x,"%d", i);
    p[i] = 1;
    int len = strlen(x);
    for(int j = 0; j < len/2 && p[i]; j++)
      if (x[j] != x[len-1-j])
        p[i] = 0;
  }

  memset(s, 0, sizeof(s));
  for(int i = 1; i*i < MAX; i++)
    if (p[i])
      s[i*i] = 1;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++)
  {
    printf("Case #%d: ", caso);
    scanf("%d %d", &A, &B);

    int r = 0;
    for(int i = A; i <= B; i++)
      if (s[i] && p[i])
        r++;

    printf("%d\n", r);
  }
}
