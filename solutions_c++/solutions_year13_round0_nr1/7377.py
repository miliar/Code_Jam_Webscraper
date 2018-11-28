#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
bool check(char c, vector< vector<char> > &board, int x, int y){
    if(x < 0 || x > 4 || y < 0 || y > 4) return false;
    int horizon = 0;
    int vertical = 0;
    int dia1 = 0;
    int dia2 = 0;
    for(int i = 0; i < 4; i++){
        if(board[i][y] == c || board[i][y] == 'T') vertical++;
    }
    if(vertical == 4){
        //cout << "Char " << c << " vertical " << " X: " << x << " Y:" << y << endl;
        return true;
    }
    for(int j = 0; j < 4; j++){
        if(board[x][j] == c || board[x][j] == 'T') horizon++;
    }
    if(horizon == 4) {
        //cout << "Char " << c << " horizon " << " X: " << x << " Y:" << y << endl;
        return true;
    }
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(x - i == y - j && (board[i][j] == c || board[i][j] == 'T')){
                dia1++;
            }
            if(x - i == -(y -j) && (board[i][j] == c || board[i][j] == 'T')){
                dia2++;
            }
        }
    }
    if(dia1 == 4 || dia2 == 4) {
        return true;
    }
    return false;
}
string solve(int caseNo, vector< vector<char> > &board){
    caseNo++;
    bool flag = false;
    stringstream ss;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(board[i][j] == '.') flag = true;
            if(check('X', board, i, j) == true){
                ss << "Case #" << caseNo << ": X won" ;
                return ss.str();
            }
            if(check('O', board, i, j) == true){
                ss << "Case #" << caseNo << ": O won" ;
                return ss.str();
            }
        }
    }
    if(flag == true){
        ss << "Case #" << caseNo << ": Game has not completed" ;
    }else{
        ss << "Case #" << caseNo << ": Draw" ;
    }
    return ss.str();
}

int main(){
    int num = 0;
    cin >> num;
    int i = 0; 
    int dump = 0;
    vector<string> ans;
    while(i < num){
        vector< vector<char> > board(4, vector<char>(4));
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                cin >> board[j][k];
            }
        }
        ans.push_back(solve(i, board));
        i++;
    }
    for(int i = 0; i < num; i++){
        cout << ans[i] << endl;
    }
}
