#include <cstdio>
#include <cstring>

int main () {

  int T;
  scanf ("%d\n", &T);
  char s1 [150];
  char s2 [150];
  for (int t = 1; t <= T; ++t) {
    int n;
    scanf ("%d\n", &n);
    scanf ("%s%s", s1, s2);
    //printf ("s1 = %s s2 = %s\n", s1, s2);
    int l1 = strlen (s1);
    int l2 = strlen (s2);
    int i, j;
    i = j = 0;
    bool possible = true;
    int moves = 0;
    while (i < l1 && j < l2) {
      //printf ("comparing s1[%d] = %c and s2[%d] = %c\n", i, s1[i], j, s2[j]);
      if (s1[i] != s2[j]) {
	possible = false;
	break;
      }
      if (s1[i+1] == s2[j+1]) {
	++i;
	++j;
	continue;
      }
      // We know that the following character is different
      if (s1[i+1] == s2[j]) {
	//printf ("Enters first option\n");
	while (s1[i+1] == s2[j]) {
	  ++moves;
	  ++i;
	}
      }
      else if (s1[i] == s2[j+1]) {
	while (s1[i] == s2[j+1]) {
	  ++moves;
	  ++j;
	}
      }
      ++i;
      ++j;
    }
    if (!possible || s1[i] != s2[j])
      printf ("Case #%d: Fegla Won\n", t);
    else
      printf ("Case #%d: %d\n", t, moves);
  }

  return 0;
}
