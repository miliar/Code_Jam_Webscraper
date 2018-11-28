#include <cstdio>
#include <cstring>

int t, T;
char str[1000001];
int n;
//             a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
int con[26] = {0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ,1};

int solve()
{
  int i, j;
  int ans;
  int len, count, last;
  len = strlen(str);
  ans = 0;
  last = 0;
  for(i = 0; i < len; ++i) {
    count = 0;
    for(j = i; j < len && count < n; ++j)
      if(con[str[j]-'a'] == 0)
	break;
      else
	count++;
    j--;
    if(count == n) {
      if((i-last)*(len-j) > 0) {
	ans += (i-last)*(len-j) + len-j;
      }
      else {
	ans += i-last;
	ans += len-j;
      }
      last = i+1;
    }
  }
  return ans;
}

main()
{
  scanf("%d", &T);
  for(t = 1; t <= T; ++t) {
    scanf("%s", str);
    scanf("%d", &n);
    printf("Case #%d: %d\n", t, solve());
  }
}
