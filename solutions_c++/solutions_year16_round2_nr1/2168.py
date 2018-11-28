#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        unordered_map<char, int> charcount;
        vector<int> numcount(10, 0);
        for (int j = 0; j < s.size(); j++) {
            if (charcount.find(s[j]) == charcount.end()) {
                charcount[s[j]] = 1;
            }
            else charcount[s[j]] += 1;
        }
        numcount[0] = charcount['Z'];
        charcount['Z'] -= numcount[0];
        charcount['E'] -= numcount[0];
        charcount['R'] -= numcount[0];
        charcount['O'] -= numcount[0];
        numcount[2] = charcount['W'];
        charcount['T'] -= numcount[2];
        charcount['W'] -= numcount[2];
        charcount['O'] -= numcount[2];
        numcount[4] = charcount['U'];
        charcount['F'] -= numcount[4];
        charcount['O'] -= numcount[4];
        charcount['U'] -= numcount[4];
        charcount['R'] -= numcount[4];
        numcount[6] = charcount['X'];
        charcount['S'] -= numcount[6];
        charcount['I'] -= numcount[6];
        charcount['X'] -= numcount[6];
        numcount[8] = charcount['G'];
        charcount['E'] -= numcount[8];
        charcount['I'] -= numcount[8];
        charcount['G'] -= numcount[8];
        charcount['H'] -= numcount[8];
        charcount['T'] -= numcount[8];
        numcount[1] = charcount['O'];
        charcount['O'] -= numcount[1];
        charcount['N'] -= numcount[1];
        charcount['E'] -= numcount[1];
        numcount[3] = charcount['T'];
        charcount['T'] -= numcount[3];
        charcount['H'] -= numcount[3];
        charcount['R'] -= numcount[3];
        charcount['E'] -= 2 * numcount[3];
        numcount[5] = charcount['F'];
        charcount['I'] -= numcount[5];
        numcount[7] = charcount['S'];
        numcount[9] = charcount['I'];
        cout << "Case #" << i+1 << ": ";
        for (int j = 0; j < 10; j++) {
            for (int l = 0; l < numcount[j]; l++) {
                cout << j;
            }
        }
        cout << endl;
    }
    return 0;
}
