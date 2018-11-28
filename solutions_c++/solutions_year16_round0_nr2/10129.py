#include <stdio.h>
#include <string.h>
bool check_happy(char arr[], int n, char c) {
  for (int i = 0; i < n; ++i) {
    if (arr[i] != c) {
      return false;
    }
  }
  return true;
}

void reverse(char arr[], int e) {
  for (int i = 0; i < e/2; ++i) {
    char tmp = arr[e-i-1];
    arr[e-i-1] = arr[i];
    if (arr[e-i-1] == '-') arr[e-i-1] = '+';
    else if (arr[e-i-1] == '+') arr[e-i-1] = '-';

    arr[i] = tmp;
    if (arr[i] == '+') arr[i] = '-';
    else if (arr[i] == '-') arr[i] = '+';
  }
  if (e%2==1) {
    if (arr[e/2] == '+') arr[e/2] = '-';
    else if (arr[e/2] == '-') arr[e/2] = '+';
  }
}

int flipping(char arr[], int n, char c, int cnt) {
  if (check_happy(arr, n, c)) {
    return cnt;
  }
  if (n == 1 && arr[0] != 'c') return cnt+1;

  int min = 987654321;
  int tmp;
  if (arr[n-1] == c) {
    return flipping(arr, n-1, c, cnt);
  }
  else if (arr[0] != c) {
    reverse(arr,n);
    min = flipping(arr,n-1,c,cnt+1);
    reverse(arr,n);
  }
  if (c == '-') c = '+';
  else if (c=='+') c = '-';
  tmp = flipping(arr, n-1, c, cnt);
  ++tmp;
  
  if (min > tmp) min = tmp;
  return min;
}

int main() {
  int t;
  char s[101];
  scanf("%d",&t);
  for (int i = 1; i <= t; ++i) {
    scanf("%s",s);
    printf("Case #%d: %d\n", i, flipping(s,strlen(s),'+',0));
  }
  return 0;
}
