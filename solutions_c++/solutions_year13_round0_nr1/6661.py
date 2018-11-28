#include<iostream>
#include<stdio.h>
using namespace std;
char tab[5][5];
inline void calc(int D){
    scanf("%s",tab[0]);
     scanf("%s",tab[1]);
      scanf("%s",tab[2]);
       scanf("%s",tab[3]);
       bool winX=false;
       bool winY = false;
       bool dot = false;
    for( int i =0; i <4;i++){
        int X=0;int Y =0; int T =0;
        int XX=0; int YY =0; int TT =0;
        for( int j =0; j <4 ; j++){
            if(tab[i][j]=='X')X++;
            if(tab[i][j]=='O')Y++;
            if(tab[i][j]=='T'){X++;Y++;}
            if(tab[j][i]=='X')XX++;
            if(tab[j][i]=='O')YY++;
            if(tab[j][i]=='T'){XX++;YY++;}
            if(tab[i][j]=='.')dot =true;
        }
        if( XX == 4) winX = true;
        if( YY  == 4) winY= true;
        if ( X == 4) winX = true;
        if ( Y == 4) winY=true;
    }
    {

    int X=0;int Y=0;
    int XX=0; int YY=0;
        for(int i =0; i < 4; i++){
            if(tab[i][i]=='X')X++;
            if(tab[i][i]=='O')Y++;
            if(tab[i][i]=='T'){X++;Y++;}
            if(tab[3-i][i]=='X')XX++;
            if(tab[3-i][i]=='O')YY++;
            if(tab[3-i][i]=='T'){XX++;YY++;}

        }
              if( XX == 4) winX = true;
        if( YY  == 4) winY= true;
        if ( X == 4) winX = true;
        if ( Y == 4) winY=true;
    }
    printf("Case #%d: ",D);
    if( winX && winY){printf("Draw\n");}
    if( winX && !winY){printf("X won\n");}
    if(!winX  && winY){printf("O won\n");}
    if(! winX && !winY && dot){printf("Game has not completed\n");}
    if(! winX && !winY && !dot){printf("Draw\n");}
}
int main(){
    int t;
    scanf("%d",&t);
    for(int i =0; i < t; i++){
        calc(i+1);
    }
}
