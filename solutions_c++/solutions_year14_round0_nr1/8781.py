#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int
main()
{
  int t, T, i, j, k, sol, r1, r2, x;
  vector<int> v;
  cin >> T;
  for (t = 0; t < T; t++) {
    sol = 0;
    cin >> r1;
    for (i = 0; i < 4; i++) {
      for (j = 0; j < 4; j++) {
        cin >> x;
        if (i == (r1-1))
          v.push_back(x);
      }
    }
    cin >> r2;
    for (i = 0; i < 4; i++) {
      for (j = 0; j < 4; j++) {
        cin >> x;
        if (i == (r2-1) ) {
          for (k = 0; k < v.size(); k++) {
            if (v[k] == x) {
              if (sol == 0) sol = x;
              else sol = -1;
            }
          }
        }
      }
    }
    v.clear();
    printf("Case #%d: ", t+1);
    if (sol > 0)
      printf("%d\n", sol); 
    else if (sol == 0)
      printf("Volunteer cheated!\n");
    else
      printf("Bad magician!\n");


  }

  return 0;
}
