#include <cstdio>
#include <algorithm>
using namespace std;

int arr[10003];

void work(int ind) {
  printf("Case #%d: ", ind);
  int X, N;
  scanf("%d %d", &N, &X);
  int i;
  for(i = 0; i < N; i++) {
    scanf("%d", &arr[i]);
  }
  sort(arr, arr + N);
  int large, small;
  small = 0;
  large = N - 1;
  int cnt = 0;
  while(large > small) {
    if(arr[large] + arr[small] <= X) {
      large--;
      small++;
      cnt++;
    }
    else {
      large--;
      cnt++;
    }
  }
  if(large == small) {
    cnt++;
  }
  printf("%d\n", cnt);
  
}

int main() {
  int T;
  scanf("%d", &T);
  for(int i = 1; i <= T; i++) {
    work(i);
  }
  return 0;
}
