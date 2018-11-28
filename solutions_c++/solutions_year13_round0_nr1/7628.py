#include <iostream>
#include <cstring>

using namespace std;

bool get_stat(char** b, char player) {
    bool row;
    for(int i=0;i<4;i++){
        row = true;
        for(int j=0;j<4;j++){
            if(!(b[i][j]==player || b[i][j] == 'T')) { /*cout << b[i][j];*/ row = false; }
        }
        if(row) return true;
    }
    //return row;
    for(int i=0;i<4;i++){
        row = true;
        for(int j=0;j<4;j++){
            if(!(b[j][i]==player || b[j][i] == 'T')) { /*cout << b[i][j];*/ row = false; }
        }
        if(row) return true;
    }
    //return row;
    row = true;
    for(int i=0;i<4;i++)
        if(!(b[i][i]==player || b[i][i] == 'T')) { /*cout << b[i][j];*/ row = false; }
    if(row) return true;

    row = true;
    for(int i=0;i<4;i++)
        if(!(b[i][3-i]==player || b[i][3-i] == 'T')) { /*cout << b[i][j];*/ row = false; }

    return row;
}

int main() {
    int notc;
    bool not_completed;
    cin >> notc;
    char** board = new char*[4];
    for(int i=0;i<4;i++) board[i] = new char[4];
    for(int i=0; i<notc; i++) {
        not_completed = false;
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                cin >> board[j][k];
                if(board[j][k] == '.') not_completed = true;
            }
        }

        cout << "Case #" << i+1 << ": ";
        bool x = get_stat(board,'X');
        bool o = get_stat(board,'O');
        if(x) cout << "X won" << endl;
        else if(o) cout << "O won" << endl;
        else {
            if(not_completed) cout << "Game has not completed" << endl;
            else cout << "Draw" << endl;
        }


    }
    //program ends...
    return 0;

}
