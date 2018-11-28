#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

//to do
//get game to work for draw
//get game to work for incomplete

const int COL = 4;
const int ROW = 4;

int counter2 = 0;

int draw(char[ROW][COL]); //checks for draws
/* ****** functions borrowed from ACSL Chess Queen *********************************/
int lr(int, int, int, char[ROW][COL]);//calculates if there is a win left to right
int ud(int, int, int, char[ROW][COL]);//calculates if there is a win up and down
int diag(int, int, int, char[ROW][COL]);//calculates if there is a win diagonaly
int diag1(int, int, int, char[ROW][COL]);//calculates if there is a win diagonaly

int main(int argc, char *argv[])
{
    char minefeild[COL][ROW]; 
    int cases, answer, res;
    string result;
    ifstream infile;
    ofstream outfile;
    infile.open("A-small-practice(6).txt");
    outfile.open("answer.txt"); 
    
    infile >> cases;
    
for (int j = 0; j < cases; j++)
   {
         result = "  ";
    for(int r = 0; r < ROW; r ++)
         {   
          for (int c = 0; c < COL; c++)
              infile >> minefeild[r][c];
          }
              
    for(int r = 0; r < ROW; r ++)  
    {
     
          for (int c = 0; c < COL; c++)
              cout << minefeild[r][c] << " ";
     cout << endl;
    }
    cout << endl;
    //result = "Draw";
   
    
    for(int r = 0; r < ROW; r ++)
         {   
          for (int c = 0; c < COL; c++)
              {
              answer = lr(4, r, c, minefeild);
              if(answer == 4)
                        {
                        res = 1;
                        result = "X won";
                        cout << answer << "X won" << endl;
                        }
              if(counter2 == -4)
                        {
                        result = "O won";
                        cout << "O won" << endl;
                        }
              answer = ud(4, r, c, minefeild);
              if(answer == 4)
                        {
                        result = "X won";
                        cout << "X won" << endl;
                        }
              if(counter2 == -4)
                        {
                        result = "O won";
                        cout << "O won" << endl;
                        }
              answer = diag(4, r, c, minefeild); 
              if(answer == 4)
                        {
                        result = "X won";
                        cout << "X won" << endl;
                        }
              if(counter2 == -4)
                        {
                        result = "O won";
                        cout << "O won" << endl;
                        }
              answer = diag1(4, r, c, minefeild); 
              if(answer == 4)
                        {
                        result = "X won";
                        cout << "X won" << endl;
                        }
              if(counter2 == -4)
                        {
                        result = "O won";
                        cout << "O won" << endl;
                        }
              }
          }
      if(result != "X won" && result != "O won" && draw(minefeild) == 16)
                result = "Draw";
      else if(result != "X won" && result != "O won" && draw(minefeild) <= 15)
                result = "Game has not completed";   
    
    
    

    //outfile.open("answer.txt");
    
            //for (int c = 0; c < cases; c++)
                outfile << "Case #" << j + 1 << ": " << result <<endl;
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}

/* ****** functions borrowed from ACSL Chess Queen *********************************/
/* ****** functions borrowed from ACSL Chess Queen *********************************/
/* ****** functions borrowed from ACSL Chess Queen *********************************/

int draw( char Board[ROW][COL])
{
    int counter = 0;
    for(int r = 0; r < ROW; r++)
         {   
          for (int c = 0; c < COL; c++)
              {
                   if(Board[r][c] == 'X' || Board[r][c] == 'O' || Board[r][c] == 'T')
                    counter ++;
              }
         }
         return counter;     
}

int lr(int n, int x, int y, char Board[ROW][COL])
{
        int z = 0, g = y, x2 = x, counter = 0;
        counter2 = 0;
        //check right
        for(x; x < ROW; x++)
        {
               
                      for(z; z <= n; z++)
                      {
                             if((y + z) >= 0 && (y + z) <= (ROW - 1))
                             {
                             if(Board[(x2)][(y + z)] == 'X'  || Board[(x2)][(y + z)] == 'T')
                                counter ++;
                             if(Board[(x2)][(y + z)] == 'O'  || Board[(x2)][(y + z)] == 'T')
                                counter2 --;
                           
                             }
                      }
        }
        
        //check left
        z = 1;
        for(g; g >= 0; g--) 
               {                     
                      for(z; z <= n; z++)
                      {
                             if((y - z) >= 0 && (y - z) <= (ROW - 1))
                             {
                             if(Board[(x2)][(y - z )] == 'X' || Board[(x2)][(y - z)] == 'T')
                               counter ++;
                             if(Board[(x2)][(y - z )] == 'O' || Board[(x2)][(y - z)] == 'T')
                               counter2 --;                  
                             }
                      }
               }
        
    return counter;    
}


int ud(int n, int x, int y, char Board[ROW][COL])  
{
   int z = 0, g = y, x2 = x, counter = 0;
   counter2 = 0;
        
        //check down
        for(x; x < ROW; x++)
        {
               
                      for(z; z <= n; z++)
                      {
                             if((x2 + z) >= 0 && (x2 + z) <= (ROW - 1))
                             {
                              if(Board[(x2 + z)][(y)] == 'X' || Board[(x2 + z)][(y)] == 'T')
                                counter ++;
                              if(Board[(x2 + z)][(y)] == 'O' || Board[(x2 + z)][(y)] == 'T')
                                counter2 --; 
                             }
                      }
        }
        
        //check up
        z = 1;
        for(g; g >= 0; g--) 
               {                     
                      for(z; z <= n; z++)
                      {
                             if((x2 - z) >= 0 && (x2 - z) <= (ROW - 1))
                             {
                              if(Board[(x2 - z)][(y )] == 'X' || Board[(x2 - z)][(y )] == 'T')
                                   counter ++; 
                              if(Board[(x2 - z)][(y )] == 'O' || Board[(x2 - z)][(y )] == 'T')
                                   counter2 --; 
                             }
                      }
               }
        return counter;  
}   

int diag(int n, int x, int y, char Board[ROW][COL]) 
{
     int z = 0, g = y, x2 = x, x3 = x, x4 = x, counter = 0;
     counter2 = 0;
        
        //check down, right
        for(x; x < ROW; x++)
        {
               
                      for(z; z <= n; z++)
                      {
                             if((x2 + z) >= 0 && (x2 + z) <= (ROW - 1) && (y + z) >= 0 && (y + z) <= (ROW - 1))
                             {
                              if(Board[(x2 + z)][(y + z)] == 'X' || Board[(x2 + z)][(y + z)] == 'T')
                                   counter ++;
                              if(Board[(x2 + z)][(y + z)] == 'O' || Board[(x2 + z)][(y + z)] == 'T')
                                   counter2 --;
                             }
                      }
        }
        
        
        
        //check up, left
        z = 1;
        for(x4; x4 < ROW; x4 ++)
        {
               
                      for(z; z <= n; z++)
                      {
                             if((x2 - z) >= 0 && (x2 - z) <= (ROW - 1) && (y - z) >= 0 && (y - z) <= (ROW - 1))
                             {
                              if(Board[(x2 - z)][(y - z)] == 'X' || Board[(x2 - z)][(y - z)] == 'T')
                                  counter ++;
                              if(Board[(x2 - z)][(y - z)] == 'O' || Board[(x2 - z)][(y - z)] == 'T')
                                  counter2 --;
                             }
                      }
        }
        
     return counter;
        
} 

int diag1(int n, int x, int y, char Board[ROW][COL]) 
{
    int z = 0, g = y, x2 = x, x3 = x, x4 = x, counter = 0;
    counter2 = 0;
    //check down, left
        z = 1;
        for(g; g >= 0; g--) 
        {
               
                      for(z; z <= n; z++)
                      {
                             if((x2 + z) >= 0 && (x2 + z) <= (ROW - 1) && (y - z) >= 0 && (y - z) <= (ROW - 1))
                             {
                              if(Board[(x2 + z)][(y - z)] == 'X' || Board[(x2 + z)][(y - z)] == 'T')
                                   counter ++;
                              if(Board[(x2 + z)][(y - z)] == 'O' || Board[(x2 + z)][(y - z)] == 'T')
                                   counter2 --;
                             }
                      }
        }
        
        //check up, right
        z = 0;
        for(x3; x3 < ROW; x3 ++)
        {
               
                      for(z; z <= n; z++)
                      {
                             if((x2 - z) >= 0 && (x2 - z) <= (ROW - 1) && (y + z) >= 0 && (y + z) <= (ROW - 1))
                             {
                              if(Board[(x2 - z)][(y + z)] == 'X' || Board[(x2 - z)][(y + z)] == 'T')
                                   counter ++;
                              if(Board[(x2 - z)][(y + z)] == 'O' || Board[(x2 - z)][(y + z)] == 'T')
                                   counter2 --;
                             }
                      }
        }
        
        return counter;
}
    


