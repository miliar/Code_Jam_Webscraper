#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int res = 0;
        string s;
        cin >> s;
        int a[30];
        int b[10];
        memset (a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        for (int i=0; i<s.length(); i++) {
            a[s[i]-'A']++;
        }
        while (a['Z'-'A'] > 0) {
            a['Z'-'A']--;
            a['E'-'A']--;
            a['R'-'A']--;
            a['O'-'A']--;
            b[0]++;
        }
        while (a['W'-'A'] > 0) {
            a['T'-'A']--;
            a['W'-'A']--;
            a['O'-'A']--;
            b[2]++;
        }
        while (a['U'-'A'] > 0) {
            a['F'-'A']--;
            a['O'-'A']--;
            a['U'-'A']--;
            a['R'-'A']--;
            b[4]++;
        }
        while (a['X'-'A'] > 0) {
            a['S'-'A']--;
            a['I'-'A']--;
            a['X'-'A']--;
            b[6]++;
        }
        while (a['G'-'A'] > 0) {
            a['E'-'A']--;
            a['I'-'A']--;
            a['G'-'A']--;
            a['H'-'A']--;
            a['T'-'A']--;
            b[8]++;
        }
        while (a['H'-'A'] > 0) {
            a['T'-'A']--;
            a['H'-'A']--;
            a['R'-'A']--;
            a['E'-'A']--;
            a['E'-'A']--;
            b[3]++;
        }
        while (a['F'-'A'] > 0) {
            a['F'-'A']--;
            a['I'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
            b[5]++;
        }
        while (a['S'-'A'] > 0) {
            a['S'-'A']--;
            a['E'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
            a['N'-'A']--;
            b[7]++;
        }

        while (a['O'-'A'] > 0) {
            b[1]++;
            a['O'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
        }
        while (a['N'-'A'] > 0) {
            b[9]++;
            a['N'-'A']--;
            a['I'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
        }
        cout << "Case #" << i+1 << ": ";
        for (int i=0; i<10; i++) {
            while(b[i]!=0) {
                cout << i;
                b[i]--;
            }
        }
        cout << endl;
    }
    return 0;
}
