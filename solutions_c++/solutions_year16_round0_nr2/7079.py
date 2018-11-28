#include <iostream>

using namespace std;

char s[101];
int main() {
  int t;
  scanf("%d", &t);

  for(int i=0; i<t; i++) {
    scanf("%s", s);
    long long int result = 0;
    if (s[0]=='-') result++;
    for(int j=1; s[j]!='\0'; j++) {
      if (s[j-1] == '+') {
        if (s[j] == '-') {
          result+=2;
        }
      } else {
      }
    }

    printf("Case #%d: %lld\n", i+1, result);

  }
  return 0;
}
