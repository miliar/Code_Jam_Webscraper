/* 
 * File:   main.cpp
 * Author: Vekkiokonio
 *
 * Created on 13 aprile 2013, 3.44
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char check_line(char, char, char, char);

int main(int argc, char** argv) {
    int n = 0;
    char num[4] = {'x', 'x', 'x', 'x'};
    int test = 1;
    char m[4][4];
    ifstream myfile;
    ofstream output("ex1_large.txt");
    myfile.open("A-large.in");
    myfile.getline(num, 5);
    int index = 0;
    while (int(num[index]) > 47 && int(num[index]) < 58){
        n = n*10 + int(num[index] - 48);
        index++;
    }
    n++;
    while (test < n){
        bool not_end = false;
        int i = 0;
        char win = '0';
        for (int j = 0; j < 4; j++){
            for (int k = 0; k < 4; k++)
                m[j][k] = myfile.get();
            myfile.get();
        }
        myfile.get();
        while (i < 4 && (win != 'X' && win != 'O')){
                win = check_line(m[i][0], m[i][1], m[i][2], m[i][3]);
                if (win == '.')
                    not_end = true;
                i++;
        }
        if (win == 'X' || win == 'O')
            output << "Case #" << test << ": " << win << " won" << endl;
        else {
            i = 0;
            while (i < 4 && (win != 'X' && win != 'O')){
                win = check_line(m[0][i], m[1][i], m[2][i], m[3][i]);
                if (win == '.')
                    not_end = true;
                i++;
            }
            if (win == 'X' || win == 'O')
                output << "Case #" << test << ": " << win << " won" << endl;
            else {
                win = check_line(m[0][0], m[1][1], m[2][2], m[3][3]);
                if (win == '.')
                    not_end = true;
                if (win == 'X' || win == 'O')
                    output << "Case #" << test << ": " << win << " won" << endl;
                else{
                    win = check_line(m[0][3], m[1][2], m[2][1], m[3][0]);
                    if (win == '.')
                        not_end = true;
                    if (win == 'X' || win == 'O')
                        output << "Case #" << test << ": " << win << " won" << endl;
                    else if (not_end)
                        output << "Case #" << test << ": Game has not completed" << endl;
                    else
                        output << "Case #" << test << ": Draw" << endl;
                }
            }
        }
        test++;
    }
    myfile.close();
    output.close();
    return 0;   
}

char check_line(char a, char b, char c, char d){
    if (a == 'T' && b == c && c == d || b == 'T' && a == c && c == d || c == 'T' && a == b && b == d || d == 'T' && a == b && b == c || a == b && b == c && c == d)
        if (a != 'T')
            return a;
        else
            return b;
    else if (a == '.' || b == '.' || c == '.' || d == '.')
        return '.';
    return '-';
}