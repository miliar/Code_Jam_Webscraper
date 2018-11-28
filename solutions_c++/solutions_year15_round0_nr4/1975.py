#include <iostream>
#include <fstream>
#include <string>
#define MAX_T 100
#define MAX_X 20
#define MAX_C 20
#define MAX_R 20
using namespace std;

ifstream fin ("D-small-attempt4.in");
ofstream fout ("results.txt");
int T;
bool richard[MAX_X+1][MAX_R+1][MAX_C+1];

void init();
void read();
string solve(int X, int R, int C);
void write(int caseNum, string ans);

int main(){
    init();
    read();
    return 0;
}

void init(){
    for(int x = 1; x <= MAX_X; x++){
        for(int r = 1; r <= MAX_R; r++){
            for(int c = 1; c <= MAX_C; c++){
                if(x > max(r,c)) richard[x][r][c] = true;
                if((r*c)%x != 0) richard[x][r][c] = true;
            }
        }
    }

    richard[3][1][3] = true;
    richard[4][1][4] = true;
    richard[4][2][4] = true;


    for(int x = 1; x <= 4; x++){
        for(int r = 1; r <= 4; r++){
            for(int c = r; c <= 4; c++){
                cout << x << "," << r << "," << c << ": " << richard[x][r][c] << endl;
            }
        }
    }
}

string solve(int X, int R, int C){
    if(R > C){
        int t = R;
        R = C;
        C = t;
    }
    if(richard[X][R][C]) return "RICHARD";
    /*if((R*C)%X != 0) return "RICHARD";
    if(X > R*C) return "RICHARD";
    if(X > C) return "RICHARD";
    if(X >= 3 && (R*C)%X == 0) return "RICHARD";*/

    return "GABRIEL";
}

void read(){
    int X, R, C;
    fin >> T;
    for(int i = 0; i < T; i++){
        fin >> X >> R >> C;
        write(i, solve(X,R,C));
    }
    fin.close();
    fout.close();
}

void write(int caseNum, string ans){
    fout << "Case #" << caseNum+1 << ": " << ans << endl;
}
