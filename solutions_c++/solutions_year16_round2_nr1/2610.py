#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int main() {
    string s;
    ifstream fin;
    fin.open ("C:\\Users\\dima6\\ClionProjects\\GoogleCodeJamRound1B\\inputA.txt");
    ofstream fout;
    fout.open ("C:\\Users\\dima6\\ClionProjects\\GoogleCodeJamRound1B\\outputA.txt");
    int T;
    fin >> T;
    string numbers[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    for (int i = 0; i < T; i++) {
        fin >> s;
        int letters[100] = {0};
        int *digits = new int[10];
        for (int i = 0; i < s.length(); i++) {
            letters[s[i]]++;
        }
        digits[0] = letters['Z'];
        for (int k = 0; k < digits[0]; k++) {
            for (int j = 0; j < numbers[0].length(); j++) {
                letters[numbers[0][j]]--;
            }
        }
        digits[6] = letters['X'];
        for (int k = 0; k < digits[6]; k++) {
            for (int j = 0; j < numbers[6].length(); j++) {
                letters[numbers[6][j]]--;
            }
        }
        digits[7] = letters['S'];
        for (int k = 0; k < digits[7]; k++) {
            for (int j = 0; j < numbers[7].length(); j++) {
                letters[numbers[7][j]]--;
            }
        }
        digits[8] = letters['G'];
        for (int k = 0; k < digits[8]; k++) {
            for (int j = 0; j < numbers[8].length(); j++) {
                letters[numbers[8][j]]--;
            }
        }
        digits[5] = letters['V'];
        for (int k = 0; k < digits[5]; k++) {
            for (int j = 0; j < numbers[5].length(); j++) {
                letters[numbers[5][j]]--;
            }
        }
        digits[4] = letters['F'];
        for (int k = 0; k < digits[4]; k++) {
            for (int j = 0; j < numbers[4].length(); j++) {
                letters[numbers[4][j]]--;
            }
        }
        digits[2] = letters['W'];
        for (int k = 0; k < digits[2]; k++) {
            for (int j = 0; j < numbers[2].length(); j++) {
                letters[numbers[2][j]]--;
            }
        }
        digits[1] = letters['O'];
        for (int k = 0; k < digits[1]; k++) {
            for (int j = 0; j < numbers[1].length(); j++) {
                letters[numbers[1][j]]--;
            }
        }
        digits[3] = letters['R'];
        for (int k = 0; k < digits[3]; k++) {
            for (int j = 0; j < numbers[3].length(); j++) {
                letters[numbers[3][j]]--;
            }
        }
        digits[9] = letters['I'];
        for (int k = 0; k < digits[9]; k++) {
            for (int j = 0; j < numbers[9].length(); j++) {
                letters[numbers[9][j]]--;
            }
        }
        stringstream res;
        for (int p = 0; p < 10; p++) {
            for (int k = 0; k < digits[p]; k++){
                res << p;
            }
        }
        fout << "Case #" << (i + 1) << ": "<< res.str() << endl;
    }
    fin.close();
    fout.close();

    return 0;
}