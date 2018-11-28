// clang++ -W -Wall -O3 *.cpp
// ./a.out < in

#include <iostream>
#include <cstring>

#define N 4

using namespace std;

char board[N][N];
int ti = -1, tj = -1;

bool won(char p) {
    if (ti != -1 && tj != -1)
        board[ti][tj] = p;

    bool diag1 = true, diag2 = true;
    for(int k = 0; k < N; k++) {
        int l;
        for(l = 0; l < N; l++) { // horizontal
            if(board[l][k] != p)
                break;
        }
        if (l == N) return true;
        
        for(l = 0; l < N; l++) { // vertical
            if(board[k][l] != p)
                break;
        }
        if (l == N) return true;
        
        diag1 &= (board[k][k] == p);
        diag2 &= (board[k][N-k-1] == p);
    }
    return diag1 || diag2;
}

string search() {
    if (won('X'))
        return "X won";
    if (won('O'))
        return "O won";
    if (memchr(board, '.', N*N) != NULL)
        return "Game has not completed";
    return "Draw";
}

int main() {
    int T;
    cin >> T;
    
    for(int t = 1; t <= T; t++) {
        ti = -1;
        tj = -1;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j< N; j++) {
                cin >> board[i][j];
                if (board[i][j] == 'T') {
                    ti = i;
                    tj = j;
                }
            }
            //cout << board[i][0] << board[i][1] << board[i][2] << board[i][3] << endl;
        }

        cout << "Case #" << t << ": " << search() << endl;
    }
}
