#include<stdio.h>
using namespace std;
char board[10][10];
bool empty;
void init(){
    empty = false;
    char s[10];
    for(int i=0; i<4; ++i){
        scanf("%s",board[i]);
        for(int j=0; j<4; ++j)
            if(board[i][j]=='.')    empty = true;
        //printf("%s\n",board[i]);
    }
}
bool judge(char who){
    //x is who

    //hang
    for(int i=0; i<4; ++i){
        int sum = 0;
        for(int j=0; j<4; ++j)
            if(board[i][j]==who || board[i][j]=='T')
                sum++;
        if(sum==4)  return true;
    }

    //lie
    for(int j=0; j<4; ++j){
        int sum = 0;
        for(int i=0; i<4; ++i)
            if(board[i][j]==who || board[i][j]=='T')
                sum++;
        if(sum==4)  return true;
    }

    //dui1
    for(int i=0; i<4; ++i){
        int sum = 0;
        for(int j=0; j<4; ++j)
            if(board[j][j]==who || board[j][j]=='T')
                sum++;
        if(sum==4)  return true;
    }

    //dui2
    for(int i=0; i<4; ++i){
        int sum = 0;
        int x=0,y=3;
        for(int j=0; j<4; ++j){
            if(board[x][y]==who || board[x][y]=='T')
                sum++;
            x++; y--;
        }
        if(sum==4)  return true;
    }
    return false;
}
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,Case=1;
    scanf("%d",&T);
    while(T--){
        init();
        bool X = judge('X');
        bool O = judge('O');
        printf("Case #%d: ",Case++);
        if(X==false && O==false){
            if(empty)   printf("Game has not completed\n");
            else        printf("Draw\n");
        }
        else{
            if(X)   printf("X won\n");
            else    printf("O won\n");
        }
    }
    return 0;
}
