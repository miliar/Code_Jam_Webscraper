#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int index = 1; index <= t; ++index) {
        string input;
        cin >> input;
        int numbers[10] = {};
        int chara[30] = {};

        for (int i = 0; i < input.length(); i++) {
            chara[input[i] - 'A']++;
        }

        // recognize zero  --z
        while (chara['Z' - 'A'] > 0 && chara['E' - 'A'] > 0
               && chara['R' - 'A'] > 0 & chara['O' - 'A'] > 0) {
            numbers[0]++;
            chara['Z' - 'A']--;
            chara['E' - 'A']--;
            chara['R' - 'A']--;
            chara['O' - 'A']--;
        }

        // recognize two  --w
        while (chara['T' - 'A'] > 0 && chara['W' - 'A'] > 0
               && chara['O' - 'A'] > 0) {
            numbers[2]++;
            chara['T' - 'A']--;
            chara['W' - 'A']--;
            chara['O' - 'A']--;
        }

        // recognize four  --u
        while (chara['F' - 'A'] > 0 && chara['O' - 'A'] > 0
               && chara['U' - 'A'] > 0 && chara['R' - 'A']) {
            numbers[4]++;
            chara['F' - 'A']--;
            chara['O' - 'A']--;
            chara['U' - 'A']--;
            chara['R' - 'A']--;
        }

        // recognize six  --x
        while (chara['S' - 'A'] > 0 && chara['I' - 'A'] > 0
               && chara['X' - 'A'] > 0) {
            numbers[6]++;
            chara['S' - 'A']--;
            chara['I' - 'A']--;
            chara['X' - 'A']--;
        }

        // After six, other s is seven
        while (chara['S' - 'A'] > 0 && chara['E' - 'A'] > 0
               && chara['V' - 'A'] > 0 && chara['E' - 'A'] > 0
                && chara['N' - 'A'] > 0) {
            numbers[7]++;
            chara['S' - 'A']--;
            chara['E' - 'A']--;
            chara['V' - 'A']--;
            chara['E' - 'A']--;
            chara['N' - 'A']--;
        }

        // After four, other f is five
        while (chara['F' - 'A'] > 0 && chara['I' - 'A'] > 0
               && chara['V' - 'A'] > 0 && chara['E' - 'A']) {
            numbers[5]++;
            chara['F' - 'A']--;
            chara['I' - 'A']--;
            chara['V' - 'A']--;
            chara['E' - 'A']--;
        }


        // After zero and four, other r is three
        while (chara['T' - 'A'] > 0 && chara['H' - 'A'] > 0
               && chara['R' - 'A'] > 0 && chara['E' - 'A'] > 0
               && chara['E' - 'A'] > 0) {
            numbers[3]++;
            chara['T' - 'A']--;
            chara['H' - 'A']--;
            chara['R' - 'A']--;
            chara['E' - 'A']--;
            chara['E' - 'A']--;
        }

        // recognize eight  --g
        while (chara['E' - 'A'] > 0 && chara['I' - 'A'] > 0
               && chara['G' - 'A'] > 0 && chara['H' - 'A'] > 0
               && chara['T' - 'A'] > 0) {
            numbers[8]++;
            chara['E' - 'A']--;
            chara['I' - 'A']--;
            chara['G' - 'A']--;
            chara['H' - 'A']--;
            chara['T' - 'A']--;
        }

        // Next o is one
        while (chara['O' - 'A'] > 0 && chara['N' - 'A'] > 0
               && chara['E' - 'A'] > 0) {
            numbers[1]++;
            chara['O' - 'A']--;
            chara['N' - 'A']--;
            chara['E' - 'A']--;
        }

        // final is nine
        while (chara['N' - 'A'] > 0 && chara['I' - 'A'] > 0
               && chara['N' - 'A'] > 0 && chara['E' - 'A']) {
            numbers[9]++;
            chara['N' - 'A']--;
            chara['I' - 'A']--;
            chara['N' - 'A']--;
            chara['E' - 'A']--;
        }
        printf("Case #%d: ", index);
        for (int i = 0; i < 10; i++) {
            while (numbers[i] > 0) {
                printf("%d", i);
                numbers[i] --;
            }
        }
        printf("\n");
    }

    return 0;
}