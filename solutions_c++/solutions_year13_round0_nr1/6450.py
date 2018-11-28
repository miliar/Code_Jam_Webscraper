#include <iostream>
#include <map>
#include <string>
#include <stdlib.h>
#include <cmath>
#include <cstdio>


using namespace std;
bool checkLetter(char letter,char toCheck)
{
    if((letter==toCheck)||(letter=='T'))
       {
           return true;
       }
       else
       {
           return false;
       }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w+",stdout);
    int T,i,j,k;
    char C;
    bool notFinished;
    string board[4];
    cin>>T;

    for(i=1;i<=T;i++)
    {
        cin>>board[0];
        cin>>board[1];
        cin>>board[2];
        cin>>board[3];

    notFinished=false;

    if((checkLetter(board[0][0],'X')&&checkLetter(board[0][1],'X')&&checkLetter(board[0][2],'X')&&checkLetter(board[0][3],'X'))||
       (checkLetter(board[1][0],'X')&&checkLetter(board[1][1],'X')&&checkLetter(board[1][2],'X')&&checkLetter(board[1][3],'X'))||
       (checkLetter(board[2][0],'X')&&checkLetter(board[2][1],'X')&&checkLetter(board[2][2],'X')&&checkLetter(board[2][3],'X'))||
       (checkLetter(board[3][0],'X')&&checkLetter(board[3][1],'X')&&checkLetter(board[3][2],'X')&&checkLetter(board[3][3],'X'))||
       (checkLetter(board[0][0],'X')&&checkLetter(board[1][0],'X')&&checkLetter(board[2][0],'X')&&checkLetter(board[3][0],'X'))||
       (checkLetter(board[0][1],'X')&&checkLetter(board[1][1],'X')&&checkLetter(board[2][1],'X')&&checkLetter(board[3][1],'X'))||
       (checkLetter(board[0][2],'X')&&checkLetter(board[1][2],'X')&&checkLetter(board[2][2],'X')&&checkLetter(board[3][2],'X'))||
       (checkLetter(board[0][3],'X')&&checkLetter(board[1][3],'X')&&checkLetter(board[2][3],'X')&&checkLetter(board[3][3],'X'))||
       (checkLetter(board[0][0],'X')&&checkLetter(board[1][1],'X')&&checkLetter(board[2][2],'X')&&checkLetter(board[3][3],'X'))||
       (checkLetter(board[0][3],'X')&&checkLetter(board[1][2],'X')&&checkLetter(board[2][1],'X')&&checkLetter(board[3][0],'X')))
       {
            cout<<"Case #"<<i<<": "<<"X won"<<endl;
            continue;
       }

if((checkLetter(board[0][0],'O')&&checkLetter(board[0][1],'O')&&checkLetter(board[0][2],'O')&&checkLetter(board[0][3],'O'))||
       (checkLetter(board[1][0],'O')&&checkLetter(board[1][1],'O')&&checkLetter(board[1][2],'O')&&checkLetter(board[1][3],'O'))||
       (checkLetter(board[2][0],'O')&&checkLetter(board[2][1],'O')&&checkLetter(board[2][2],'O')&&checkLetter(board[2][3],'O'))||
       (checkLetter(board[3][0],'O')&&checkLetter(board[3][1],'O')&&checkLetter(board[3][2],'O')&&checkLetter(board[3][3],'O'))||
       (checkLetter(board[0][0],'O')&&checkLetter(board[1][0],'O')&&checkLetter(board[2][0],'O')&&checkLetter(board[3][0],'O'))||
       (checkLetter(board[0][1],'O')&&checkLetter(board[1][1],'O')&&checkLetter(board[2][1],'O')&&checkLetter(board[3][1],'O'))||
       (checkLetter(board[0][2],'O')&&checkLetter(board[1][2],'O')&&checkLetter(board[2][2],'O')&&checkLetter(board[3][2],'O'))||
       (checkLetter(board[0][3],'O')&&checkLetter(board[1][3],'O')&&checkLetter(board[2][3],'O')&&checkLetter(board[3][3],'O'))||
       (checkLetter(board[0][0],'O')&&checkLetter(board[1][1],'O')&&checkLetter(board[2][2],'O')&&checkLetter(board[3][3],'O'))||
       (checkLetter(board[0][3],'O')&&checkLetter(board[1][2],'O')&&checkLetter(board[2][1],'O')&&checkLetter(board[3][0],'O')))
       {
            cout<<"Case #"<<i<<": "<<"O won"<<endl;
            continue;
       }

       for(j=0;j<4;j++)
       {
           for(k=0;k<4;k++)
           {
               if(board[j][k]=='.')
               {
                   notFinished=true;
                   break;
               }
           }
           if(notFinished)
            {
                break;
            }
       }

       if(notFinished)
       {
           cout<<"Case #"<<i<<": "<<"Game has not completed"<<endl;
           continue;
       }

       cout<<"Case #"<<i<<": "<<"Draw"<<endl;

    }
    return 0;
}
