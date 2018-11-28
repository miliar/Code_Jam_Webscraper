#include <iostream>

using namespace std;

char board[4][4];


int horizontalCheck(int row, int& blankCount)
{
   int xCount = 0;
   int oCount = 0;
   int tCount = 0;
   for(int x =0; x < 4; ++x)
   {
      if( 'X' == board[x][row])
         ++xCount;

      if( 'T' == board[x][row])
         ++tCount;

      if( 'O' == board[x][row])
         ++oCount;

      if( '.' == board[x][row])
         ++blankCount;
   }
  
  // cout << "Row " << row << ": X: " << xCount << " T: " << tCount << " O: " << oCount << endl; 
   if( (xCount +tCount) == 4 )
      return 1;

   if( (oCount + tCount) == 4)
      return 2;

   return 0;
}

int verticalCheck(int col, int& blankCount)
{  
   int xCount = 0;
   int oCount = 0;
   int tCount = 0;

   for(int y =0; y < 4; ++y)
   {
      if( 'X' == board[col][y])
         ++xCount;

      if( 'T' == board[col][y])
         ++tCount;

      if( 'O' == board[col][y])
         ++oCount;
      
      if( '.' == board[col][y])
         ++blankCount;
   }

   
   //cout << "Col " << col << ": X: " << xCount << " T: " << tCount << " O: " << oCount << endl; 
   if( (xCount +tCount) == 4 )
      return 1;

   if( (oCount + tCount) == 4)
      return 2;
   
   return 0;
}


int diagCheckTopLeft(int& blankCount)
{
   int xCount = 0;
   int oCount = 0;
   int tCount = 0;
   int x = 0;
   int y = 0;
   
   while(x < 4 && y < 4)
   {
      if( 'X' == board[x][y])
            ++xCount;

      if( 'T' == board[x][y])
            ++tCount;

      if( 'O' == board[x][y])
            ++oCount;

      if( '.' == board[x][y])
         ++blankCount;

      ++x;
      ++y;
   }


   //cout << "Top Left Diag: X: " << xCount << " T: " << tCount << " O: " << oCount << endl; 
   if( (xCount +tCount) == 4 )
   if( (xCount +tCount) == 4 )
      return 1;

   if( (oCount + tCount) == 4)
      return 2;

  return 0; 

}

int diagCheckTopRight(int& blankCount)
{
   int xCount = 0;
   int oCount = 0;
   int tCount = 0;
   int x = 3;
   int y = 0;
   
   while(x >= 0 && y < 4)
   {
      if( 'X' == board[x][y])
            ++xCount;

      if( 'T' == board[x][y])
            ++tCount;

      if( 'O' == board[x][y])
            ++oCount;

      if( '.' == board[x][y])
         ++blankCount;

      --x;
      ++y;
   }

   //cout << "Top Right Diag: X: " << xCount << " T: " << tCount << " O: " << oCount << endl; 
   if( (xCount +tCount) == 4 )
      return 1;

   if( (oCount + tCount) == 4)
      return 2;
   
   return 0;
}

bool eval(int num, int gameNum)
{
   if(1 == num)
   {
      cout << "Case #" << gameNum << ": X won" << endl;
      return true;
   }

   if(2 == num)
   {
      cout << "Case #" << gameNum << ": O won" << endl; 
      return true;
   }

   return false;
}

int main(int argc, char* argv[])
{
   int testCases;

   cin >> testCases;


   for(int n=1; n <= testCases; ++n)
   {
      for(int y=0; y < 4; ++y)
      {
         for(int x=0; x < 4; ++x)
         {
           cin >> board[x][y]; 

         }

      }
     
      int blankCount = 0; 
  
      if(eval(horizontalCheck(0,blankCount), n))
            continue;

      if(eval(horizontalCheck(1,blankCount), n))
            continue;

      if(eval(horizontalCheck(2,blankCount), n))
            continue;
      if(eval(horizontalCheck(3,blankCount), n))
            continue;
      
      if(eval(verticalCheck(0,blankCount), n))
         continue;
      if(eval(verticalCheck(1,blankCount), n))
         continue;
      if(eval(verticalCheck(2,blankCount), n))
         continue;
      if(eval(verticalCheck(3,blankCount), n))
         continue;
      
      if(eval(diagCheckTopLeft(blankCount), n))
         continue;
      if(eval(diagCheckTopRight(blankCount), n))
         continue;

      if(blankCount > 0)
         cout << "Case #" << n << ": Game has not completed" << endl; 
      else
         cout << "Case #" << n << ": Draw" << endl; 
      
   }
   return 0;

}
