#include <cstdio>

int arr1[4], arr2[4];

void work(int ind) {
  printf("Case #%d: ", ind);
  int A, B;
  scanf("%d", &A);
  A--;
  int i, j;
  int temp;
  for(i = 0; i < 4; i++) {
    for(j = 0; j < 4; j++) {
      scanf("%d", &temp);
      if(A == i) {
	arr1[j] = temp;
      }
    }
  }
  scanf("%d", &B);
  B--;
  for(i = 0; i < 4; i++) {
    for(j = 0; j < 4; j++) {
      scanf("%d", &temp);
      if(B == i) {
	arr2[j] = temp;
      }
    }
  }
  int flag = 0, ans = 0;
  for(i = 0; i < 4; i++) {
    temp = arr1[i];
    for(j = 0; j < 4; j++) {
      if(arr2[j] == temp) break;
    }
    if(j != 4) {
      flag++;
      ans = temp;
    }
  }
  if(flag == 0) {
    printf("Volunteer cheated!\n");
  }
  else if(flag == 1) {
    printf("%d\n", ans);
  }
  else {
    printf("Bad magician!\n");
  }
}
      
  

int main() {
  int T;
  scanf("%d", &T);
  int cnt = 0;
  while(T--) {
    cnt++;
    work(cnt);
  }
  return 0;
}
