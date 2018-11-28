#include <iostream>

using namespace std;

int arr[16];

int main() {
  int cc;
  cin >> cc;
  for (int c = 1; c <= cc; c++) {
    memset(arr, 0, sizeof arr);
    int a;
    cin >> a;
    for (int i = 0; i < 16; i++) {
      int k;
      cin >> k;
      if (i >= (a-1)*4 && i < (a * 4)) {
        arr[k-1] = 1;
      }
    }

    int b;
    cin >> b;
    for (int i = 0; i < 16; i++) {
      int k;
      cin >> k;
      if (i >= (b-1)*4 && i < (b * 4)) {
        arr[k-1] += 1;
      }
    }


    int num;
    int cnt = 0;
    for (int i = 0; i < 16; i++) {
      if (arr[i] == 2 ) {
        cnt++;
        num = i+1;
      }
    }

    printf("Case #%d: ", c);


    if (cnt == 0) {
      printf("Volunteer cheated!\n");
    } else if (cnt == 1) {
      printf("%d\n", num);
    } else {
      printf("Bad magician!\n");
    }


  }


  return 0;
}
