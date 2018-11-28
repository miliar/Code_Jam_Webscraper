#include <cstdio>
#include <vector>
using namespace std;

bool contains(int x, vector<int> &vec) {
  for (int i = 0; i < vec.size(); i++) {
    if (vec[i] == x) {
      return true;
    }
  }
  return false;
}

int main(){
  int zet;
  scanf("%d", &zet);
  int caseNr = 0;
  while (zet--) {
    caseNr++;
    printf("Case #%d: ", caseNr);

    vector<int> first;

    int row1;
    scanf("%d", &row1);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
          int a;
          scanf("%d", &a);
        if (i+1 == row1) {
          first.push_back(a);
        }
      }
    }

    vector<int> result;

    int row2;
    scanf("%d", &row2);
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
          int a;
          scanf("%d", &a);
        if (i+1 == row2) {
          if (contains(a, first)) {
            result.push_back(a);
          }
        }
      }
    }

    switch (result.size()) {
      case 0:
        printf("Volunteer cheated!\n");
        break;
      case 1:
        printf("%d\n", result[0]);
        break;
      default:
        printf("Bad magician!\n");
        break;
    }
  }
  return 0;
}
