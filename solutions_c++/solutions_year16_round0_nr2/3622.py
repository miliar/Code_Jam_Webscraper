#include <iostream>
#include <string>
#include <set>

using namespace std;

void printPancakeSolution(const string &stack) {
    string normStack = stack + "+";

    int transits = 0;
    char current = normStack[0];
    for(char c : normStack) {
        if(c != current) {
            transits++;
            current = c;
        }
    }

    cout << transits;
}

int main() {
    int numCases;
    cin >> numCases;
    
    for(int caseNum = 1; caseNum <= numCases; ++caseNum) {
        cout << "Case #" << caseNum << ": ";

        string stack;
        cin >> stack;
        printPancakeSolution(stack);

        cout << endl;
    }
}
