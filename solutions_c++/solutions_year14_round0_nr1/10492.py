#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;

int main(){
    ifstream fin("A-small-attempt3.in");
    ofstream fout ("A-small-attempt3.out");
    int num;
    fin >> num;
    for (int i = 0; i < num; i++){
        int r;
        fin >> r;
        int s[16];
        for (int a = 0; a < 16; a++){
            fin >> s[a];
        }
        int c[4];
        for (int x = 0; x < 4; x++){
            c[x] = s[(r - 1) * 4 + x];
        }
        fin >> r;
        for (int a = 0; a < 16; a++){
            fin >> s[a];
        }
        int ans = 0;
        int n;
        for (int y = 0; y < 4; y++){
            for (int x = 0; x < 4; x++){
                if (c[x] == s[(r - 1) * 4 + y]){
                    ans++;
                    n = c[x];
                    break;
                }
            }
        }
        fout << "Case #" << i + 1 << ": ";
        if (ans > 1){
            fout << "Bad magician!";
        }else if (ans == 1){
            fout << n;
        }else{
            fout << "Volunteer cheated!";
        }
        fout << endl;
    }
}