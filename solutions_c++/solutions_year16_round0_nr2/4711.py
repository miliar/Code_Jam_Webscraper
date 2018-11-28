#include <cstdio>

int main()
{
  unsigned T;
  scanf("%u",&T);
  char temp;
  scanf("%c",&temp);
  for ( int i=1; i <= T; i++)
  {
    char current_cake,prev_cake;
    scanf("%c",&prev_cake);
    unsigned count = 0;
    for(;;)
    {
      scanf("%c",&current_cake);
      if(current_cake == '\n'){
        break;
      }else
      {
        if (current_cake != prev_cake)
          count++;
        prev_cake = current_cake;
      }
    }

    if(prev_cake == '-')
      printf("Case #%d: %u\n",i, count + 1);
    else
      printf("Case #%d: %u\n",i, count);
  }
}
