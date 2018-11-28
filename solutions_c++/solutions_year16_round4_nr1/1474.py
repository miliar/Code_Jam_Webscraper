#include <stdio.h>
#include <string.h>

#include <utility>


using std::swap;


char Fight(char a, char b) {
  if (a == 'P' && b == 'R') return 'P';
  if (a == 'R' && b == 'S') return 'R';
  if (a == 'S' && b == 'P') return 'S';
  return Fight(b, a);
}


bool Check(int n, char* str) {
  char buf[100], buf2[100];
  for (int i = 0; i < n; ++i) { buf[i] = str[i]; }

  while (n > 1) {
    for (int i = 0; i < n / 2; ++i) {
      if (buf[i * 2] == buf[i * 2 + 1]) {
        return false;
      }
      buf2[i] = Fight(buf[i * 2], buf[i * 2 + 1]);
    }
    n /= 2;
    for (int i = 0; i < n; ++i) {
      buf[i] = buf2[i];
    }
  }
  return true;
}


bool ok;
char ans[100];

void DFS(int n, int i, char *str) {
  if (n == i) {
    if (Check(n, str)) {
      ok = true;
      if (ans[0] == '\0' || strcmp(str, ans) < 0) {
        strcpy(ans, str);
      }
    }
  } else {
    for (int j = i; j < n; ++j) {
      swap(str[i], str[j]);
      DFS(n, i + 1, str);
      swap(str[i], str[j]);
    }
  }
}


int main(void) {
  int num_cases;
  scanf("%d", &num_cases);

  for (int case_idx = 1; case_idx <= num_cases; ++case_idx) {
    int n, r, p, s;
    scanf("%d %d %d %d", &n, &r, &p, &s);

    char str[10];
    int i = 0;
    while (p--) { str[i++] = 'P'; }
    while (r--) { str[i++] = 'R'; }
    while (s--) { str[i++] = 'S'; }
    str[i] = '\0';

    ans[0] = '\0';
    ok = false;
    DFS(1 << n, 0, str);
    if (ok) {
      printf("Case #%d: %s\n", case_idx, ans);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", case_idx);
    }
  }
  return 0;
}
