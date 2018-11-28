#include<cstdio>

using namespace std;

int main() {
  int t;
  scanf("%d\n", &t);
  for(int i = 1; i <= t; ++i) {
    int a = 0;
    char last = '.';
    char c;
    while((c = getchar()) != '\n') {
      if (last == '.') {
        last = c;
      } else if (last != c) {
        a++;
        last = c;
      }
    }

    if(last == '-') {
      a++;
    }
    printf("Case #%d: %d\n", i, a);
  }
  return 0;
}
