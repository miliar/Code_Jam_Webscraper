#include <cstdio>

using namespace std;

const int MAXS=100;

int cases, last, totes;
char inp[MAXS+5];

int main()
{
  scanf("%d", &cases);
  for(int q=1; q<=cases; q++)
  {
    last=0, totes=0;
    scanf("%s", inp);
    for(int i=0; inp[i]; i++)
    {
      if(inp[i]!=inp[i-1])
      {
        if(inp[i]=='-')
        {
          if(last)
            totes+=2;
          else
            totes++, last++;
        }
        else
          last++;
      }
    }
    printf("Case #%d: %d\n", q, totes);
  }
}
