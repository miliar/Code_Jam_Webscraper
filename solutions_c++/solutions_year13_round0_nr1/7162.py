#include <cstdio>

char A[4][4];
int main()
{
  freopen("tictac.in", "r", stdin);
  freopen("tictac.out", "w", stdout);
  
  int N;
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    scanf(" ");
    bool completed = true;
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
	scanf("%c", &A[j][k]);
	if (A[j][k] == '.')
	  completed = false;
      }
      scanf(" ");
    }
    
    int winner = 0;
    for (int j = 0; j < 4 && !winner; j++) {
      char ok = A[j][0] == 'T' ? A[j][1] : A[j][0];
      if (ok == '.') continue;
      int k;
      for (k = 0; k < 4; k++)
	if (A[j][k] != ok && A[j][k] != 'T')
	  break;
      if (k == 4)
	winner = ok == 'X' ? 1 : 2;
    }
    
    for (int k = 0; k < 4 && !winner; k++) {
      char ok = A[0][k] == 'T' ? A[1][k] : A[0][k];
      if (ok == '.') continue;
      int j;
      for (j = 0; j < 4; j++)
	if (A[j][k] != ok && A[j][k] != 'T')
	  break;
      if (j == 4)
	winner = ok == 'X' ? 1 : 2;
    }
    
    if (!winner) {
      char ok = A[0][0] == 'T' ? A[1][1] : A[0][0];
      int j = 0;
      if (ok != '.')
	for (j = 0; j < 4; j++)
	  if (A[j][j] != ok && A[j][j] != 'T')
	    break;
      if (j == 4)
	winner = ok == 'X' ? 1 : 2;
      ok = A[0][3] == 'T' ? A[1][2] : A[0][3];
      j = 0;
      if (ok != '.')
	for (j = 0; j < 4; j++)
	  if (A[j][3 - j] != ok && A[j][3 - j] != 'T')
	    break;
      if (j == 4)
	winner = ok == 'X' ? 1 : 2;
    }
    
    if (winner == 1)
      printf("Case #%d: X won\n", i + 1);
    else
      if (winner == 2)
	printf("Case #%d: O won\n", i + 1);
      else
	if (completed)
	  printf("Case #%d: Draw\n", i + 1);
	else
	  printf("Case #%d: Game has not completed\n", i + 1);
  }
  
  return 0;
}
