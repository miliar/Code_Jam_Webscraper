#include <cstdio>

int main()
{
  int N,T;
  scanf("%u",&T);
  for(unsigned j = 1 ; j <= T ; j++)
  {
    scanf("%u", &N);
    int flag = 0;
    if( N == 0 )
    {
      printf("Case #%d: INSOMNIA\n",j);
      continue;
    }
    for(int i=1;;i++)
    {
      unsigned long long M = i * N;
      unsigned long long temp = M;
      while(M)
      {
        int digit = M % 10;
        flag |= (1<<digit);
        M /= 10;
      }
      if(flag == 1023)
      {
        printf("Case #%d: %llu\n",j, temp);
        break;
      }
    }
  }

  return 0;
}
