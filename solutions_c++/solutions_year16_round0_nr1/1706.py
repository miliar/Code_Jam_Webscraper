#include<cstdio>
int main()
{
  int i, x, y, tmp, mask, T, N;
  scanf("%d", &T);
  for (i=1;i<=T;i++) {
    scanf("%d", &N);
    x = N; y = 1;
    mask = 0;
    while (N) {
      tmp = x;
      while (tmp>0) {
	mask |= (1<<(tmp%10));
	tmp/=10;
      }
      //printf("%d %d\n", y, x);
      if (mask+1 == (1<<10)) {
	break;
      }
      x += N;
      y++;
    }
    printf("Case #%d: ",i);
    if (N>0) {
      printf("%d\n",x);
    } else {
      printf("INSOMNIA\n");
    }
  }
  return 0;
}
