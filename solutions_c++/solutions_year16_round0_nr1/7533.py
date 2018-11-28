#include <bits/stdc++.h>

using namespace std;

bool digits[10];
int q;
int last_digit;

void check(int n) {
  while(n){
    if(digits[n%10] == false) {
      digits[n%10] = true;
      last_digit = n%10;
      q++;
    }
    n/=10;
  }
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for(int test = 1; test <= t; test++) {
    int n;
    q = 0;
    for(int i = 0; i<10; i++) {
      digits[i] = false;
    }
    scanf("%d", &n);
    int sum = n;
    if(n == 0) {
      printf("Case #%d: INSOMNIA\n", test);
      continue;
    }
    for(int i = 0; 1; i++, sum+=n) {
      check(sum);
      if(q == 10) break;
    }
    printf("Case #%d: %d\n", test, sum);
  }
  return 0;
}
