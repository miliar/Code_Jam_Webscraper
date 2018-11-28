#include <iostream>
using namespace std;

int main()
{
   int n;
   cin >> n;

   for(int i = 0; i < n; i++)
   {
      int x, r, c;
      cin >> x >> r >> c;
      bool richard = true;
      if( (r * c) % x != 0 ||//non-multiple
         (( x > r ) && (x > c)))//overflow
      {
         richard = true;
      }
      else
      {
         richard = false;
         //1 always passes
         //2 always passes if multiple
         if( x == 3 )
         {
          //for 3 straight
           //always passes if board is at least 3x1
          //for 3 bent
            if( std::min(r,c) < 2 )
               richard = true;
         }

         if( x == 4 )//at least one must have dimension 4
         {
            int other = std::min(r,c);
            if( other == 1 || other == 2 )
               richard = true;
            //case 0 (square) (4x1 fails)    
            //case 2 (4x2 or 4x4 still good)
            //case 3
            //case 4 zig-zag breaks 4x2

            //for 4 straigt (case 4)
              //always passes if board is at least 4x1, but may overflow (above)          
         }
      }

      std::cout << "Case #" << i+1 << ": " << (richard ? "RICHARD" : "GABRIEL") << std::endl;
   }
}