#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

int check(char Map[][5], int X){
    int isWin = 0;
    for(int i = 0; i < 4; ++i){
        int isC = 1, isR = 1;
        for(int j = 0; j < 4; ++j){
            if(Map[i][j] != X && Map[i][j] != 'T'){
                isR = 0;
            }
            if(Map[j][i] != X && Map[j][i] != 'T'){
                isC = 0;
            }
        }
        if(isC || isR){
            isWin = 1;
        }
    }
    int isC = 1, isR = 1;
    for(int i = 0; i < 4; ++i){
        if(Map[i][i] != X && Map[i][i] != 'T'){
            isC = 0;
        }
        if(Map[i][3 - i] != X && Map[i][3 - i] != 'T'){
            isR = 0;
        }
    }
    isWin |= isC | isR;
    return isWin;
}

int count(char Map[][5]){
    int sum = 0;
    for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j) sum += Map[i][j] == '.';
    return sum;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas){
        char Map[5][5];
        for(int i = 0; i < 4; ++i){
            scanf("%s", Map[i]);
        }
        int mask = (check(Map, 'O') << 1) | (check(Map, 'X'));
        printf("Case #%d: ", cas);
        if(mask == 0){
            if(count(Map) == 0){
                puts("Draw");
            }
            else {
                puts("Game has not completed");
            }
        }
        if(mask == 2){
            puts("O won");
        }
        if(mask == 1) {
            puts("X won");
        }
    }
}
