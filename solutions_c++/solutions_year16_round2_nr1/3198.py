#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

void printDigitsSolution(const string &text) {
    map<char, int> count;

    for(char c : text) {
        count[c] += 1;
    }

    auto recognizeDigitBy = [&count](char letter, const string &written) {
        int digitCount = count[letter];

        for(char c : written) {
            count[c] -= digitCount;
        }

        return digitCount;
    };

    map<char, int> digits;
    digits['0'] = recognizeDigitBy('Z', "ZERO");
    digits['2'] = recognizeDigitBy('W', "TWO");
    digits['4'] = recognizeDigitBy('U', "FOUR");
    digits['6'] = recognizeDigitBy('X', "SIX");
    digits['8'] = recognizeDigitBy('G', "EIGHT");
    digits['3'] = recognizeDigitBy('H', "THREE");
    digits['1'] = recognizeDigitBy('O', "ONE");
    digits['5'] = recognizeDigitBy('F', "FIVE");
    digits['7'] = recognizeDigitBy('V', "SEVEN");
    digits['9'] = recognizeDigitBy('I', "NINE");

    for(auto &entry : count) {
        if(entry.second != 0) {
            cout << "[error] count " << entry.second << " for letter " << entry.first << " in " << text << endl;
        }
    }

    string result;
    for(char digit = '0'; digit <= '9'; digit++) {
        for(int i = 0; i < digits[digit]; i++) {
            result += digit;
        }
    }
    cout << result;
}

int main() {
    int numCases;
    cin >> numCases;
    
    for(int caseNum = 1; caseNum <= numCases; ++caseNum) {
        cout << "Case #" << caseNum << ": ";

        string text;
        cin >> text;
        printDigitsSolution(text);

        cout << endl;
    }
}
