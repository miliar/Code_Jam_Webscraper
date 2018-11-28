#include <cstdio>

int solve() {
  int row1, row2;
  int answer1[4], answer2[4];
  int tmp;

  scanf("%d",&row1);
  for (int i=1; i<=4; i++)
    for (int j=0; j<4; j++)
      if (i == row1)
	scanf("%d",&answer1[j]);
      else
	scanf("%d",&tmp);

  scanf("%d",&row2);
  for (int i=1; i<=4; i++)
    for (int j=0; j<4; j++)
      if (i == row2)
	scanf("%d",&answer2[j]);
      else
	scanf("%d",&tmp);

  int answer = -2;

  for (int i=0; i<4; i++) {
    bool present = false;
    for (int j=0; j<4; j++)
      if (answer2[j] == answer1[i])
	present = true;
    if (present) {
      if (answer == -2)
	answer = answer1[i];
      else
	return -1;
    }
  }
  return answer;
}

int main() {
  int t;
  scanf("%d",&t);
  for (int tc=1; tc<=t; tc++) {
    int answer = solve();
    if (answer > 0) 
      printf("Case #%d: %d\n", tc, answer);
    else if (answer == -1)
      printf("Case #%d: Bad magician!\n", tc);
    else
      printf("Case #%d: Volunteer cheated!\n", tc);
  }
}
