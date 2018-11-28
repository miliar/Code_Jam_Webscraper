#include <cstdio>

using namespace std;

int main () {

  int T;
  scanf ("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int count [20];
    for (int i = 0; i < 20; ++i)
      count[i] = 0;
    for (int k = 0; k < 2; ++k) {
      int r, x;
      scanf ("%d", &r);
      for (int i = 1; i < 5; ++i) {
	for (int j = 1; j < 5; ++j) {
	  scanf ("%d", &x);
	  if (i == r)
	    count[x]++;
	}
      }
    }

    // Check
    int c = 0;
    int k;
    for (int i = 1; i <= 16; ++i)
      if (count[i] == 2) {
	++c;
	k = i;
      }

    // Print
    printf ("Case #%d: ", t);
    if (c == 0)
      printf ("Volunteer cheated!\n");
    else if (c == 1)
      printf ("%d\n", k);
    else
      printf ("Bad magician!\n");
    
  }
  
  return 0;
}
