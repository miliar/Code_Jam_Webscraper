#include <iostream>

using namespace std;

int T;

int caseNum = 0;
bool possibleNums[17];

void initNums() {
    for (int i = 1; i <= 16; i++) {
        possibleNums[i] = true;
    }
}

void elimNums() {
    int answer;
    cin >> answer;
    for (int r = 1; r <= 4; r++) {
        for (int c = 1; c <= 4; c++) {
            int num;
            cin >> num;
            if (answer != r) {
                possibleNums[num] = false;
            }
        }
    }
}

void output() {
    cout << "Case #" << ++caseNum << ": ";
    int nSolutions = 0;
    int solution = 0;
    for (int i = 1; i<= 16; i++) {
        if (possibleNums[i]) {
            nSolutions++;
            solution = i;
        }
    }
    if (nSolutions == 0) {
        cout << "Volunteer cheated!";
    } else if (nSolutions > 1) {
        cout << "Bad magician!";
    } else {
        cout << solution;
    }
    cout << endl;
}

int main() {
    cin >> T;
    for (int i = 0; i < T; i++) {
        initNums();
        elimNums();
        elimNums();
        output();
    }
}
