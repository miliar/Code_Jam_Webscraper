#include <bits/stdc++.h>
using namespace std;
map<int, string> spelling;

void init() {
    spelling[0] = "ZERO";
    spelling[1] = "ONE";
    spelling[2] = "TWO";
    spelling[3] = "THREE";
    spelling[4] = "FOUR";
    spelling[5] = "FIVE";
    spelling[6] = "SIX";
    spelling[7] = "SEVEN";
    spelling[8] = "EIGHT";
    spelling[9] = "NINE";
}

map<char, int> freq;
char str[5000];

void decrement(int i) {
    for (int j = 0; j < spelling[i].length(); j++) {
        if (freq.count(spelling[i][j]))
            freq[spelling[i][j]]--;
    }
}

int main(void) {
    int t;
    init();
    scanf("%d", &t);
    int c = 0;
    while (t--) {
        for (char x = 'A'; x < 'Z';  x++) {
            freq[x] = 0;
        }
        scanf("%s", str);
        int l = strlen(str);
        for (int i = 0; i < l; i++) {
                freq[str[i]]++;
        }
        string ans;
        while (freq['Z'] > 0) {
            decrement(0);
            ans += '0';
        }
        while (freq['O'] - freq['W'] - freq['U'] > 0) {
            decrement(1);
            ans += '1';
        }
        while (freq['W'] > 0) {
            decrement(2);
            ans += '2';
        }
        while (freq['H'] - freq['G'] > 0) {
            decrement(3);
            ans += '3';
        }
        while (freq['U'] > 0) {
            decrement(4);
            ans += '4';
        }
        while (freq['F'] - freq['U'] > 0) {
            decrement(5);
            ans += '5';
        }
        while (freq['X'] > 0) {
            decrement(6);
            ans += '6';
        }
        while (freq['S'] - freq['X'] > 0) {
            decrement(7);
            ans += '7';
        }
        while (freq['G'] > 0) {
            decrement(8);
            ans += '8';
        }
        while (freq['I'] > 0) {
            decrement(9);
            ans += '9';
        }
        printf("Case #%d: ", ++c);
        cout << ans << endl;
    }
    return 0;
}

