//
//  main.cpp
//  GCJ
//
//  Created by 闫旭 on 13-4-13.
//  Copyright (c) 2013年 闫旭. All rights reserved.
//
#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
    int mm;
//    freopen("A-large.in","r",stdin);
//    freopen("output.txt", "w", stdout);
    std::cin >> mm;
    for (int s = 1; s<=mm; ++s){
        char matrix[1001][1001];
        bool flag_com = true;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                char c;
                cin>>c;
                matrix[i][j] = c;
                if (c == '.') flag_com = false;
            }
        }
        bool flag_x = false;
        bool flag_o = false;
        for (int i=0; i<4; ++i) {
            if ((matrix[i][0] == 'T' || matrix[i][0] == 'X' ) &&
                (matrix[i][1] == 'T' || matrix[i][1] == 'X' ) &&
                (matrix[i][2] == 'T' || matrix[i][2] == 'X' ) &&
                (matrix[i][3] == 'T' || matrix[i][3] == 'X' ) ) {
                flag_x = true;
                break;
            }
            if ((matrix[i][0] == 'T' || matrix[i][0] == 'O' ) &&
                (matrix[i][1] == 'T' || matrix[i][1] == 'O' ) &&
                (matrix[i][2] == 'T' || matrix[i][2] == 'O' ) &&
                (matrix[i][3] == 'T' || matrix[i][3] == 'O' ) ) {
                flag_o = true;
                break;
            }
            if ((matrix[0][i] == 'T' || matrix[0][i] == 'O') &&
                (matrix[1][i] == 'T' || matrix[1][i] == 'O') &&
                (matrix[2][i] == 'T' || matrix[2][i] == 'O') &&
                (matrix[3][i] == 'T' || matrix[3][i] == 'O') ) {
                flag_o = true;
                break;
            }
            if ((matrix[0][i] == 'T' || matrix[0][i] == 'X') &&
                (matrix[1][i] == 'T' || matrix[1][i] == 'X') &&
                (matrix[2][i] == 'T' || matrix[2][i] == 'X') &&
                (matrix[3][i] == 'T' || matrix[3][i] == 'X') ) {
                flag_x = true;
                break;
            }
        }
        if ((matrix[0][0] == 'T' || matrix[0][0] == 'X' ) &&
            (matrix[1][1] == 'T' || matrix[1][1] == 'X' ) &&
            (matrix[2][2] == 'T' || matrix[2][2] == 'X' ) &&
            (matrix[3][3] == 'T' || matrix[3][3] == 'X' ) ) {
            flag_x = true;
        }
        if ((matrix[0][3] == 'T' || matrix[0][3] == 'X' ) &&
            (matrix[1][2] == 'T' || matrix[1][2] == 'X' ) &&
            (matrix[2][1] == 'T' || matrix[2][1] == 'X' ) &&
            (matrix[3][0] == 'T' || matrix[3][0] == 'X' ) ) {
            flag_x = true;
        }
        if ((matrix[0][0] == 'T' || matrix[0][0] == 'O' ) &&
            (matrix[1][1] == 'T' || matrix[1][1] == 'O' ) &&
            (matrix[2][2] == 'T' || matrix[2][2] == 'O' ) &&
            (matrix[3][3] == 'T' || matrix[3][3] == 'O' ) ) {
            flag_o = true;
        }
        if ((matrix[0][3] == 'T' || matrix[0][3] == 'O' ) &&
            (matrix[1][2] == 'T' || matrix[1][2] == 'O' ) &&
            (matrix[2][1] == 'T' || matrix[2][1] == 'O' ) &&
            (matrix[3][0] == 'T' || matrix[3][0] == 'O' ) ) {
            flag_o = true;
        }

        if (flag_x) {
            cout << "Case #" << s <<": X won"<<endl;
        }
        else if (flag_o) {
            cout << "Case #" << s <<": O won"<<endl;
        }
        else if (!flag_com) {
            cout << "Case #" << s <<": Game has not completed" << endl;
        }
        else {
            cout << "Case #" << s <<": Draw" << endl;
        }
    }
    
//fclose(stdin);
//fclose(stdout);
    return 0;
}

