#include <stdio.h>
#include <string.h>

int T;
int A, B;
int i;

bool isPalin(int n)
{
  char s[100];
  sprintf(s, "%d", n);
  
  int len = strlen(s);
  int i = 0;
  int j = len-1;
  while (i < j) {
    if (s[i] != s[j]) return false;
    i++; j--;
  }
  
  return true;
}

int main() {

  scanf("%d", &T);
  
  int cs = 0;
  while (T--) {
    cs++;
    
    scanf("%d %d", &A, &B);
    
    int cnt = 0;
    for (i = 1; i*i <= B; i++) {
      if (i*i < A) continue;
      if (!isPalin(i)) continue;
      if (!isPalin(i*i)) continue;
      cnt++;
    }
    
    printf("Case #%d: %d\n", cs, cnt);    
  }
  
  return 0;
}