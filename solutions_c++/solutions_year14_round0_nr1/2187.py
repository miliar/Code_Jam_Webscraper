#include<iostream>
#include<fstream>
using namespace std;
int t, i, j, k, first_answer, second_answer, right_number, count;
int f[5][5];
int s[5][5];
int main() {
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt0.in");
    fout.open("A-small-practice.out");
    fin >> t;
    for (k = 0; k < t; ++k) {
        fin >> first_answer;
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                fin >> f[i][j];
            }
        }
        fin >> second_answer;
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                fin >> s[i][j];
            }
        }
        count = 0;
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                if (f[first_answer-1][i] == s[second_answer-1][j]) {
                    count++;
                    right_number = f[first_answer-1][i];
                }
            }
        }
        fout << "Case #" << k + 1 << ": ";
        if (count == 0) fout << "Volunteer cheated!";
        else if (count == 1) fout << right_number;
        else fout << "Bad magician!";
        fout << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
