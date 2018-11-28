#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>

using namespace std;

#define LENN 4

int main()
{
  int T, guess;
  int grid[LENN+10][LENN+10];

  scanf("%d", &T);
  for (int t = 1; t <= T; t++)
    {
      scanf("%d", &guess);
      for (int i = 0; i < LENN; i++) {
	for (int j = 0; j < LENN; j++) {
	  scanf("%d", &grid[i][j]);
	}
      }

      set<int> A;
      for (int i = 0; i < LENN; i++) {
	A.insert(grid[guess-1][i]);
      }

      scanf("%d", &guess);
      for (int i = 0; i < LENN; i++) {
	for (int j = 0; j < LENN; j++) {
	  scanf("%d", &grid[i][j]);
	}
      }
      
      set<int> B;
      for (int i = 0; i < LENN; i++) {
	B.insert(grid[guess-1][i]);
      }

      vector<int> AB (4);
      AB.resize(set_intersection(
        A.begin(), A.end(),
	B.begin(), B.end(),
	AB.begin()) - AB.begin());

      printf("Case #%d: ", t);
      if (AB.size() == 1) {
	printf("%d\n", *(AB.begin()));
      } else if (AB.size() > 1) {
	puts("Bad magician!");
      } else {
	puts("Volunteer cheated!");
      }
    }

  return EXIT_SUCCESS;
}
