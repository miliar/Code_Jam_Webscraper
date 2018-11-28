#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

char grid[5][5];

bool oflag, xflag;

void reset()
{
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            grid[i][j] = '.';
        }
    }
}

void chkvrtcl(int i){
    int sum = int(grid[0][i] + grid[1][i] + grid[2][i] + grid[3][i]);
    if((sum == (3 * int('X') + int('T'))) || sum == (4 * int('X'))){xflag = true; return;}
    if((sum == (3 * int('O') + int('T'))) || sum == (4 * int('O'))){oflag = true; return;}
}

void chkhorizontal(int i){
    int sum = int(grid[i][0] + grid[i][1] + grid[i][2] + grid[i][3]);
    if((sum == (3 * int('X') + int('T'))) || sum == (4 * int('X'))){xflag = true; return;}
    if((sum == (3 * int('O') + int('T'))) || sum == (4 * int('O'))){oflag = true; return;}
}

void chkdiagonal(){
    int sum = int(grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]);
    if((sum == (3 * int('X') + int('T'))) || sum == (4 * int('X'))){xflag = true; return;}
    if((sum == (3 * int('O') + int('T'))) || sum == (4 * int('O'))){oflag = true; return;}

    sum = int(grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0]);

    if((sum == (3 * int('X') + int('T'))) || sum == (4 * int('X'))){xflag = true; return;}
    if((sum == (3 * int('O') + int('T'))) || sum == (4 * int('O'))){oflag = true; return;}
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int t, freespace;
    char in;

    cin >> t;

    for(int i = 1; i <= t; i++){
        cout << "Case #" << i << ": ";
        oflag = false; xflag = false;
        freespace = 0;

        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                cin >> grid[j][k];
                if(grid[j][k] == '.'){
                    freespace++;
                }
            }
        }

        chkdiagonal();
        if(oflag) {cout << "O won" << endl; continue;}
        else if(xflag) {cout << "X won" << endl; continue;}

        for(int j = 0; j < 4; j++){
            chkvrtcl(j);
            chkhorizontal(j);
            if(oflag || xflag) break;
        }

        if(oflag) {cout << "O won" << endl; continue;}
        else if(xflag) {cout << "X won" << endl; continue;}

        if(!freespace) cout << "Draw" << endl;
        else {cout << "Game has not completed" << endl;}
    }


    return 0;
}
