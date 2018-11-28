#include <iostream>

using namespace std;

char x[4][4];

int find_result() {
    int i, j, check, locx=-1, locy, ptr;
    
    for(i = 0; i < 4; i++) {
        for(j = 0; j < 4; j++) {
            if(x[i][j] == 'T') {
                locx = i;
                locy = j;
            }
        }
    }
    
    for(ptr = 0; ptr < 2; ptr++) {
        if(locx != -1) {
            if(ptr == 0) {
                x[locx][locy] = 'O';
            } else {
                x[locx][locy] = 'X';
            }
        }
        
        for(i = 0; i < 4; i++) {
            if(x[i][0] == 'X' && x[i][1] == 'X' && x[i][2] == 'X' && x[i][3] == 'X') {
                return 1;
            }
            if(x[0][i] == 'X' && x[1][i] == 'X' && x[2][i] == 'X' && x[3][i] == 'X') {
                return 1;
            }
            if(x[i][0] == 'O' && x[i][1] == 'O' && x[i][2] == 'O' && x[i][3] == 'O') {
                return 2;
            }
            if(x[0][i] == 'O' && x[1][i] == 'O' && x[2][i] == 'O' && x[3][i] == 'O') {
                return 2;
            }
        }
        
        if(x[0][0] == 'X' && x[1][1] == 'X' && x[2][2] == 'X' && x[3][3] == 'X') {
            return 1;
        }
        if(x[0][0] == 'O' && x[1][1] == 'O' && x[2][2] == 'O' && x[3][3] == 'O') {
            return 2;
        }
        
        if(x[0][3] == 'X' && x[1][2] == 'X' && x[2][1] == 'X' && x[3][0] == 'X') {
            return 1;
        }
        if(x[0][3] == 'O' && x[1][2] == 'O' && x[2][1] == 'O' && x[3][0] == 'O') {
            return 2;
        }
    }
    
    check = 0;
    for(i = 0; i < 4; i++) {
        for(j = 0; j < 4; j++) {
            if(x[i][j] == '.') {
                check = 1;
            }
        }
    }
    
    if(check == 1) {
        return 4;
    } else {
        return 3;
    }
}

int main() {
    int i, j, k, n, *res;
    
    cin >> n;
    
    res = new int[n];
    
    for(i = 0; i < n; i++) {
        for(j = 0; j < 4; j++) {
            for(k = 0; k < 4; k++) {
                cin >> x[j][k];
            }
        }
        cout << "\n";
        
        res[i] = find_result();
    }
    
    for(i = 0; i < n; i++) {
        cout << "Case #" << i+1 << ": ";
        if(res[i] == 1) {
            cout << "X won";
        } else if(res[i] == 2) {
            cout << "O won";
        } else if(res[i] == 3) {
            cout << "Draw";
        } else {
            cout << "Game has not completed";
        }
        cout << "\n";
    }
    
    return 0;
}
