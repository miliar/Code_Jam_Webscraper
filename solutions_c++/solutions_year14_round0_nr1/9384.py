#include <cstdio>

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    int x;
    scanf("%d", &x);

    int a[4];
    for (int i = 0; i < 4; ++i)
    {
      for (int j = 0; j < 4; ++j)
      {
	int y;
	scanf("%d", &y);

	if (i + 1 == x)
	{
	  a[j] = y;
	}
      }
    }

    scanf("%d", &x);

    int ans = 0;
    bool flag = true;
    for (int i = 0; i < 4; ++i)
    {
      for (int j = 0; j < 4; ++j)
      {
	int y;
	scanf("%d", &y);

	if (i + 1 == x)
	{
	  for (int k = 0; k < 4; ++k)
	  {
	    if (y == a[k])
	    {
	      if (ans == 0)
	      {
		ans = y;
	      }
	      else
	      {
		flag = false;
	      }
	    }
	  }
	}
      }
    }

    printf("Case #%d: ", t + 1);
    if (ans == 0)
    {
      printf("Volunteer cheated!\n");
    }
    else
    {
      if (flag)
      {
	printf("%d\n", ans);
      }
      else
      {
	printf("Bad magician!\n");
      }
    }
  }

  return 0;
}
