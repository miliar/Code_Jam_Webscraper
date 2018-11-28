#include <stdio.h>

int main() {
  int t, s, i, c, friends, people, v[1003], aux;
  char in[1003];

  c = 1;
  scanf("%d", &t);
  while (t--) {
    friends = 0;
    people = 0;
    scanf("%d", &s);
    scanf("%s", in);
    for (i = 0; i < s + 1; i++) {
      v[i] = in[i] - '0';
    }
    for (i = 0; i < s + 1; i++) {
      if (i > people) {
	aux = i - people;
	friends += aux;
	people = people + aux + v[i];
      } else {
	people += v[i];
      }
    }
    printf("Case #%d: %d\n", c, friends);
    c++;
  }
  return 0;
}
