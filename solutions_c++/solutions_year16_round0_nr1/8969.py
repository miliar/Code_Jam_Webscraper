#include <iostream>
#include <cstring>
using namespace std;
void solveAndPrint(string &digits, int caseNum);
int main(int argc, char *argv[]) {
    int numOfCase;
    cin >> numOfCase;
    string digits;
    for (int i = 0; i < numOfCase; i++) {
        cin >> digits;
        solveAndPrint(digits, i + 1);
    }
}

void solveAndPrint(string &digits, int caseNum) {
    int hits[10] = {0};
    for (auto iter = digits.begin(); iter < digits.end(); iter++) {
        hits[(*iter - '0')] = 1;
    }
    if (hits[1] == 0 && hits[2] == 0 && hits[3] == 0 && hits[4] == 0&&hits[5]==0 && hits[6] == 0 && hits[7] == 0 && hits[8] == 0 && hits[9] == 0) {
        cout << "Case #" << caseNum << ": "
             << "INSOMNIA" << endl;
        return;
    }
    //have solution
    long number = atol(digits.c_str());
    long sofar = 0;
    while (true) {
        sofar += number;
        long tmp = sofar;
        while (sofar != 0) {
            hits[sofar%10] = 1;
            if (hits[0] == 1 && hits[1] == 1 && hits[2] == 1 && hits[3] == 1 && hits[4] == 1 && hits[5] == 1 && hits[6] == 1 && hits[7] == 1 && hits[8] == 1 && hits[9] == 1) {
                cout << "Case #" << caseNum << ": " << tmp << endl;
                return;
            } else {
                sofar /= 10;
                continue;
            }
        }
        sofar=tmp;
    }
}
