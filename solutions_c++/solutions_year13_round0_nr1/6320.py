#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

char tic[5][5];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int iCase = 1; iCase <= T; iCase ++ ){
        for(int i = 0; i <4; i ++ )
            scanf("%s",&tic[i]);
        bool xwin = false, owin = false,isFinish = true;
        int xcnt = 0, ocnt = 0, tcnt = 0;
        for(int i = 0; i < 4; i ++ ){
            xcnt =0; ocnt = 0;tcnt = 0;
            for(int j = 0; j < 4; j ++){
                if(tic[i][j] == 'X') xcnt ++;
                else if(tic[i][j] == 'T') tcnt++;
                else if(tic[i][j] == 'O') ocnt ++;
                else isFinish = false;
            }
            if(xcnt == 4 || (xcnt == 3 && tcnt == 1)) {xwin = true; break;}
            if(ocnt == 4 || (ocnt == 3 && tcnt == 1)) {owin = true; break;}
        }
        for(int j = 0; j < 4; j ++ ){
            xcnt =0; ocnt = 0;tcnt = 0;
            for(int i = 0; i < 4; i ++){
                if(tic[i][j] == 'X') xcnt ++;
                else if(tic[i][j] == 'T') tcnt++;
                else if(tic[i][j] == 'O') ocnt ++;
                else isFinish = false;
            }
            if(xcnt == 4 || (xcnt == 3 && tcnt == 1)) {xwin = true; break;}
            if(ocnt == 4 || (ocnt == 3 && tcnt == 1)) {owin = true; break;}
        }


        xcnt =0; ocnt = 0;tcnt = 0;
        for(int i = 0; i < 4; i ++ ){
            if(tic[i][i] == 'X') xcnt ++;
            else if(tic[i][i] == 'T') tcnt++;
            else if(tic[i][i] == 'O') ocnt ++;
            else isFinish = false;
        }
        if(xcnt == 4 || (xcnt == 3 && tcnt == 1)) xwin = true;
        if(ocnt == 4 || (ocnt == 3 && tcnt == 1)) owin = true;
        xcnt =0; ocnt = 0;tcnt = 0;
        for(int i = 0; i < 4; i ++ ){
            if(tic[i][3-i] == 'X') xcnt ++;
            else if(tic[i][3-i] == 'T') tcnt++;
            else if(tic[i][3-i] == 'O') ocnt ++;
            else isFinish = false;
        }
        if(xcnt == 4 || (xcnt == 3 && tcnt == 1)) xwin = true;
        if(ocnt == 4 || (ocnt == 3 && tcnt == 1)) owin = true;
        printf("Case #%d: ",iCase);
        if(xwin) printf("X won\n");
        else if(owin) printf("O won\n");
        else if(!isFinish) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
