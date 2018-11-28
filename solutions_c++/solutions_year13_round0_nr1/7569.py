#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>
#include <sstream>

using namespace std;
typedef long long ll;

string solve(vector<string>& v)
{
    int row, col;
    row = v.size(), col = v[0].size();
    
    for(int y = 0; y < row; y++) {
        int X, O;
        bool draw = false;
        X = O = 0;
        for(int x = 0; x < col; x++) {
            if(v[y][x] == 'T')
                continue;
            else if(v[y][x] == 'X')
                X++;
            else if(v[y][x] == 'O')
                O++;
            else {
                draw = true;
                break;
            }
        }
        if(!draw and ((X and !O) or (!X and O))) {
            if(X) return "X won";
            else return "O won";
        }
    }

    for(int x = 0; x < col; x++) {
        int X, O;
        bool draw = false;
        X = O = 0;
        for(int y = 0; y < row; y++) {
            if(v[y][x] == 'T')
                continue;
            else if(v[y][x] == 'X')
                X++;
            else if(v[y][x] == 'O')
                O++;
            else {
                draw = true;
                break;
            }
        }
        if(!draw and ((X and !O) or (!X and O))) {
            if(X) return "X won";
            else return "O won";
        }
    }
    
    int X, O;
    bool draw = false;
    X = O = 0;
    for(int x = 0, y = 0; x < col; x++, y++) {
        if(v[y][x] == 'T')
            continue;
        else if(v[y][x] == 'X')
            X++;
        else if(v[y][x] == 'O')
            O++;
        else {
            draw = true;
            break;
        }
    }
    if(!draw and ((X and !O) or (!X and O))) {
        if(X) return "X won";
        else return "O won";
    }
    X = O = 0;
    draw = false;
    for(int x = col -1, y = 0; x >= 0; x--, y++) {
        if(v[y][x] == 'T')
            continue;
        else if(v[y][x] == 'X')
            X++;
        else if(v[y][x] == 'O')
            O++;
        else {
            draw = true;
            break;
        }
    }
    if(!draw and ((X and !O) or (!X and O))) {
        if(X) return "X won";
        else return "O won";
    }
   
    draw = true;
    for(int y = 0; y < row; y++) {
        for(int x = 0; x < col; x++) {
            if(v[y][x] == '.') {
                draw = false;
                break;
            }
        }
    }
   
    if(draw) return "Draw";
    else return "Game has not completed";
}

int main()
{
    int T;
    cin >> T;
    for(int c = 1; c <= T; c++) {
        vector<string> v;

        for(int i = 0; i < 4; i++) {
            string s;
            cin >> s;
            v.push_back(s);
        }
        cout << "Case #" << c << ": " << solve(v) << endl;;

    }
    return 0;
}

