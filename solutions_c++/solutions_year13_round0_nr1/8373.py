#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdio.h>

using namespace std;

#define SIZE 6

char map[SIZE][SIZE];

int cx, co;
int tx, ty;
int bl;

void ReadData (void){
    cx = co = 0;
    bl = 0;
    for (int x=0 ;x<4 ;x++){
        scanf ("%s",map[x]);
        for (int y=0 ;y<4 ;y++){
            if (map[x][y] == 'O')
                co++;
            else if (map[x][y] == 'X')
                cx++;
            else if (map[x][y] == 'T')
                tx = x, ty = y;
            else
                bl = 1;
        }
    }
    return ;
}
bool JudgeWin (char c){
    map[tx][ty] = c;
    int cnt;
    for (int x=0 ;x<4 ;x++){
        cnt = 0;
        for (int y=0 ;y<4 ;y++){
            if (map[x][y] == c)
                cnt++;
        }
        if (cnt == 4)
            return true;
    }
    for (int y=0 ;y<4 ;y++){
        cnt = 0;
        for (int x=0 ;x<4 ;x++){
            if (map[x][y] == c)
                cnt++;
        }
        if (cnt == 4)
            return true;
    }
    cnt = 0;
    for (int s=0 ;s<4 ;s++){
        if (map[s][s] == c)
            cnt++;
    }
    if (cnt == 4)
        return true;
    cnt = 0;
    for (int s=0 ;s<4 ;s++){
        if (map[s][3-s] == c)
            cnt++;
    }
    if (cnt == 4)
        return true;
    return false;
}
int main (){
    int t;
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);
    scanf ("%d",&t);
    for (int test=1 ;test<=t ;test++){
        ReadData ();
        printf ("Case #%d: ",test);
        if (cx > co){
            if (JudgeWin ('X')){
                printf ("X won\n");
                continue;
            }
        }
        else{
            if (JudgeWin ('O')){
                printf ("O won\n");
                continue;
            }
        }
        if (bl == 1)
            printf ("Game has not completed\n");
        else
            printf ("Draw\n");
    }
    return 0;
}
/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

*/
