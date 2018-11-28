#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

typedef long long LL;
const int maxn = 110;
const char aim[] = "+-";
char s[maxn];

int main() {
  freopen("B-large.in.txt", "r", stdin);
  freopen("B-large.out.txt", "w", stdout);
  int t, tt = 0;
  scanf("%d", &t);
  while (t--) {
    scanf("%s", s);
    int len = int(strlen(s)), ans = 0, flag = 0;
    for (int i = len - 1; i >= 0; --i) {
      if (s[i] != aim[flag]) {
        ++ans;
        flag ^= 1;
      }
    }
    printf("Case #%d: %d\n", ++tt, ans);
  }
  return 0;
}
