#include<iostream>
#include<string>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int test = 0; test < T; test++)
    {
      string s;
      cin>>s;
      string newstr = s;
      char prev = newstr[0];
      long long count = 0;
      for(int i=1; i < newstr.size();i++)
        {
          if(prev == newstr[i])
            continue;
          if(prev == '-' && newstr[i] == '+')
            {
              count += 1;
              prev = newstr[i];
            }
          else if(prev == '+' && newstr[i] == '-')
            {
              count += 1;
              prev = newstr[i];
            }
        }
      if(prev == '-')
        printf("Case #%d: %lld\n", test + 1, count + 1);
      else
        printf("Case #%d: %lld\n", test + 1, count);

    }
}
