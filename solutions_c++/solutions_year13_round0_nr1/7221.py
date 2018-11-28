#include<fstream.h>
using namespace std;
char board[4][4];
int C1;
fstream fout("Sample.out");
int BCount(char alpha, int x, int y, int mark)
{
     
     int ctr = 0;
     switch(mark)
     {
                 case 1 :  for(int i = 1; i < 4; i++)
                           {
                                  if(board[i][y] == alpha || board[i][y] == 'T')
                                                 continue;
                                  else
                                  {
                                                 ctr = 1;
                                                 break;
                                  }
                           }
                           if(!ctr)
                                   fout << "Case #" << C1 << ": " << alpha << " won";
                           break;
                 case 2 :  for(int j = 1; j < 4; j++)
                           {
                                   if(board[x][j] == alpha || board[x][j] == 'T')
                                                  continue;
                                   else
                                   {
                                       ctr = 1;
                                       break;
                                   }
                           }
                           if(!ctr)
                                   fout << "Case #" << C1 << ": " << alpha << " won";
                           break;
                 case 3 :  for(int i = 0, j = y; i < 4; i++,(y==3)?j--:j++)
                           {
                                   if(board[i][j] == alpha || board[i][j] == 'T')
                                                  continue;
                                   else
                                   {
                                       ctr = 1;
                                       break;
                                   }
                           }
                           if(!ctr)
                                   fout << "Case #" << C1 << ": " << alpha << " won";
                           break;
                 case 4 :  for(int i = 0; i < 4; i++)
                           {
                                   for(int j = 0; j < 4; j++)
                                           if(board[i][j] == '.')
                                           {
                                                          fout << "Case #" << C1 << ": " << "Game has not completed";
                                                          ctr = 1;
                                                          break;
                                           }
                                   if(ctr)
                                          break;
                           }
                           if(!ctr)
                                   fout << "Case #" << C1 << ": " << "Draw";
     }
                                           
     return ctr;
}                                                  
int main()
{
    fstream fin("Sample.in");
    
    int cases, ctr = 0;
    fin >> cases;
    for(C1 = 1; C1 <= cases; C1++)
    {
            ctr = 2;
            for(int x = 0; x < 4; x++)
                    for(int y = 0; y < 4; y++)
                            fin >> board[x][y];
            for(int y = 0; y < 4; y++)
            {
                    if(board[0][y] == 'X')
                                   ctr = BCount('X',0,y,1);
                    else if(board[0][y] == 'O')
                                   ctr = BCount('O',0,y,1);
                    else if(board[0][y] == 'T')
                    {
                         ctr = BCount('X',0,y,1);
                         if(ctr)
                                ctr = BCount('O',0,y,1);
                    }
                    if(!ctr)
                            break;
            }
            if(ctr)
            for(int x = 0; x < 4; x++)
            {
                    if(board[x][0] == 'X')
                                   ctr = BCount('X',x,0,2);
                    else if(board[x][0] == 'O')
                                   ctr = BCount('O',x,0,2);
                    else if(board[x][0] == 'T')
                    {
                         ctr = BCount('X',x,0,2);
                         if(ctr)
                                ctr = BCount('O',x,0,2);
                    }
                    if(!ctr)
                            break;
            }
            if(ctr)
            for(int y = 0; y < 4; y = y + 3)
            {
                    if(board[0][y] == 'X')
                                   ctr = BCount('X',0,y,3);
                    else if(board[0][y] == 'O')
                                   ctr = BCount('O',0,y,3);
                    else if(board[0][y] == 'T')
                    {
                         ctr = BCount('X',0,y,3);
                         if(ctr)
                                ctr = BCount('O',0,y,3);
                    }
                    if(!ctr)
                            break;
            }
            if(ctr)
                   ctr = BCount('T',0,0,4);
            fout<<'\n';
            
    }
}
