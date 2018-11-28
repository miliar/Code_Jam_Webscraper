#include "bits/stdc++.h"

using namespace std;

int main()
{
map<string, string> M;
M["3 1 1"] = "RICHARD"; M["3 1 2"] = "RICHARD"; M["3 1 3"] = "RICHARD"; M["3 1 4"] = "RICHARD";
M["3 2 1"] = "RICHARD"; M["3 2 2"] = "RICHARD"; M["3 2 3"] = "GABRIEL"; M["3 2 4"] = "RICHARD";
M["3 3 1"] = "RICHARD"; M["3 3 2"] = "GABRIEL"; M["3 3 3"] = "GABRIEL"; M["3 3 4"] = "GABRIEL";
M["3 4 1"] = "RICHARD"; M["3 4 2"] = "RICHARD"; M["3 4 3"] = "GABRIEL"; M["3 4 4"] = "RICHARD";

M["4 1 1"] = "RICHARD"; M["4 1 2"] = "RICHARD"; M["4 1 3"] = "RICHARD"; M["4 1 4"] = "RICHARD";
M["4 2 1"] = "RICHARD"; M["4 2 2"] = "RICHARD"; M["4 2 3"] = "RICHARD"; M["4 2 4"] = "RICHARD";
M["4 3 1"] = "RICHARD"; M["4 3 2"] = "RICHARD"; M["4 3 3"] = "RICHARD"; M["4 3 4"] = "GABRIEL";
M["4 4 1"] = "RICHARD"; M["4 4 2"] = "RICHARD"; M["4 4 3"] = "GABRIEL"; M["4 4 4"] = "GABRIEL";



      int t;

      scanf("%d", &t);
      string s;
      
      getline(cin, s);
      for(int tst =1 ; tst <= t; tst++)
      {
            getline(cin , s);
            int x = s[0] - '0';
            int r = s[2] - '0';
            int c = s[4] - '0';
            
            string winner = "";
            switch( x )
            {
                  case 1: winner = "GABRIEL";
                          break;
                  case 2: if( (r * c) % 2 == 0)
                                winner = "GABRIEL";
                          else
                                winner = "RICHARD";
                          break;
                  case 3:
                  case 4: winner = M[s] ;
                          break;
            }

            cout << "Case #"<< tst << ": " << winner << "\n";
      }
      

      return 0;
}
