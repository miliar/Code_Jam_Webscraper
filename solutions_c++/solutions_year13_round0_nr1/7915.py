#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int Judge();
char map[4][4];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, play, cnt = 0;
    scanf("%d", &T);
    gets(map[0]);
    while(T--){
        memset(map, 0, sizeof(map));
        for(int i = 0; i < 4; i++)
            scanf("%s", map[i]);
        ++cnt;
        printf("Case #%d: ", cnt);
        if(Judge() == 4)
            puts("Game has not completed");
        else if(Judge() == 3)
                puts("Draw");
        else if(Judge() == 2)
            puts("X won");
        else
            puts("O won");
    }
    return 0;
}
int Judge(){
    int X, O, X1, O1, play = 0;
    for(int i = 0; i < 4; i++){
        X = O = X1 = O1 = 0;
        for(int j = 0; j < 4; j++){
            if(map[i][j] == 'X' || map[i][j] == 'T')
                X++;
            if(map[i][j] == 'O' || map[i][j] == 'T')
                O++;
            if(map[j][i] == 'X' || map[j][i] == 'T')
                X1++;
            if(map[j][i] == 'O' || map[j][i] == 'T')
                O1++;
            if(map[i][j] == '.' || map[j][i] == '.')
                play = 1;
        }
        //printf("%d %d %d %d\n", X, X1, O, O1);
        if(X == 4 || X1 == 4)  return 2;
        if(O == 4 || O1 == 4)  return 1;
    }
    X = O = X1 = O1 = 0;
    for(int i = 0; i < 4; i++){
        if(map[i][i] == 'X' || map[i][i] == 'T')
            X++;
        if(map[i][i] == 'O' || map[i][i] == 'T')
            O++;
        if(map[i][3-i] == 'X' || map[i][3-i] == 'T')
            X1++;
        if(map[i][3-i] == 'O' || map[i][3-i] == 'T')
            O1++;
    }
    if(X == 4 || X1 == 4)  return 2;
    if(O == 4 || O1 == 4)  return 1;
    if(play == 1)   return 4;
    return 3;
}
