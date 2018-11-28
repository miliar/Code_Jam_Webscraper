#include <cstdio>
#define MAXN 1005

using namespace std;

char str[MAXN];
int n;

int main() {
  int tc;
  scanf("%d", &tc);
  for(int i = 0; i < tc; i++) {
    scanf("%d %s\n", &n, str);
    int ans = 0;
    int standup = 0;
    for(int ii = 0; ii <= n; ii++) {
      if(standup < ii) {
	ans += (ii - standup);
	standup = ii;
      }
      standup += str[ii] - '0';
    }
    printf("Case #%d: %d\n", i+1, ans);
  }
  return 0;
}
