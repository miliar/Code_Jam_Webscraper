#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

string str[5];

int check(char a, char b)
{
    if(a==b || a=='T') return 1;
    return 0;
}

int Horizontally(char ch)
{
    int flag;
    for(int i=0; i<4; i++)
    {
    flag = 1;
    for(int j=0; j<4; j++)
    {
         if(str[i][j] != 'T' && str[i][j] != ch)
         flag = 0;
    }
    if(flag)
    return 1;
    }
    return 0;
}

int Vertically(char ch)
{
    int flag;
    for(int j=0; j<4; j++)
    {
    flag = 1;
    for(int i=0; i<4; i++)
    {
         if(str[i][j] != 'T' && str[i][j] != ch)
         flag = 0;
    }
    if(flag)
    return 1;
    }
    return 0;
}

int Diagonally(char ch)
{
    //left
    if( check(str[0][0], ch) && check(str[1][1], ch) && check(str[2][2], ch) && check(str[3][3], ch) ) return 1;
    
    //right
    if( check(str[0][3], ch) && check(str[1][2], ch) && check(str[2][1], ch) && check(str[3][0], ch) ) return 1;
    
    return 0;
}

int Wins(char ch)
{
    if( Horizontally(ch) ) return 1;
    else if( Vertically(ch) ) return 1;
    else if( Diagonally(ch) ) return 1;
    return 0;
}

int isNotFilled()
{
    for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
    if(str[i][j] == '.') return 1;
    return 0;
}

main()
{
      int testCases;
      string output;
      scanf("%d",&testCases);
      for(int tc=1; tc<=testCases; tc++)
      {
           for(int i=0; i<4; i++)
           cin>>str[i];
           
           if(Wins('O')) output = "O won";
           else if(Wins('X')) output = "X won";
           else if(isNotFilled()) output = "Game has not completed";
           else output = "Draw";           
           cout<<"Case #"<<tc<<": "<<output<<endl;
      }
}
