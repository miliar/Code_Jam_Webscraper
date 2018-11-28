#include <iostream>
#include <string>
using namespace std;

string flip (string pancake) {
    string res;
    for (int i = pancake.length() - 1; i >= 0; i--) {
        if (pancake[i] == '-') {
            res += '+';
        } else {
            res += '-';
        }
    }

    return res;
}

int flipCalc (string pancake){
    if (pancake.length() == 0) {
        return 0;
    }
    if (pancake[pancake.length() - 1] == '+') {
        return flipCalc(pancake.erase(pancake.length() - 1));
    }

    int leadingPlus = 0;
    int flipCount = 0;
    while (pancake[leadingPlus] == '+') {
        flipCount = 1;
        pancake[leadingPlus] = '-';
        leadingPlus++;
    }

    return flipCalc(flip(pancake)) + 1 + flipCount;
}


int main () {
    int T;
    string dummy;
    cin >> T;
    getline(cin, dummy);
    for (int t = 1; t <= T; t++) {
        string pancake;
        getline(cin, pancake);
        cout << "Case #" << t << ": " << flipCalc(pancake) << endl;
    }
    return 0;
}
