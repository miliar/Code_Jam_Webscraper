#include<stdio.h>
#include<string.h>
#include<iostream>
#include<sstream>
using namespace std;

bool checkTicTacToe(char str[][5], int);

int main()
{
   int N=0,i=0;
   char str[4][5];
   string str1;
   std::getline(std::cin, str1);                 //get each line
   stringstream(str1) >> N;

   while(i++ < N)
   {
     int j=0;
     while(j< 4)
     {
     	std::getline(std::cin, str1);                 //get each line
     	strcpy(str[j], str1.c_str());
        j++;
     }
     if(!checkTicTacToe(str, i))
     {
     cout<<"Case #"<<i<<": Game has not completed\n";
     }
     if(i<N)
     std::getline(std::cin, str1);                 //get each line
     
   }
   return 0;
}

bool checkTicTacToe( char str[][5], int N)
{
    int i=0, j=0;
    int irowCountX=0, irowCountO=0, irowCountT=0, irowCountEm=0;
    int icolCountX=0, icolCountO=0, icolCountT=0, icolCountEm=0;

    for(i=0 ;i<4; i++)
    {
       irowCountX=0, irowCountO=0, irowCountT=0, irowCountEm=0;
       icolCountX=0, icolCountO=0, icolCountT=0, icolCountEm=0;

       for(j=0; j<4; j++)
       {
          if(str[i][j]== 'X')
             irowCountX++;
          if(str[j][i]== 'X')
             icolCountX++;
          if(str[i][j]== 'O')
             irowCountO++;
          if(str[j][i]== 'O')
             icolCountO++;
          if(str[i][j]== 'T')
             irowCountT++;
          if(str[j][i]== 'T')
             icolCountT++;
          if(str[i][j] == '.' || str[j][i]== '.')  //for Empty
          {
               irowCountEm++;
          }
       }
       
       if(irowCountX == 4 || (irowCountX==3 && irowCountT==1)|| icolCountX == 4 || (icolCountX==3 && icolCountT==1))
       {
             cout<<"Case #"<<N<<": X won"<<"\n";
             return true;
       }
       else if(irowCountO == 4 || (irowCountO==3 && irowCountT==1)|| icolCountO == 4 || (icolCountO==3 && icolCountT==1))
       {
             cout<<"Case #"<<N<<": O won"<<"\n";
             return true;
       }
     }
                 //do for diagnolsa
     int iDiaCountX=0, iDiaCountO=0, iDiaCountT=0, iDiaCountEm=0;
     int iDia2CountX=0, iDia2CountO=0, iDia2CountT=0, iDia2CountEm=0;
     for(i=0; i<4; i++)
     {
         if(str[i][i] == 'X') iDiaCountX++;
         else if(str[i][i] == 'O') iDiaCountO++;
         else if(str[i][i] == 'T') iDiaCountT++; 
     }
     if(iDiaCountX == 4 || (iDiaCountX==3 && iDiaCountT==1))
     {
         cout<<"Case #"<<N<<": X won\n";
         return true;
     }
     if(iDiaCountO == 4 || (iDiaCountO==3 && iDiaCountT==1))
     {
         cout<<"Case #"<<N<<": O won\n";
         return true;
     }
     j =3;
     for(i=0; i<4; i++)
     {
         if(str[i][j] == 'X') iDia2CountX++;
         else if(str[i][j] == 'O') iDia2CountO++;
         else if(str[i][j] == 'T') iDia2CountT++; 
         j--;
     }
     if(iDia2CountX == 4 || (iDia2CountX==3 && iDia2CountT==1))
     {
         cout<<"Case #"<<N<<": X won\n";
         return true;
     }
     if(iDia2CountO == 4 || (iDia2CountO==3 && iDia2CountT==1))
     {
         cout<<"Case #"<<N<<": O won\n";
         return true;
     }
     if(irowCountEm ==0)
     {
         cout<<"Case #"<<N<<": Draw\n";
         return true;
     }
    return false;
}

