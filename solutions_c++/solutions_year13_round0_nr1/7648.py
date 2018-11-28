#include <fstream>
using namespace std;

const int N = 6;
char a[N][N];

void initialize(int d[N][N]) {
    for(int i = 0; i <= 5; ++i) {
        for(int j = 0; j <= 5; ++j) {
            d[i][j] = 0;
        }
    }
}

int solve(char p) {
    int d[N][N];
    initialize(d);
    //rows
    for(int i = 1; i <= 4; ++i) {
        for(int j = 1; j <= 4; ++j) {
            if(a[i][j] == p || a[i][j] == 'T') {
                d[i][j] = d[i][j - 1] + 1;
            }
            else {
                d[i][j] = 0;
            }

            if(d[i][j] == 4) {
                return 1;
            }
        }
    }

    //columns
    initialize(d);
    for(int j = 1; j <= 4; ++j) {
        for(int i = 1; i <= 4; ++i) {
            if(a[i][j] == p || a[i][j] == 'T') {
                d[i][j] = d[i - 1][j] + 1;
            }
            else {
                d[i][j] = 0;
            }

            if(d[i][j] == 4) {
                return 1;
            }
        }
    }

    //first diagonal
    initialize(d);
    int sw = 1;
    for(int i = 1; i <= 4; ++i) {
        if(!(a[i][i] == p || a[i][i] == 'T')) {
            sw = 0;
            break;
        }
    }

    if(sw) {
        return 1;
    }

    //second diagonal

    sw = 1;
    for(int i = 1; i <= 4; ++i) {
        if( !(a[i][4 - i + 1] == p || a[i][4 - i + 1] == 'T')) {
            sw = 0;
            break;
        }
    }


    if(sw) {
        return 1;
    }

    return 0;
}

int main() {
    ifstream fin("date.in");
    ofstream fout("date.out");
    int t;
    fin >> t;
    for(int c = 1; c <= t; ++c) {
        for(int i = 1; i <= 4; ++i) {
            for(int j = 1; j <= 4; ++j) {
                fin >> a[i][j];
            }
        }

        fout << "Case #" << c << ": ";
        if(solve('X')) {
           fout << "X won\n";
           continue;
        }

        if(solve('O')) {
            fout << "O won\n";
            continue;
        }

        if(!solve('X') && !solve('Y')) {
            int sw = 0;
            for(int i = 1; i <= 4; ++i) {
                for(int j = 1; j <= 4; ++j) {
                    if(a[i][j] == '.') {
                        sw = 1;
                    }
                }
            }

            if(sw) {
                fout << "Game has not completed\n";
                continue;
            }
            else {
                fout << "Draw\n";
                continue;
            }
        }
    }

    return 0;

}
