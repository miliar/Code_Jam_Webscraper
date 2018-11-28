#include <bits/stdc++.h>

using namespace std;

int main()
{
  int t;
  scanf("%d",&t );
  for(int i = 0 ; i < t ; i++)
  {
    string s;
    bitset<100> bs;
    int total = 0;
    cin >> s;
    for(int x = 0 ; x < (int)s.size() ; x++)
    {
      if(s[x] == '-')
        bs.set(x,0);
      else
        bs.set(x,1);
    }
    while(bs.count() != s.size())
    {
      for(int x = s.size()-1 ; x >= 0 ; x--)
      {

        if(s[x] == '-')
        {
          total++;
          for(int y = x ; y >= 0 ; y--)
          {
            if(s[y] == '+')
            {
              bs.set(y,0);
              s[y] = '-';
            }
            else
            {
              s[y] = '+';
              bs.set(y,1);
            }
          }
        }
      }
    }
    printf("Case #%d: %d\n",i+1,total);
  }
  return 0;
}
