#include <cstdio>

using namespace std;

void solve(int test) {
  int len;
  scanf("%d", &len);
  getchar();
  int stood = 0;
  int answer = 0;
  for (int i = 0; i < len + 1; i++) {
    int c = getchar() - '0';
    if (c > 0 && stood < i) {
      answer += i - stood;
      stood = i;
    }
    stood += c;
  }
  printf("Case #%d: %d\n", test, answer);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    solve(i);
  }
  return 0;
}