#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef pair<int, char> symbol;
const int MAXL = 10005;
char input[MAXL];
char req[5] = "ijkx";

symbol mul(const symbol &a, const symbol &b) {
  if(a.second == '1')
    return symbol(a.first*b.first, b.second);
  if(b.second == '1')
    return symbol(a.first*b.first, a.second);
  if(a.second == b.second)
    return symbol(-1*a.first*b.first, '1');

  if(a.second == 'i' && b.second == 'j')
    return symbol(a.first*b.first, 'k');
  if(a.second == 'i' && b.second == 'k')
    return symbol(-1*a.first*b.first, 'j');

  if(a.second == 'j' && b.second == 'i')
    return symbol(-1*a.first*b.first, 'k');
  if(a.second == 'j' && b.second == 'k')
    return symbol(a.first*b.first, 'i');

  if(a.second == 'k' && b.second == 'i')
    return symbol(a.first*b.first, 'j');
  if(a.second == 'k' && b.second == 'j')
    return symbol(-1*a.first*b.first, 'i');
}

int main(void) {
  int T;
  scanf("%d", &T);
  for(int kase = 1; kase <= T; ++kase) {
    int L, X, ptr = 0;
    symbol tmp = symbol(1, '1');
    scanf("%d %d", &L, &X);
    scanf("%s", input);
    for(int i = 0; i < X; ++i) {
      for(int j = 0; j < L; ++j) {
        tmp = mul(tmp, symbol(1, input[j]));
        if(tmp == symbol(1, req[ptr])) {
          tmp = symbol(1, '1');
          ptr++;
        }
      }
    }
    printf("Case #%d: ", kase);
    if(tmp == symbol(1, '1') && ptr == 3)
      printf("YES\n");
    else
      printf("NO\n");
  }
  return 0;
}
