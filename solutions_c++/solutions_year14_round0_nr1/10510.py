#include <cstdio>
#include <cstring>

int a[4][4], b[4][4];
bool cards[17];

int main (){
  freopen ("input.in", "r", stdin);
  freopen ("output.out", "w", stdout);
  int t, r1, r2, c, d, cases = 0;
  scanf ("%d", &t);
  while (t--){
    memset (cards, 0, sizeof (cards));
    c = 0;
    scanf ("%d", &r1);
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
	scanf ("%d", &a[i][j]);
    for (int j = 0; j < 4; j++)
      cards[a[r1 -  1][j]] = 1;
    scanf ("%d", &r2);
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
	scanf ("%d", &b[i][j]);
    for (int j = 0; j < 4; j++)
      if (cards[b[r2 - 1][j]]){
	c++;
	d = b[r2 - 1][j];
      }
    printf ("Case #%d: ", ++cases);
    if (c > 1) printf ("Bad magician!\n");
    if (c == 1) printf ("%d\n", d);
    if (!c) printf ("Volunteer cheated!\n");
  }
}
