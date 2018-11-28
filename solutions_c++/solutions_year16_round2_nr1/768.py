#include <bits\stdc++.h>
using namespace std;

string s;

int freq[26];
string ans;
string DIGITS[] = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
int DIGITS_FREQ[10][26] = { 0 };
int digits[10];

void remove(int target, int count) {
    for (int i = 0; i < 26; i++)
        freq[i] -= count * DIGITS_FREQ[target][i];
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    memset(DIGITS_FREQ, 0, sizeof(DIGITS_FREQ));
    for (int i = 0; i <= 9; i++) 
        for (int j = 0; j < DIGITS[i].length(); j++) 
            DIGITS_FREQ[i][DIGITS[i][j] - 'A']++;

    int t, c = 1;
    scanf("%d", &t);
    while (t--) {
        cin >> s;
        memset(freq, 0, sizeof(freq));
        memset(digits, 0, sizeof(digits));
        for (int i = 0; i < s.length(); i++)
            freq[s[i] - 'A']++;

        digits[0] = freq['Z' - 'A']; // ZERO
        remove(0, digits[0]);
        digits[2] = freq['W' - 'A']; // TWO
        remove(2, digits[2]);
        digits[4] = freq['U' - 'A']; // FOUR
        remove(4, digits[4]);
        digits[6] = freq['X' - 'A']; // SIX
        remove(6, digits[6]);
        digits[8] = freq['G' - 'A']; // EIGHT
        remove(8, digits[8]);
        digits[1] = freq['O' - 'A']; // ONE
        remove(1, digits[1]);
        digits[5] = freq['F' - 'A']; // FIVE
        remove(5, digits[5]);
        digits[7] = freq['S' - 'A']; // SEVEN
        remove(7, digits[7]);
        digits[3] = freq['H' - 'A']; // THREE
        remove(3, digits[3]);
        digits[9] = freq['N' - 'A'] / 2; // NINE
        remove(9, digits[9]);

        ans.clear();
        for (int i = 0; i < 10; i++)
            for (int j = 0; j < digits[i]; j++)
                ans.push_back('0' + i);

        cout << "Case #" << c++ << ": " << ans << endl;
    }
    return 0;
}