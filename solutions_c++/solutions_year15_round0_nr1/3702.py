#include <iostream>
#include <cstdio>

const int MAX_SIZE = 1003;

void solve(char* s, int i) {
  int friends_needed;
  int total_standing = s[0] - '0';
  for (int i = 1; s[i]; i++) {
    if (total_standing + friends_needed < i && s[i] != '0') {
      friends_needed = i - total_standing;
    }
    total_standing += s[i] - '0';
  }
  printf("Case #%d: %d\n", i, friends_needed);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tests;	  	    
  scanf("%d\n", &tests);
  for (int i = 0; i < tests; i++) {
    int s_max;
    scanf("%d ", &s_max);
    char s[MAX_SIZE];
    scanf("%s", s);
    solve(s, i + 1);
  }
  fclose(stdout);
}
