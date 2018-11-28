/*
Will Long
Google Code Jam 2016
Round 1B - Problem 1

April 30, 2016
*/

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <deque>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char *argv[]) {
    string fname = argv[1];
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout);

    int char_freqs[26];
    for (int i = 0; i < 26; i++) {
        char_freqs[i] = 0;
    }
    int digit_counts[10];
    for (int i = 0; i < 10; i++) {
        digit_counts[i] = 0;
    }

    int cases;
    cin >> cases;
    
    for (int tc = 1; tc <= cases; tc++) {
        string message;
        cin >> message;

        for (int i = 0; i < message.size(); i++) {
            char ch = message.at(i);
            char_freqs[ch - 'A']++;
        }

        // ZERO
        while (char_freqs['Z'-'A']) {
            //cout << 0;
            char_freqs['Z'-'A']--;
            char_freqs['E'-'A']--;
            char_freqs['R'-'A']--;
            char_freqs['O'-'A']--;
            digit_counts[0]++;
        }
        // TWO
        while (char_freqs['W'-'A']) {
            //cout << 2;
            char_freqs['T'-'A']--;
            char_freqs['W'-'A']--;
            char_freqs['O'-'A']--;
            digit_counts[2]++;
        }
        // SIX
        while (char_freqs['X'-'A']) {
            //cout << 6;
            char_freqs['I'-'A']--;
            char_freqs['X'-'A']--;
            char_freqs['S'-'A']--;
            digit_counts[6]++;
        }
        // EIGHT
        while (char_freqs['G'-'A']) {
            //cout << 8;
            char_freqs['I'-'A']--;
            char_freqs['G'-'A']--;
            char_freqs['H'-'A']--;
            char_freqs['E'-'A']--;
            char_freqs['T'-'A']--;
            digit_counts[8]++;
        }
        // SEVEN
        while (char_freqs['V'-'A'] && char_freqs['S'-'A']) {
            //cout << 7;
            char_freqs['S'-'A']--;
            char_freqs['N'-'A']--;
            char_freqs['V'-'A']--;
            char_freqs['E'-'A']-=2;
            digit_counts[7]++;
        }
        // FIVE
        while (char_freqs['V'-'A']) {
            //cout << 5;
            char_freqs['F'-'A']--;
            char_freqs['I'-'A']--;
            char_freqs['V'-'A']--;
            char_freqs['E'-'A']--;
            digit_counts[5]++;
        }
        // FOUR
        while (char_freqs['F'-'A']) {
            //cout << 4;
            char_freqs['F'-'A']--;
            char_freqs['U'-'A']--;
            char_freqs['R'-'A']--;
            char_freqs['O'-'A']--;
            digit_counts[4]++;
        }
        // ONE
        while (char_freqs['O'-'A']) {
            //cout << 1;
            char_freqs['O'-'A']--;
            char_freqs['N'-'A']--;
            char_freqs['E'-'A']--;
            digit_counts[1]++;
        }
        // NINE
        while (char_freqs['N'-'A']) {
            //cout << 9;
            char_freqs['I'-'A']--;
            char_freqs['N'-'A']-=2;
            char_freqs['E'-'A']--;
            digit_counts[9]++;
        }
        // THREE        
        while (char_freqs['R'-'A']) {
            //cout << 3;
            char_freqs['T'-'A']--;
            char_freqs['E'-'A']-=2;
            char_freqs['R'-'A']--;
            char_freqs['H'-'A']--;
            digit_counts[3]++;
        }

        cout << "Case #" << tc << ": ";
        for (int i = 0; i < 10; i++) {
            while (digit_counts[i]) {
                cout << i;
                digit_counts[i]--;
            }
        }
        cout << endl;
    }

    return 0;
}