#include<bits/stdc++.h>
using namespace std;
int main()
{
    int tst;
    scanf("%lld",&tst);
    for(long long int y=1;y<=tst;y++)
    {
  char str[10000];
  scanf("%s",str);
  char pr=str[0];
  long long int i,count=0;
  for(i=0;i<strlen(str);i++)
  {
      if(str[i]!=pr)
      {
          count++;
          pr=str[i];
      }
  }
  if(pr=='-')
    count++;

  printf("Case #%lld: %lld\n",y,count);
    }
    return 0;
}
