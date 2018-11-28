#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

char a[5][5];

bool x_won(char a, char b, char c, char d){
    return ((a == 'X' || a == 'T') && (b == 'X' || b == 'T') &&
            (c == 'X' || c == 'T') && (d == 'X' || d == 'T'));
}

bool o_won(char a, char b, char c, char d){
    return ((a == 'O' || a == 'T') && (b == 'O' || b == 'T') &&
            (c == 'O' || c == 'T') && (d == 'O' || d == 'T'));
}

int main(){
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    bool X, O, completed;
    cin >> n;
    for (int i = 1; i <= n; i++){
        X = O = 0;
        completed = 1;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++){
                cin >> a[j][k];
                if (a[j][k] == '.')
                    completed = 0;
            }
        for (int j = 0; j < 4; j++){
            X = X || x_won(a[j][0], a[j][1], a[j][2], a[j][3]);
            X = X || x_won(a[0][j], a[1][j], a[2][j], a[3][j]);
            O = O || o_won(a[j][0], a[j][1], a[j][2], a[j][3]);
            O = O || o_won(a[0][j], a[1][j], a[2][j], a[3][j]);
        }
        X = X || x_won(a[0][0], a[1][1], a[2][2], a[3][3]);
        X = X || x_won(a[0][3], a[1][2], a[2][1], a[3][0]);
        O = O || o_won(a[0][0], a[1][1], a[2][2], a[3][3]);
        O = O || o_won(a[0][3], a[1][2], a[2][1], a[3][0]);
        if (X) cout << "Case #" << i << ": X won" << endl;
        else if (O) cout << "Case #" << i << ": O won" << endl;
        else if (X == O && X == 0 && completed) cout << "Case #" << i << ": Draw" << endl;
        else cout << "Case #" << i << ": Game has not completed" << endl;
    }

    return 0;
}
