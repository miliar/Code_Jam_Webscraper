#include <iostream>
#include <fstream>
using namespace std;
void solveAndPrint(string &pattern, int caseNum);
int main(int argc, char *argv[]) {
    int numOfCase;
    cin >> numOfCase;
    string pattern;
    for (int i = 0; i < numOfCase; i++) {
        cin >> pattern;
        solveAndPrint(pattern, i + 1);
    }
}

void solveAndPrint(string &pattern, int caseNum) {
    auto beginIter = pattern.begin();
    auto endIter = pattern.end();
    bool beginAndEndSame;
    int numberOfChar = 0;
    int result = 0;
    if (*beginIter == '-') {
        if (*beginIter != *(endIter - 1))
            beginAndEndSame = false;
        else
            beginAndEndSame = true;
        for (auto i = beginIter + 1; i < endIter; i++) {
            if (*i == '+') {
                i = i + 1;
                numberOfChar++;
                while (i < endIter && *i == '+')
                    i++;
            }
        }
        result = 2 * numberOfChar + 1;
        if (!beginAndEndSame)
            result -= 2;
        cout << "Case #" << caseNum << ": " << result << endl;
    } else {
        for (auto i = beginIter + 1; i < endIter; i++) {
            if (*i == '-') {
                i++;
                numberOfChar++;
                while (i < endIter && *i == '-')
                    i++;
            }
        }
        result = 2 * numberOfChar;
        cout << "Case #" << caseNum << ": " << result << endl;
    }
}
