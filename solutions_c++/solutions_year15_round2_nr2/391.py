#include <cstdio>

void main2()
{
  int R, C, N;
  scanf("%d%d%d", &R, &C, &N);
  
  int R1 = (R-1)*C + (C-1)*R;
  int N1 = R*C-N;
  int R2 = (R-1)*C + (C-1)*R;
  int N2 = R*C-N;
  
  
  for (int i=1; i+1<R; i++)
  for (int j=1; j+1<C; j++)
  {
    if ((i+j)%2 == 0 && N1 > 0)
    {
      N1--;
      R1 -= 4;
    }
    if ((i+j)%2 == 1 && N2 > 0)
    {
      N2--;
      R2 -= 4;
    }
  }
  
  if (C > 1)
  for (int i=1; i+1<R; i++)
  {
    if (i%2 == 0 && N1 > 0)
    {
      N1--;
      R1 -= 3;
    }
    if (i%2 == 1 && N2 > 0)
    {
      N2--;
      R2 -= 3;
    }
    if ((i+C-1)%2 == 0 && N1 > 0)
    {
      N1--;
      R1 -= 3;
    }
    if ((i+C-1)%2 == 1 && N2 > 0)
    {
      N2--;
      R2 -= 3;
    }
  }
  
  if (R > 1)
  for (int i=1; i+1<C; i++)
  {
    if (i%2 == 0 && N1 > 0)
    {
      N1--;
      R1 -= 3;
    }
    if (i%2 == 1 && N2 > 0)
    {
      N2--;
      R2 -= 3;
    }
    if ((i+R-1)%2 == 0 && N1 > 0)
    {
      N1--;
      R1 -= 3;
    }
    if ((i+R-1)%2 == 1 && N2 > 0)
    {
      N2--;
      R2 -= 3;
    }
  }
  
  if (R == 1)
  {
    for (int i=0; i<C; i++)
    if (i%2 == 1 && N1 > 0)
    {
      N1--;
      R1 -= 2;
      if (i == C-1)
        R1++;
    }
  }
  
  if (C == 1)
  {
    for (int i=0; i<R; i++)
    if (i%2 == 1 && N1 > 0)
    {
      N1--;
      R1 -= 2;
      if (i == R-1)
        R1++;
    }
  }
  
  if (R > 1 && C > 1)
  {
    if (N1 > 0)
    {
      N1--;
      R1 -= 2;
    }
    if ((R+1)%2 == 0 && N1 > 0)
    {
      N1--;
      R1 -= 2;
    }
    if ((C+1)%2 == 0 && N1 > 0)
    {
      N1--;
      R1 -= 2;
    }
    if ((R+C)%2 == 0 && N1 > 0)
    {
      N1--;
      R1 -= 2;
    }
    if ((R+1)%2 == 1 && N2 > 0)
    {
      N2--;
      R2 -= 2;
    }
    if ((C+1)%2 == 1 && N2 > 0)
    {
      N2--;
      R2 -= 2;
    }
    if ((R+C)%2 == 1 && N2 > 0)
    {
      N2--;
      R2 -= 2;
    }
  }
  
  printf("%d\n", R2 < R1 ? R2 : R1);
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int i=0; i<T; i++)
  {
    printf("Case #%d: ", i+1);
    main2();
  }  
}
