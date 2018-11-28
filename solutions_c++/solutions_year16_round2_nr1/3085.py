#include <iostream>
#include <string>

using namespace std;

void puzzle(string s) {
    int huruf[26];
    for (int i=0; i<26; i++)
        huruf[i] = 0;
    for (int i=0; i<s.length(); i++)
        huruf[((int) s.at(i)) - 65]++;

    int angka[10];
    for (int i=0; i<10; i++)
        angka[i] = 0;

    while (huruf[25] > 0) {
        angka[0]++; huruf[25]--; huruf[4]--; huruf[17]--; huruf[14]--;
    }
    while (huruf[22] > 0) {
        angka[2]++; huruf[19]--; huruf[22]--; huruf[14]--;
    }
    while (huruf[20] > 0) {
        angka[4]++; huruf[5]--; huruf[14]--; huruf[20]--; huruf[17]--;
    }
    while (huruf[23] > 0) {
        angka[6]++; huruf[18]--; huruf[8]--; huruf[23]--;
    }
    while (huruf[6] > 0) {
        angka[8]++; huruf[4]--; huruf[8]--; huruf[6]--; huruf[7]--; huruf[19]--;
    }

    while (huruf[14] > 0) {
        angka[1]++; huruf[14]--; huruf[13]--; huruf[4]--;
    }
    while (huruf[7] > 0) {
        angka[3]++; huruf[19]--; huruf[7]--; huruf[17]--; huruf[4]--; huruf[4]--;
    }
    while (huruf[5] > 0) {
        angka[5]++; huruf[5]--; huruf[8]--; huruf[21]--; huruf[4]--;
    }
    while (huruf[18] > 0) {
        angka[7]++; huruf[18]--; huruf[4]--; huruf[21]--; huruf[4]--; huruf[14]--;
    }
    while (huruf[13] > 1 && huruf[8] > 0 && huruf[4] > 0) {
        angka[9]++; huruf[13]--; huruf[8]--; huruf[13]--; huruf[4]--;
    }

    for (int i=0; i<10; i++) {
        while (angka[i] > 0) {
            cout << i;
            angka[i]--;
        }
    }
    cout << endl;
}

int main() {
    int t; string s;
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> s;
        cout << "Case #" << i+1 << ": "; puzzle(s);
    }
    return 0;
}
