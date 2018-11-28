#include <iostream>
#include <string>
using namespace std;

void countLetter(string &s, int count[]) {
    for (int i = 0; i < s.length(); ++i)
        count[s[i] - 'A'] += 1;
}

void solve(int count[]) {
    int digits[10] = {0};
    // get 0's
    while (count['Z' - 'A'] > 0) {
        cerr << "z: " << count['Z' - 'A'] << endl;
        --count['Z' - 'A'];
        --count['E' - 'A'];
        --count['R' - 'A'];
        --count['O' - 'A'];
        ++digits[0];
    }
    // get 2's
    while (count['W' - 'A'] > 0) {
        --count['T' - 'A'];
        --count['W' - 'A'];
        --count['O' - 'A'];
        ++digits[2];
    }
    // get 4's
    while (count['U' - 'A'] > 0) {
        --count['F' - 'A'];
        --count['O' - 'A'];
        --count['U' - 'A'];
        --count['R' - 'A'];
        ++digits[4];
    }
    // get 5's. since FOUR has been removed, FIVE is only digit that has F
    while (count['F' - 'A'] > 0) {
        --count['F' - 'A'];
        --count['I' - 'A'];
        --count['V' - 'A'];
        --count['E' - 'A'];
        ++digits[5];
    }
    // get 6's
    while (count['X' - 'A'] > 0) {
        --count['S' - 'A'];
        --count['I' - 'A'];
        --count['X' - 'A'];
        ++digits[6];
    }
    // get 8's
    while (count['G' - 'A'] > 0) {
        --count['E' - 'A'];
        --count['I' - 'A'];
        --count['G' - 'A'];
        --count['H' - 'A'];
        --count['T' - 'A'];
        ++digits[8];
    }
    // get 1's
    while (count['O' - 'A'] > 0) {
        --count['O' - 'A'];
        --count['N' - 'A'];
        --count['E' - 'A'];
        ++digits[1];
    }
    // get 3's
    while (count['T' - 'A'] > 0) {
        --count['T' - 'A'];
        --count['H' - 'A'];
        --count['R' - 'A'];
        --count['E' - 'A'];
        --count['E' - 'A'];
        ++digits[3];
    }
    // get 7's
    while (count['V' - 'A'] > 0) {
        --count['S' - 'A'];
        --count['E' - 'A'];
        --count['V' - 'A'];
        --count['E' - 'A'];
        --count['N' - 'A'];
        ++digits[7];
    }
    // get 9's
    digits[9] += count['I' - 'A'];
    cerr << "digits: ";
    for (int i = 0; i < 10; ++i)
        cerr << digits[i];
    cerr << endl;
    for (int i = 0; i < 10; ++i) {
        while (digits[i] > 0) {
            cout << i;
            --digits[i];
        }
    }
}

int main() {
    int t;
    int count[26];
    string s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> s;
        cout << "Case #" << i << ": ";
        for (int j = 0; j < 26; ++j) count[j] = 0;
        countLetter(s, count);
        cerr << "count: ";
        for (int j = 0; j < 26; ++j)
            cerr << count[j] << " ";
        cerr << endl;
        solve(count);
        cout << endl;
    }
    return 0;
}
