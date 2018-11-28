#include<iostream>
#include<string>
#include<fstream>

using namespace std;

// 4*4 square board, with single T in one of the 16 squares
// players: X, O; X starting
// row, column or a diagonal containing 4


ofstream outfile;
string Status_case[4] = {"X won", "O won", "Draw", "Game has not completed"};
int char_num(char c) {
    if (c == 'X')
        return 0;
    else if (c == 'O')
        return 1;
    else if (c == 'T')
        return 2;
    else if (c == '.')
        return 3;
}

void print_status(int casenum, int status) {
    outfile << "Case #" << casenum << ": " << Status_case[status] << endl;
}

bool count_result(int caseNum, int *countx) {
    if (countx[0] == 4 || (countx[0] + countx[2]) == 4){
        // X won
        print_status(caseNum, 0);
        return true;
    } else if (countx[1] == 4 || (countx[1] + countx[2]) == 4){
        // O won
        print_status(caseNum, 1);
        return true;
    } else {
        return false;
    }
}

int main()
{
    ifstream infile;
    outfile.open("out.txt", ofstream::out);
    infile.open("A-large.in", ifstream::in);

    int case_num;
    string space;
    infile >> case_num;

    char square[4][4];
    for(int i = 1; i <=case_num; i++) {
        bool print_flag = false;
        int count_all[4] = {0};

        for (int j = 0; j < 4; j++) {
            infile >> square[j];
        }

        // check rows
        for (int j = 0; j < 4; j++) {
            int countx[4] = {0};
            for (int k = 0; k < 4; k++) {
                countx[char_num(square[j][k])]++;
                count_all[char_num(square[j][k])]++;
            }
            print_flag = count_result(i, countx);
            if (print_flag) break;
        }

        if (print_flag) continue;

        // check columns
        for (int j = 0; j < 4; j++) {
            int countx[4] = {0};
            for (int k = 0; k < 4; k++) {
                countx[char_num(square[k][j])]++;
            }
            print_flag = count_result(i, countx);
            if (print_flag) break;
        }

        if (print_flag) continue;

        // check diagonal
        for (int x = 0; x < 2; x++) {
            int countx[4] = {0};
            if (x == 0) {
                for (int j = 0; j < 4; j++) {
                    countx[char_num(square[j][j])]++;
                }
                print_flag = count_result(i, countx);
            } else {
                for (int j = 0; j < 4; j++) {
                    countx[char_num(square[3-j][j])]++;
                }
                print_flag = count_result(i, countx);
            }
            if (print_flag) break;
        }

        if (print_flag) continue;
        else if(print_flag == false) {
            if (count_all[3] == 0) {
                print_status(i, 2);
            } else {
                print_status(i, 3);
            }

        }




        getline(infile, space);
    }

    return 0;
}


