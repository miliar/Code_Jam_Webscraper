#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
    int t;
    cin >> t;
    char arr[4][4];
    for(int y = 1  ;y <= t ;y++){
     //   cout <<"\ny : "<< y << endl;
     bool Full = true;

    for(int i = 0 ; i < 4 ; ++i)
         for(int j = 0 ;j < 4 ; ++j){
          cin >> arr[i][j];
          if(arr[i][j] == '.')
            Full = false;
         }

    int cases = -1;
    // rows
    for(int i = 0 ; i < 4 ; ++i){
     int xcount = 0 , ocount = 0,tcount = 0;
         for(int j = 0 ;j < 4 ; ++j){
           xcount+=(arr[i][j] == 'X');
           ocount+=(arr[i][j] == 'O');
           tcount+=(arr[i][j] == 'T');
         }
         if(xcount == 4){cases = 1; break;}
         else if(ocount==4){cases = 2;  break;}
         else if(xcount == 3 && tcount == 1) {cases = 1; break;}
         else if(ocount==3 && tcount == 1){cases = 2;  break;}
    }
    if(cases == -1){
    // colums
    for(int i = 0 ; i < 4 ; ++i){
     int xcount = 0 , ocount = 0,tcount = 0;
         for(int j = 0 ;j < 4 ; ++j){
           xcount+=(arr[j][i] == 'X');
           ocount+=(arr[j][i] == 'O');
           tcount+=(arr[j][i] == 'T');
         }
         if(xcount == 4){cases = 1; break;}
         else if(ocount==4){cases = 2;  break;}
         else if(xcount == 3 && tcount == 1) {cases = 1; break;}
         else if(ocount==3 && tcount == 1){cases = 2;  break;}
    }
    }
    if(cases == -1){
    // Diagonal left to right
    int xcount = (arr[0][0] == 'X') +(arr[1][1] == 'X') + (arr[2][2] == 'X') + (arr[3][3] == 'X');
    int ocount = (arr[0][0] == 'O') +(arr[1][1] == 'O') + (arr[2][2] == 'O') + (arr[3][3] == 'O');
    int tcount = (arr[0][0] == 'T') +(arr[1][1] == 'T') + (arr[2][2] == 'T') + (arr[3][3] == 'T');
         if(xcount == 4){cases = 1; }
         else if(ocount==4){cases = 2; }
         else if(xcount == 3 && tcount == 1) {cases = 1;}
         else if(ocount==3 && tcount == 1){cases = 2;}
    }

    if(cases == -1){
    // Diagonal right to left
    int xcount = (arr[0][3] == 'X') +(arr[1][2] == 'X') + (arr[2][1] == 'X') + (arr[3][0] == 'X');
    int ocount = (arr[0][3] == 'O') +(arr[1][2] == 'O') + (arr[2][1] == 'O') + (arr[3][0] == 'O');
    int tcount = (arr[0][3] == 'T') +(arr[1][2] == 'T') + (arr[2][1] == 'T') + (arr[3][0] == 'T');
         if(xcount == 4){cases = 1;}
         else if(ocount==4){cases = 2;}
         else if(xcount == 3 && tcount == 1) {cases = 1;}
         else if(ocount==3 && tcount == 1){cases = 2;}
    }
        if(cases == 1)
        cout << "Case #"<<y<<": X won" << endl;
        else if(cases == 2)
        cout << "Case #"<<y<<": O won"<<endl;
        else if(Full)
        cout << "Case #"<<y<<": Draw"<<endl;
        else
        cout << "Case #"<<y<<": Game has not completed"<<endl;

    }

    return 0;
}
