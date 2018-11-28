#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<stdlib.h>
#define SIZE 4
#define SCALE 10
char Diagonal(char x[][SIZE]);
char Horizontal(char x[][SIZE]);
char Vertical(char x[][SIZE]);
char Continue(char x[][SIZE]);
using namespace std;
int main()
{
 ofstream output;
 ifstream input;
 int T;
 int k;
 int Case = 1;
 char consume;
 char board[SIZE][SIZE] = {'.'};
 input.open("A-small-attempt1.in");
 output.open("output.txt");
 input >> T;
cout << T;
 if(T>=1 && T<=SCALE)
  {
  for(k=1; k<=T; k++)
   {
    int i = 0;
    int j = 0;
    char read;
    while(i<SIZE)
    {
    j = 0;
      while(j<SIZE)
      {
         input >> read;
         if(read != '\n')
           {
             board[i][j] = read;
              j++;
           }     
      }
     i++;
    }
  
   char Decide = Diagonal(board);
// cout << k << " D " << Decide << "\n";
   if(Decide != 'z')
     {
        output << "Case #" << k << ": " << Decide << " won" << "\n";
        Case++;
     }   
   else
     {
       Decide = Vertical(board);
// cout << k << " V " << Decide << "\n"; 
       if(Decide != 'z')
    	 {
       	 output << "Case #" << k << ": " << Decide << " won" << "\n";
       	 Case++;
    	 }
         else
           {
             Decide = Horizontal(board);
  //      cout << k << " H " << Decide << "\n";  
            if(Decide != 'z') 
                 {
       		  output << "Case #" << k << ": " << Decide << " won" << "\n";
      		   Case++;
        	 }    
               else
                 {
                   Decide = Continue(board);
                   if(Decide != 'z')
                     {
                      output << "Case #" << k << ": " << "Game has not completed" << "\n"; 
                      Case++;
                     }
                    else
                       {
                       output << "Case #" << k << ": " << "Draw" << "\n";
                       }
                 }   
 
           }
     }
   
    }
  }
 else
   exit(1);
   input.close();
 return 0;
}

char Diagonal(char board[][SIZE])
{
  char victor_i;
  char victor_j;
  int i,j;
 int vic_set_i = 0;
 int vic_set_j = 0;
  int T_count_i = 0;
  int T_count_j = 0;
  int count_i = 0;
  int count_j = 0;
  for(i=1; i<SIZE; i++)
     {
            if(((board[i][i] == board[i-1][i-1]) || (board[i][i] == 'T') || (board[i-1][i-1] == 'T')) && board[i][i] != '.' && board[i-1][i-1] != '.')
              count_i++;
            else 
               break;
            if((board[i][i] != 'T') || (board[i][i] != '.') && (vic_set_i != 1))
              {
                 victor_i = board[i][i];
                 vic_set_i = 1;
                }
            if(board[i-1][i-1] == 'T')
              T_count_i++;
     }
    
      for(j=1; j<SIZE; j++)
     { 
            if(((board[j][SIZE-1-j] == board[j-1][SIZE-j]) || (board[j][SIZE-1-j] == 'T') || (board[j-1][SIZE-j] == 'T')) && board[j][SIZE-1-j] != '.' && board[j-1][SIZE-j] != '.')
              count_j++;
            else
               break;
            if((board[j][SIZE-1-j] != 'T') && (board[j][SIZE-1-j] != '.') && vic_set_j != 1)
            {
               victor_j = board[j][SIZE-1-j];
                vic_set_j = 1;
            }
           if(board[j-1][SIZE-j] == 'T')
                T_count_j++;
     }

     if(count_i==SIZE-1 && (T_count_i <=1) && (victor_i != '.') && (victor_i != 'T'))
     return victor_i;
      else if(count_j == SIZE-1 && (T_count_j <=1) && (victor_j != '.') && (victor_j != 'T'))
      return victor_j;
      else
         return 'z';

}

char Vertical(char board[][SIZE])
{
int i=0;
int j=0;
int count;
char victor;
int T_count = 0;
for(i=0; i<SIZE; i++)
   {
    count = 0;
    T_count = 0;
    for(j=1; j<SIZE; j++)
      {
        if(((board[j][i] == board[j-1][i]) || (board[j][i] == 'T') || (board[j-1][i]) == 'T') && board[j][i] != '.' && board[j-1][i] != '.')
         count++;
        if(board[j][i] != 'T' && board[j][i] != '.')
        victor = board[j][i];
         if(board[j-1][i] == 'T')
           T_count++;
          
      }
   if(count == 3) break; 
  }
// cout << " Lm" << i << endl;
 if(count == 3 && (T_count <=1))
 return victor;
else
 return 'z';
}

char Horizontal(char board[][SIZE])
{
  int i=0; 
  int j=0;
  int count;
  char victor;
  int T_count = 0;
  for(i=0; i<SIZE; i++)
   {
    count = 0;
    T_count = 0;
    for(j=1; j<SIZE; j++)
      {
        if(((board[i][j] == board[i][j-1]) || (board[i][j] == 'T') || (board[i][j-1]) == 'T') && board[i][j] != '.' && board[i][j-1]!= '.')
         count++;
        if(board[i][j] != 'T' && board[i][j] != '.')
        victor = board[i][j];
         if(board[i][j-1] == 'T')
          T_count++;
      }
   if(count == 3) break;
  }
  
if(count == 3 && (T_count <= 1))
 return victor;
else
 return 'z';
}

char Continue(char board[][SIZE]) 
{
  int i,j;
  int count = 0;
  for(i=0; i<SIZE; i++)
   {
     for(j=0; j<SIZE; j++)
     {
       if(board[i][j] == '.')
          {
            count++;
              break; 
          }
     }
      if(count == 1)
        break;
   }

  if(count == 1)
   return 'c';
  else
   return 'z';
}
