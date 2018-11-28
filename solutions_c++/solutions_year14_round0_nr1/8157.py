#include <cstdio>
#include <vector>

using namespace std;

int main()
{
  int T;
  int counter = 0;
  vector<int> num(16, 0);
  int row;

  scanf("%d", &T);
  T = T << 1;
  while (T--) {
    scanf("%d", &row);
    int aux;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
	scanf("%d", &aux);
	if (i == row - 1)
	  num[aux-1]++;
      }
    }
    if (!(T%2)) {
      vector<bool> flag (2, false);
      int result;
      for (int i = 0; i < 16; i++) {
	if (num[i] == 2) {
	  if (flag[1])
	    flag[0] = true;
	  else {
	    result = i+1;
	    flag[1] = true;
	  }
	}
      }

      printf("Case #%d: ", ++counter);
      if (flag[0])
	printf("Bad magician!\n");
      else if (flag[1])
	printf("%d\n", result);
      else
	printf("Volunteer cheated!\n");

      num = vector<int>(16, 0);
    }
  }

  return 0;
}
