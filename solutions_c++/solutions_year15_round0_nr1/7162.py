#include <cstdio>

int main()
{
  int t;
  int ncase = 1;
  char audience[1009];
  scanf("%d", &t);
  while(t--)
  {
    int length, answer = 0;
    scanf("%d %s", &length, audience);
    getchar();
    int acum = 0;
    for(int i = 0; i <= length; i++)
    {
      if(acum < i)
      {
        answer += i - acum;
        acum = i;
      }
      acum += (audience[i] - '0');
    }

    printf("Case #%d: %d\n", ncase++, answer);
  }
  return 0;
}
