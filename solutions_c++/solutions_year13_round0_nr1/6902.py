#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int n;
    cin >> n;
    char tic[5][5];
    bool completed, solution;
    for(int tc = 1; tc <= n; tc++){
        completed = true;
        solution = false;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> tic[i][j];
                if(tic[i][j] == '.'){
                    completed = false;
                }
            }
        }
        //row and column check
        for(int i = 0; i < 4; i++){
            if((tic[i][0] == 'X' || tic[i][0] == 'T') && (tic[i][1] == 'X' || tic[i][1] == 'T') && (tic[i][2] == 'X' || tic[i][2] == 'T') && (tic[i][3] == 'X' || tic[i][3] == 'T')){
                printf("Case #%d: X won\n", tc);
                solution = true;
                break;
            }
            if((tic[i][0] == 'O' || tic[i][0] == 'T') && (tic[i][1] == 'O' || tic[i][1] == 'T') && (tic[i][2] == 'O' || tic[i][2] == 'T') && (tic[i][3] == 'O' || tic[i][3] == 'T')){
                printf("Case #%d: O won\n", tc);
                solution = true;
                break;
            }
            if((tic[0][i] == 'X' || tic[0][i] == 'T') && (tic[1][i] == 'X' || tic[1][i] == 'T') && (tic[2][i] == 'X' || tic[2][i] == 'T') && (tic[3][i] == 'X' || tic[3][i] == 'T')){
                printf("Case #%d: X won\n", tc);
                solution = true;
                break;
            }
            if((tic[0][i] == 'O' || tic[0][i] == 'T') && (tic[1][i] == 'O' || tic[1][i] == 'T') && (tic[2][i] == 'O' || tic[2][i] == 'T') && (tic[3][i] == 'O' || tic[3][i] == 'T')){
                printf("Case #%d: O won\n", tc);
                solution = true;
                break;
            }
        }
        if(solution){
            continue;
        }
        // diagonal check
        if((tic[0][0] == 'X' || tic[0][0] == 'T') && (tic[1][1] == 'X' || tic[1][1] == 'T') && (tic[2][2] == 'X' || tic[2][2] == 'T') && (tic[3][3] == 'X' || tic[3][3] == 'T')){
            printf("Case #%d: X won\n", tc);
            continue;
        }
        if((tic[0][0] == 'O' || tic[0][0] == 'T') && (tic[1][1] == 'O' || tic[1][1] == 'T') && (tic[2][2] == 'O' || tic[2][2] == 'T') && (tic[3][3] == 'O' || tic[3][3] == 'T')){
            printf("Case #%d: O won\n", tc);
            continue;
        }
        if((tic[0][3] == 'X' || tic[0][3] == 'T') && (tic[1][2] == 'X' || tic[1][2] == 'T') && (tic[2][1] == 'X' || tic[2][1] == 'T') && (tic[3][0] == 'X' || tic[3][0] == 'T')){
            printf("Case #%d: X won\n", tc);
            continue;
        }
        if((tic[0][3] == 'O' || tic[0][3] == 'T') && (tic[1][2] == 'O' || tic[1][2] == 'T') && (tic[2][1] == 'O' || tic[2][1] == 'T') && (tic[3][0] == 'O' || tic[3][0] == 'T')){
            printf("Case #%d: O won\n", tc);
            continue;
        }
        if(!completed){
            printf("Case #%d: Game has not completed\n", tc);
        }
        else{
            printf("Case #%d: Draw\n", tc);
        }
    }

    return 0;
}
