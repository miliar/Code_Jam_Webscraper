#include <iostream>
#include <fstream>
using namespace std;

enum {
    winX, winY, draw, gover,
};

char a[4][4];

ifstream in("input.txt");
ofstream out("output.txt");

bool win(char c) {
    int h = 0, v = 0;
    bool hasH = false, hasV = false;
    for(int i = 0; i < 4; i++) {
        h = 0;
        for(int j = 0; j < 4; j++)
            if (a[i][j] == c || a[i][j] == 'T')
                h++;
        hasH |= (h == 4);
    }
    for(int i = 0; i < 4; i++) {
        v = 0;
        for(int j = 0; j < 4; j++)
            if (a[j][i] == c || a[j][i] == 'T')
                v++;
        hasH |= (v == 4);
    }
    h = 0, v = 0;
    for(int i = 0; i < 4; i++) {
        h += (a[i][i] == c || a[i][i] == 'T');
        v += (a[i][3-i] == c || a[i][3-i] == 'T');
    }

    return hasH || hasV || (h == 4) || (v == 4);
}

int main() {
    int t;
    in>>t;
    for(int tt = 0; tt < t; tt++) {
        int emp = 0, x = 0, y = 0;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++) {
                in>>a[i][j];
                if (a[i][j] == 'X' || a[i][j] == 'T') x++;
                else if (a[i][j] == 'O' || a[i][j] == 'T') y++;
                else if (a[i][j] == '.') emp++;
            }
        bool winX = win('X');
        bool winY = win('O');
        if (emp == 0) {
            if (!winX && !winY)
                out<<"Case #"<<tt+1<<": "<<"Draw\n";
            else if (winX)
                out<<"Case #"<<tt+1<<": "<<"X won\n";
            else if (winY)
                out<<"Case #"<<tt+1<<": "<<"O won\n";
        } else {
            if (winX)
                out<<"Case #"<<tt+1<<": "<<"X won\n";
            else if (winY)
                out<<"Case #"<<tt+1<<": "<<"O won\n";
            else
                out<<"Case #"<<tt+1<<": "<<"Game has not completed\n";
        }
    }
    return 0;
}
