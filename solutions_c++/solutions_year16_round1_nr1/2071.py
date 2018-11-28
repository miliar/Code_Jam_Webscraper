#include <stdio.h>
#include <string.h>
#include <deque>

#define MAX 1010
using namespace std;

deque<char> p;
char s[MAX];

int main(int argc, char const *argv[])
{
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    p.clear();
    memset(s, 0, MAX);
    scanf("%s", s);

    int l = strlen(s);
    for (int j = 0; j < l; j++) {
      if (p.size() != 0 && s[j] >= *(p.begin())) {
        p.push_front(s[j]);
      }
      else {
       p.push_back(s[j]);
      }
    }

    int size = p.size();
    printf("Case #%d: ", i+1);
    for (int j = 0; j < size; j++) {
      printf("%c", p[j]);
    }
    printf("\n");
  }
  return 0;
}