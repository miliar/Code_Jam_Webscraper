#include <iostream>
#include <cstdio>
#include <string.h>
#include <cmath>
using namespace std;

char buf[100];
bool IsPal(int n) {
  sprintf(buf, "%d", n);
  int len = strlen(buf);
  for (int i = 0; i < len - i - 1; ++i) {
    if (buf[i] != buf[len - i - 1]) {
      return false;
    }
  }
  return true;
}

int A, B;
void Input() {
  scanf("%d %d", &A, &B);
}

int main() {
  //freopen("in.txt", "r", stdin);
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i){
    Input();
    int cnt = 0;
    for (int num = A; num <= B; ++num) {
      int sq = sqrt(num);
      if (IsPal(num) && IsPal(sq) && sq * sq == num) {
	cnt ++;
      }
    }
    printf("Case #%d: %d\n", i, cnt);
  }  
  return 0;
}
