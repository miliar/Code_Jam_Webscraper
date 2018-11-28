#include<stdio.h>

int main()
{
  int T, t;
  scanf("%d", &T);
  //int max_pwd[] = {0, 0, 1, };
  for(t=1; t<=T; t++)
    {
      int R, C, W;
      scanf("%d %d %d", &R, &C, &W);
      int ans = 0;
      //ans += R*(C/W);
      for(int i=0;i<C;i+=W)
	ans++;
      if(C/W < 2)
	{
	  ans += W-1;
	}
      else
	{
	  ans += W-1;
	}
      printf("Case #%d: %d\n", t, ans);

    }
}
