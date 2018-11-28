#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <sstream>

using namespace std;

const int TOTAL_DIGITS = 10;
bool digits[TOTAL_DIGITS];


bool hasAllDigits() {
    bool ans = true;

    for (int i = 0; i < TOTAL_DIGITS ; i++) {
        if (!digits[i])
            return false;
    }

    return ans;
}

string to_string(int number) {
    string ans;

    stringstream convert;

    convert << number;

    ans = convert.str();

    return ans;
}

void updateDigits(string number){

    for (int i =0; i<number.length(); i++){
        char c = number.at(i);
        int value = atoi(&c);
        digits[value] = true;
    }
}

long long solve(string sValue){

    long long value = atoll(sValue.c_str());

    if (value == 0)
        return value;

    for (int i = 0; i < TOTAL_DIGITS ; i++) {
        digits[i] = false;
    }

    int iterator = 1;
    long long ans = value;

    while (true) {
        updateDigits(to_string(ans));

        if (hasAllDigits()){
            break;
        }

        ans = iterator*value;
        iterator++;
    }

    return ans;
}

int main() {
    freopen ("C:\\Users\\ygonzalez\\ClionProjects\\CountingSheep\\CountingSheep.in","r",stdin);
    freopen ("C:\\Users\\ygonzalez\\ClionProjects\\CountingSheep\\CountingSheep.out","w",stdout);
    int n;
    cin >> n;
    string values[n];

    for(int i = 0; i < n ; i++) {
        cin >> values[i];
        long long ans = solve(values[i]);
        if (ans == 0)
            cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
        else
            cout << "Case #" << (i+1) << ": " << ans << endl;
    }

    return 0;
}