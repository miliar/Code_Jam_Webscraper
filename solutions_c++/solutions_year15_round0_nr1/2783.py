#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int MaxN = 1010;

int main(void) {
  int tc;
  scanf("%d",&tc);
  for (int t = 1; t <= tc; ++t) {
    int n;
    char s[MaxN];

    scanf("%d",&n);
    scanf("%s",s);

    int cnt = 0, sol = 0;
    for (int i = 0; i <= n; ++i) {
      while (cnt < i && s[i] != '0') {
	++cnt;
	++sol;
      }
      cnt += s[i] - '0';
    }
    
    printf("Case #%d: %d\n",t,sol);
  } 
  return 0;
}
