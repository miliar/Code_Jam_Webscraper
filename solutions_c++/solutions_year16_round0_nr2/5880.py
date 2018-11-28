#include <iostream>
#include <string>

using namespace std;

int resolveForPositive(string stack);
int resolveForNegative(string stack);

int resolveForNegative(string stack) {
    char last = stack.back();

    if(stack.length() == 1) {
        if(last == '-')
            return 0;
        else
            return 1;
    } else {
        if(last == '-') {
            return resolveForNegative(stack.substr(0, stack.length() - 1));
        } else {
            return 1 + resolveForPositive(stack.substr(0, stack.length() - 1));
        }
    }
}

int resolveForPositive(string stack) {
    char last = stack.back();

    if(stack.length() == 1) {
        if(last == '+')
            return 0;
        else
            return 1;
    } else {
        if(last == '+') {
            return resolveForPositive(stack.substr(0, stack.length() - 1));
        } else {
            return 1 + resolveForNegative(stack.substr(0, stack.length() - 1));
        }
    }
}

int main() {
    int t;
    cin >> t;
    string stack;
    getline(cin, stack);
    for(int i = 1; i <= t; ++i) {
        getline(cin, stack);

        int flips = resolveForPositive(stack);
        cout << "Case #" << i << ": " << flips << endl;
    }
    return 0;
}
