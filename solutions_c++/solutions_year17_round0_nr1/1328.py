#include <cstdio>
#include <cstring>

int t;
char s[2000];
int k;
int sum[2000];
int len;

int main()
{
  scanf("%d", &t);
  for(int i = 0; i < t; ++i) {
    int result = 0;
    scanf("%s %d", s, &k);
    len = strlen(s);
    for(int j = 0; j < len-k+1; ++j) {
      if((sum[j]+((s[j] == '-') ? 1 : 0)) % 2) {
        ++result;
        for(int l = j; l < j+k; ++l) ++sum[l];
      }
    }
    bool ok = true;
    for(int j = len-k+1; j < len; ++j) {
      if((sum[j]+((s[j] == '-') ? 1 : 0)) % 2) {
        ok = false;
        break;
      }
    }
    printf("Case #%d: ", i+1);
    if(ok) {
      printf("%d\n", result);
    }
    else printf("IMPOSSIBLE\n");
    for(int j = 0; j < 1500; ++j) {
      sum[j] = 0;
    }
  }
  return 0;
}
