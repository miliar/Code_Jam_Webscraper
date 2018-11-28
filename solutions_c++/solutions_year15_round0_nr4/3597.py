#include <iostream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main()
{

    int cases = 0;
    cin >> cases;
    int d = cases;
    int i1, i2;
    string s;
    int X, R, C;
    int rich_wins = 0;
    int gab_wins = 0;
    while(cases) {
      --cases;
        cin >> X;
        cin >> R;
        cin >> C;
        //cout << X << ", " << R << ", " << C << "\n";

        if( X == 1)
        {
          rich_wins = 0;
          gab_wins = 1;
        }

        if( X == 2)
        {
          if((R*C)%X != 0)
          {
            rich_wins = 1;
            gab_wins = 0;
          }
          else {
            rich_wins = 0;
            gab_wins = 1;
          }
        }

        if( X == 3)
        {
          if((R*C)%X != 0)
          {
            rich_wins = 1;
            gab_wins = 0;
          }
          else {
            if( R == 1 || C == 1)
            {
              rich_wins = 1;
              gab_wins = 0;
            }
            else {
              rich_wins = 0;
              gab_wins = 1;
            }
          }

        }
        if( X == 4)
        {
          if( R*C == 12 || R*C == 16)
          {
            rich_wins = 0;
            gab_wins = 1;
          }
          else{
            rich_wins = 1;
            gab_wins = 0;
          }

        }

          if(rich_wins)
            std::cout << "Case #" << d - cases << ": RICHARD\n";
          if(gab_wins)
            std::cout << "Case #" << d - cases << ": GABRIEL\n";
        }



        return 0;
}


