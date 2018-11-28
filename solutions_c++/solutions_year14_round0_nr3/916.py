#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int maze[55][55];
int R, C, M, blank;
void draw(){
    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            if(maze[i][j] == 2)cout << "c";
            else if(maze[i][j] == 1) cout << ".";
            else if(maze[i][j] == 0) cout << "*";
        }
        cout << endl;
    }
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%d%d%d", &R, &C, &M);
        blank = R * C - M;
        printf("Case #%d:\n", ++cas);
        memset(maze, 0, sizeof(maze));
        maze[0][0] = 2;
        if(blank == 1){
            draw();
            continue;
        }
        if(R == 1){
            for(int i = 1; i < blank; i++){
                maze[0][i] = 1;
            }
            draw();
            continue;
        }
        if(C == 1){
            for(int i = 1; i < blank; i++){
                maze[i][0] = 1;
            }
            draw();
            continue;
        }
        if(blank == 2 || blank == 3 || blank == 5 || blank == 7){
            printf("Impossible\n");
            continue;
        }
        if(R == 2){
            if(blank % 2){
                printf("Impossible\n");
            }
            else{
                maze[1][0] = 1;
                int col = blank / 2;
                for(int i = 1; i < col; i++){
                    maze[0][i] = 1;
                    maze[1][i] = 1;
                }
                draw();
            }
            continue;
        }
        if(C == 2){
            if(blank % 2){
                printf("Impossible\n");
            }
            else{
                maze[0][1] = 1;
                int col = blank / 2;
                for(int i = 1; i < col; i++){
                    maze[i][0] = 1;
                    maze[i][1] = 1;
                }
                draw();
            }
            continue;
        }
        if(blank == 4){
            maze[0][1] = maze[1][0] = maze[1][1] = 1;
            draw();
            continue;
        }
        if(blank % 2 == 0){
            //cout << "blank " << blank << endl;
            int col = (blank - 2) / 2;
            if(col < C){
                for(int i = 0; i < col; i++){
                    maze[0][i] = maze[1][i] = 1;
                }
                maze[0][0] = 2;
                maze[2][0] = maze[2][1] = 1;
            }
            else{
                int row = blank / C;
                int rest = blank % C;
                for(int i = 0; i < C; i++){
                    for(int j = 0; j < row; j++){
                        maze[j][i] = 1;
                    }
                }
                for(int i = 0; i < rest; i++){
                    maze[row][i] = 1;
                }
                if(rest == 1){
                    maze[row][rest] = 1;
                    maze[row-1][C-1] = 0;
                }
                maze[0][0] = 2;
            }
        }
        else{
            //cout << "blank " << blank << endl;
            int col = (blank - 3) / 2;
            if(col < C){
                for(int i = 0; i < col; i++){
                    maze[0][i] = maze[1][i] = 1;
                }
                maze[0][0] = 2;
                maze[2][0] = maze[2][1] = maze[2][2] = 1;
            }
            else{
                int row = blank / C;
                int rest = blank % C;
                //cout << row << " " << rest << endl;
                for(int i = 0; i < C; i++){
                    for(int j = 0; j < row; j++){
                        maze[j][i] = 1;
                    }
                }
                for(int i = 0; i < rest; i++){
                    maze[row][i] = 1;
                }
                if(rest == 1){
                    maze[row][rest] = 1;
                    maze[row-1][C-1] = 0;
                }
                maze[0][0] = 2;
            }
        }
        draw();
    }
    return 0;
}
