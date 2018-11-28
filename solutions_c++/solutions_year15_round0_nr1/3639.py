#include <cstdio>
#include <cstring>
using namespace std;

char buffer[1024];

int main() {
  int tcase;
  scanf ("%d", &tcase);
  for (int itr = 1; itr <= tcase; itr++) {
    int len, idx = 0, smax, result = 0;
    scanf ("%d", &smax);
    scanf ("%s", buffer);
    
    len = strlen (buffer);
    while (buffer[idx] == ' ')
      idx++ ;

    int cnt = buffer[idx] - '0';
    for (int i = 1; i <= smax; i++) {
//      printf ("%d -> cnt = %d, result = %d\n", i, cnt, result);
      int extra = 0;
      if ((cnt < i) && ((buffer[idx+i] - '0') > 0)) {
        extra = (i - cnt);
        result += extra;
      }
      cnt += ((buffer[idx+i] - '0') + extra);
    }
    printf ("Case #%d: %d\n", itr, result);
  }
}
