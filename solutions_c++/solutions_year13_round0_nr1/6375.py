#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
 int t,k=0;
 char board[4][4];
 while(t--)
 {k++;
     char ld[4],rd[4];
     for(int i=0;i<4;i++)
    { scanf("%s",board[i]);
    ld[i]=board[i][i];
    rd[i]=board[3-i][3-i];
    }

     cout<<"Case #"<<k<<": ";
      int flag=0;
     // check in horizonat
     for(int i=0;i<4;i++)
     {
         if(board[i]=="XXXT" || board[i]=="TXXX" || board[i]=="XXXX" || board[i]=="XTXX" || board[i]=="XXTX")
         {
             cout<<"X won"<<endl;flag=1;
             break;
         }
         else if(board[i]=="OOOO" || board[i]=="OOOT" ||board[i]=="OOTO" || board[i]=="OTOO" ||board[i]=="TOOO")
         {
             cout<<"O won"<<endl;flag=1;
             break;
         }
         else if(ld=="XXXX" || ld =="XXXT"|| ld=="XXTX" || ld=="XTXX" || ld=="TXXX")
         {
             cout<<"X won"<<endl;flag=1;
             break;
         }
         else if(rd=="OOOO" || rd=="OOOT" || rd=="OOTO" || rd=="OTOO" || rd=="TOOO")
         {
             cout<<"O won"<<endl;
             flag=1;
             break;
         }


     }

     if(flag==0)
     {
         for(int i=0;i<4;i++)
         {
             for(int j=0;j<4;j++)
             {
                 if(board[i][j]=='.')
                 {
                     cout<<"Game has not completed"<<endl; flag=1;
                     break;
                 }
             }
            if(flag==1)
            break;
         }
        if(flag==0)
        {
            cout<<"Draw"<<endl;
        }
     }

 }
 return 0;
}
