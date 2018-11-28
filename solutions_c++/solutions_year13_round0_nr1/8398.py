#include <iostream>
#include <string>
#include <cstdio>
#include <fstream>

using namespace std;

int main()
{
    int t;
    freopen("input.txt", "r", stdin);
    freopen("outputt.txt", "w", stdout);
    cin >> t;
    int cases = 1;

    while(t--) {

        string s[4];

        for(int i = 0; i < 4; i++) {
            cin >> s[i];
        }
       /* if(cases == 184) {
            for(int i = 0; i < 4; i++) {
                cout << s[i] << endl;
            }
        }*/

        char flag = '?';
        bool flag1 = 0;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                    if(s[i][j] == 'T') {
                        if(i == 0 && j == 0) {
                            if(s[i+1][j] != '.' && s[i+1][j] == s[i+2][j] && s[i+2][j] == s[i+3][j]) {
                                flag = s[i+1][j];
                                break;
                            }
                            if(s[i][j+1] != '.' && s[i][j+1] == s[i][j+2] && s[i][j+2] == s[i][j+3]) {
                                flag = s[i][j+1];
                                break;
                            }
                            if(s[i+1][j+1] != '.' && s[i+1][j+1] == s[i+2][j+2] && s[i+2][j+2] == s[i+3][j+3]) {
                                flag = s[i+1][j+1];
                                break;
                            }
                        }
                        if(i == 0 && j == 3) {
                            if(s[i+1][j] != '.' && s[i+1][j] == s[i+2][j] && s[i+2][j] == s[i+3][j]) {
                                flag = s[i+1][j];
                                break;
                            }
                            if(s[i+1][j-1] != '.' && s[i+1][j-1] == s[i+2][j-2] && s[i+2][j-2] == s[i+3][j-3]) {
                                flag = s[i+1][j-1];
                                break;
                            }
                        }
                        else if(i == 0) {
                            if(s[i+1][j] != '.' && s[i+1][j] == s[i+2][j] && s[i+2][j] == s[i+3][j]) {
                                flag = s[i+1][j];
                                break;
                            }
                        }
                        else if(i != 0 && j == 0) {
                            if(s[i][j+1] != '.' && s[i][j+1] == s[i][j+2] && s[i][j+2] == s[i][j+3]) {
                                flag = s[i][j+1];
                                break;
                            }
                        }
                    }
                    if(s[i][j] == '.') {
                        flag1 = 1;
                        continue;
                    }
                    if(i == 0 && j == 0) {
                        if((s[i][j] == s[i][j+1] || s[i][j+1] == 'T') && (s[i][j] == s[i][j+2] || s[i][j+2] == 'T') && (s[i][j] == s[i][j+3] || s[i][j+3] == 'T')) {
                            flag = s[i][j];
                            break;
                        }
                        if((s[i][j] == s[i+1][j] || s[i+1][j] == 'T') && (s[i][j] == s[i+2][j] || s[i+2][j] == 'T') && (s[i][j] == s[i+3][j] || s[i+3][j] == 'T')) {
                            flag = s[i][j];
                            break;
                        }
                        if((s[i][j] == s[i+1][j+1] || s[i+1][j+1] == 'T') && (s[i][j] == s[i+2][j+2] || s[i+2][j+2] == 'T') && (s[i][j] == s[i+3][j+3] || s[i+3][j+3] == 'T')) {
                            flag = s[i][j];
                            break;
                        }
                    }
                    else if(i == 0 && j == 3) {
                        if((s[i][j] == s[i+1][j] || s[i+1][j] == 'T') && (s[i][j] == s[i+2][j] || s[i+2][j] == 'T') && (s[i][j] == s[i+3][j] || s[i+3][j] == 'T')) {
                            flag = s[i][j];
                            break;
                        }
                        if((s[i][j] == s[i+1][j-1] || s[i+1][j-1] == 'T') && (s[i][j] == s[i+2][j-2] || s[i+2][j-2] == 'T') && (s[i][j] == s[i+3][j-3] || s[i+3][j-3] == 'T')) {
                            flag = s[i][j];
                            break;
                        }
                    }
                    else if(i == 0) {
                        if((s[i][j] == s[i+1][j] || s[i+1][j] == 'T') && (s[i][j] == s[i+2][j] || s[i+2][j] == 'T') && (s[i][j] == s[i+3][j] || s[i+3][j] == 'T')) {
                            flag = s[i][j];
                            break;
                        }
                    }
                    else if(i != 0 && j == 0){
                        if((s[i][j] == s[i][j+1] || s[i][j+1] == 'T') && (s[i][j] == s[i][j+2] || s[i][j+2] == 'T') && (s[i][j] == s[i][j+3] || s[i][j+3] == 'T')) {
                            flag = s[i][j];
                            break;
                        }
                    }
                    else {
                        continue;
                    }
            }
            if(flag != '?') break;
        }

        if(flag == '?' && flag1) {
            cout << "Case #" << cases << ": " << "Game has not completed\n";
        }
        if(flag == 'X') {
            cout << "Case #" << cases << ": " << "X won\n";
        }
        if(flag == 'O') {
            cout << "Case #" << cases << ": " << "O won\n";
        }
        if(flag == '?' && !flag1) {
            cout << "Case #" << cases << ": " << "Draw\n";
        }
        cases++;
    }
    return 0;
}
