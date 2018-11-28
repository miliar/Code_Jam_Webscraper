#include <iostream>
#include <cstdio>

using namespace std;

const int kMAX = 1010;
char str[kMAX];

int main() {
  //freopen("I:\\MyDocuments\\Code\\Code Jam 2015\\A-small-attempt0.in", "r", stdin);
  //freopen("I:\\MyDocuments\\Code\\Code Jam 2015\\A-large.in", "r", stdin);
  //freopen("I:\\MyDocuments\\Code\\Code Jam 2015\\a_out.txt", "w", stdout);
  int ncase, n;
  scanf("%d", &ncase);
  for(int hh = 1; hh <= ncase; ++hh) {
    scanf("%d%s", &n, str);
    int num = 0, sum = 0;
    for(int i = 0; i <= n; ++i) {
      if(sum < i) {
        num = max(num, i - sum);
      }
      sum += str[i] - '0';
    }
    printf("Case #%d: %d\n", hh, num);
  }
  return 0;
}
