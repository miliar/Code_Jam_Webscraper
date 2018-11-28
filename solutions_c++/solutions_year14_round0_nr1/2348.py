#include <cstdio>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
  int T;
  
  scanf("%d", &T);

  for (int idx = 1; idx <= T; idx++) {
    printf("Case #%d: ", idx);
    
    int first_line;

    scanf("%d", &first_line);

    vector<int> first(4), v(4);

    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        if (i == first_line - 1) scanf("%d", &first[j]);
        else scanf("%d", &v[j]);
      }
    }

    sort(first.begin(), first.end());

    int second_line;

    scanf("%d", &second_line);

    vector<int> second(4);

    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        if (i == second_line - 1) scanf("%d", &second[j]);
        else scanf("%d", &v[j]);
      }
    }

    sort(second.begin(), second.end());

    vector<int> inter;

    set_intersection(first.begin(), first.end(), second.begin(), second.end(), back_inserter(inter));

    switch (inter.size()) {
    case 0:
      printf("Volunteer cheated!");
      break;

    case 1:
      printf("%d", inter[0]);
      break;

    default:
      printf("Bad magician!");
      break;
    }

    printf("\n");
  }
  
  return 0;
}
