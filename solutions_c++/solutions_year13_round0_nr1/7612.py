#include <iostream>
#include <cstdio>

using namespace std;

char str[4][4];
int dir[8][2] = {0, 1 , 0,-1, 1,0, -1,0, 1,1, 1,-1, -1,-1, -1,1};
bool judge(char type , int x,int y) {
    for(int i = 0 ; i < 8 ; i ++) {
        int xx = x;
        int yy = y;
        int cnt = 1;
        int cc = 0;
        while(xx >= 0 && xx < 4 && yy >= 0 && yy < 4) {
            xx += dir[i][0];
            yy += dir[i][1];
            if(xx < 0 ||xx >= 4 || yy < 0 || yy >= 4)break;
            if(str[xx][yy] == type || str[xx][yy] == 'T') {
                cnt ++; 
                if(str[xx][yy] == 'T')cc ++;
            }
        }
        if(cnt == 4 &&cc <= 1)return true;
    }
}
int main() {
    int i,j,k,l;
    int cas;
    int cc = 1;
    freopen("A-large.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&cas);
    while(cas--) {
        for(i = 0 ; i < 4 ; i ++)scanf("%s",str[i]);
        bool flag = false;
        int win = -1;
        for(i = 0 ; i < 4 ; i ++) {
            for(j = 0 ; j < 4 ; j ++) {
                if(str[i][j] == '.')flag = true;
                if(judge(str[i][j] , i , j) && str[i][j] == 'X') {
                    win = 1;
                }
                else if(judge(str[i][j] , i , j) && str[i][j] == 'O') {
                    win = 0;
                }
            }
        }
        printf("Case #%d: ",cc);
        cc++;
        if(win == -1) {
            if(flag)puts("Game has not completed");
            else puts("Draw");
        }
        else if(win == 1){
            puts("X won");
        }
        else puts("O won");
    }
}