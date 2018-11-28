#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

bool checkDiag(vector<vector<char> > board, char a){
    int xc = 0; int tc = 0;
    for(int i=0;i<4;i++){
        if(board[i][i] == a)
            xc++;
        if(board[i][i] == 'T')
            tc++;
    }
    if(xc+tc == 4)
        return true;

    xc=0;tc=0;
    for(int i=0;i<4;i++){
        if(board[i][4-(i+1)] == a)
            xc++;
        if(board[i][4-(i+1)] == 'T')
            tc++;
    }
    if(xc+tc == 4)
        return true;
    else
        return false;
}

bool checkRow(vector<vector<char> > board, char a){
    int xc,tc;
    for(int i=0;i<4;i++){
        xc = 0; tc = 0;
        for(int j=0;j<4;j++){
            if(board[i][j] == a)
                xc++;
            if(board[i][j] == 'T')
                tc++;
        }
        if(xc+tc == 4)
            return true;
    }
    return false;
}

bool checkCol(vector<vector<char> > board, char a){
    int xc,tc;
    for(int i=0;i<4;i++){
        xc = 0; tc = 0;
        for(int j=0;j<4;j++){
            if(board[j][i] == a)
                xc++;
            if(board[j][i] == 'T')
                tc++;
        }
        if(xc+tc == 4)
            return true;
    }
    return false;
}

bool isComp(vector<vector<char> > board){
    int cnt = 0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(board[i][j] == '.')
                return false;
        }
    }
    return true;
}

int main() {
    ifstream fin;ofstream fout;
    vector<vector<char> > board;
    fin.open("input.in",ios::in);fout.open("output.out",ios::out);
    int amtTest;
    string line;
    fin >> amtTest;
    board.resize(4);
    for(int i=0;i<4;i++)
        board[i].resize(4);
    for(int k=0;k<amtTest;k++){
        for(int i=0;i<4;i++){
            fin >> line;
            for(int j=0;j<4;j++){
                board[i][j] = line[j];
            }
        }
        fout << "Case #" << k+1 << ": ";
        if(checkDiag(board,'X') || checkRow(board,'X') || checkCol(board, 'X'))
            fout << "X won\n";
        else if(checkDiag(board,'O') || checkRow(board,'O') || checkCol(board, 'O'))
            fout << "O won\n";
        else if(isComp(board))
            fout << "Draw\n";
        else if(!isComp(board))
            fout << "Game has not completed\n";
    }
	return 0;
}
