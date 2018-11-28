#include "bits/stdc++.h"

using namespace std;

int main()
{
      int t,
          sMax;
      
      string s;
      scanf("%d",&t);
      
      for(int tst=1; tst <= t; tst++)
      {
            cin >> sMax >> s;
            int curr = 0, req = 0;

            for(int i=0; i < sMax + 1; i++)
            {
                  int people = s[i] - '0';
                  if(curr < i && people > 0)
                  {
                        //int people = s[i] - '0';
                        req += i - curr;
                        curr += req ;
                  }
            
                  curr += people;
            }

            printf("Case #%d: %d\n", tst, req);
      }
      
      return 0;
}
