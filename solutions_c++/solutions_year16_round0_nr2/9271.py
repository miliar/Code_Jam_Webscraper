#include <iostream>
#include <string>

using std::endl;
using std::cin;
using std::cout;
using std::string;

void doCase(int caseNum) {
    string line;
    cin >> line;

    int answer = 0;

    char last = ' ';
    for (int i = 0; i < line.length(); i++) {
        char c = line[i];
        if (c != last) {
            last = c;
            answer++;
        }
    }
    if (last == '+') {
        answer--;
    }

    cout << "Case #" << caseNum << ": " << answer << endl;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int i = 0; i < numCases; i++) {
        doCase(i+1);
    }
}
