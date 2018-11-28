#include <iostream>
#include <vector>
#include <map>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main() {
  int caseNum = 0;
  cin >> caseNum;

  for (int c = 0; c < caseNum; c++) {
    cout << "Case #" << c+1 << ": ";

    char *signs = (char *) malloc(200);
    cin >> signs;

    int count = signs[0] == '+' ? 0 : 1;
    for (int i = 1; i < strlen(signs); i++) {
      if (signs[i] == '+' || signs[i] == signs[i-1]) {
        continue;
      }
      count += 2;
    }

    cout << count;

    if (c != caseNum - 1) {
      cout << endl;
    }
  }

  return 0;
}
