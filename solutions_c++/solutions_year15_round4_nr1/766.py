#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

enum Dir
{
   NORTH,
   EAST,
   SOUTH,
   WEST,
   NONE
};

Dir translate( char c )
{
   if (c == '^') return NORTH;
   if (c == '>') return EAST;
   if (c == 'v') return SOUTH;
   if (c == '<') return WEST;
   if (c == '.') return NONE;
}

void move( long &r, long &c, Dir d )
{
   if (d == NORTH) r--;
   if (d == SOUTH) r++;
   if (d == WEST) c--;
   if (d == EAST) c++;
}

long solve ( Dir** grid, long rows, long cols )
{
   long result = 0;
   for (long r = 0; r < rows; r++) {
      for (long c = 0; c < cols; c++) {
         // Follow the arrow until you reach another
         Dir d = grid[r][c];
         if (d == NONE)
            continue;

         long r2 = r, c2 = c;
         bool fallsoff = false;

         do {
            move( r2, c2, d );
            if (r2 < 0 || r2 == rows || c2 < 0 || c2 == cols) {
               fallsoff = true;
               break;
            }
         } while (grid[r2][c2] == NONE);

         if (fallsoff) {
            result++;
            // Try other directions
            bool can_change = false;
            for (Dir d2 = NORTH; d2 < NONE; d2 = (Dir)((int)d2 + 1)) {
               r2 = r;
               c2 = c;
               fallsoff = false;
               do {
                  move( r2, c2, d2 );
                  if (r2 < 0 || r2 == rows || c2 < 0 || c2 == cols) {
                     fallsoff = true;
                     break;
                  }
               } while (grid[r2][c2] == NONE);

               if (!fallsoff) {
                  can_change = true;
                  break;
               }
            }

            if (can_change == false)
               return -1;
         }
      }
   }

   return result;
}

int main()
{
   std::ifstream in ("one.in", std::ifstream::in);
   std::ofstream out ("one.out", std::ofstream::out);

   long count;

   in >> count;
   for (long i = 1; i <= count; ++i) {
      long row, col;
      in >> row >> col;

      Dir **grid = new Dir*[row];
      for (long r = 0; r < row; ++r) {
         grid[r] = new Dir[col];
         for (long c = 0; c < col; ++c) {
            char ch;
            in >> ch;
            grid[r][c] = translate( ch );
         }
      }


      long r = solve( grid, row, col );

      if (r == -1)
         out << "Case #" << i << ": IMPOSSIBLE" << endl;
      else
         out << "Case #" << i << ": " << r << endl;
   }
   return 0;
}
