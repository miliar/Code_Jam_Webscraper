#include <cstdio>

int t, n, vetor[100000], y, z;

int findy()
{
  y = 0;
  for (int i = 0; i < n; i++)
  {
    if (i == n - 1)
    {
      break;
    }
    else if (vetor[i] > vetor[i + 1])
      y += (vetor[i] - vetor[i + 1]);
  }

  return y;
}

int findz()
{
  z = 0;
  int v = 0;
  for (int i = 0; i < n - 1; i++)
  {
    if (vetor[i] - vetor[i + 1] > v)
      v = (vetor[i] - vetor[i + 1]);
  }
  for (int i = 0; i < n - 1; i++)
  {
    if ( vetor[i] < v)
      z += vetor[i];
    else
      z += v;
  }

  return z;
}

int main()
{

  scanf("%d", &t);
  for (int i = 1; i <= t; i++)
  {
    scanf("%d", &n);
    for (int j = 0; j < n; j++)
      scanf("%d", &vetor[j]);


    printf("Case #%d: %d %d\n", i, findy(), findz());

  }
  return 0;
}
