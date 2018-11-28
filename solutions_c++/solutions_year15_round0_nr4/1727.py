#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
     int cases;
     cin >> cases;
     for(int z=0; z<cases; z++)
     {
          int x, r, c;
          cin >> x >> r >> c;
          if(r > c)
               swap(r,c);

          bool gabriel;
          switch(x)
          {
          case 1: gabriel = true;
               break;
          case 2: gabriel = (r*c)%2==0;
               break;
          case 3:
               if((r*c)%3!=0)
                    gabriel = false;
               else
                    gabriel = r!=1;
               break;
          case 4:
               if((r*c)%4!=0)
                    gabriel = false;
               else
                    gabriel = r > 2;
               break;
          }

          cout << "Case #" << (z+1) << ": " << (gabriel ? "GABRIEL" : "RICHARD") << endl;
     }

     return 0;
}
