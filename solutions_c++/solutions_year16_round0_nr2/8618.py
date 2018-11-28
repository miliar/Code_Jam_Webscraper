#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool areAllHappy(string s) {
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != '+') {
            return false;
        }
    }
    return true;
}

void flipPancakes(int lastRevIndex, string &s) {
    string s_copy = s;
    for (int i = 0; i < (lastRevIndex + 1) / 2; i++) {
        s[i] = s_copy[lastRevIndex - i];
        s[lastRevIndex - i] = s_copy[i];
    }

    for (int i = 0; i <= lastRevIndex; i++) {
        if (s[i] == '+') {
            s[i] = '-';
        }
        else if (s[i] == '-') {
            s[i] = '+';
        }
    }
}

int main() {
    int stepCount = 0;
    string str;
    int numInputs;

    cin >> numInputs;

    for (int i = 1; i <= numInputs; i++) {
        cin >> str;

        for (int j = str.length() - 1; j >= 0; j--) {
            if (areAllHappy(str)) {
                break;
            }

            if (str[j] == '+') {
                continue;
            }
            else {
                bool wasFlipped = false;
                for (int k = 0; k < j; k++) {
                    if (str[k] == '+') {
                        wasFlipped = true;
                        str[k] = '-';
                    }
                    else {
                        break;
                    }
                }

                if (wasFlipped) {
                    stepCount++;
                }

                flipPancakes(j, str);
                stepCount++;
            }
        }

        cout << "Case #" << i << ": " << stepCount << endl;
        stepCount = 0;
    }

    return 0;
}