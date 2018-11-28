/*
* @Author: Yinlong Su
* @Date:   2016-04-30 11:53:00
* @Last Modified by:   Yinlong Su
* @Last Modified time: 2016-04-30 12:28:33
*/

#include <iostream>

using namespace std;

int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
    FILE *fout = freopen("A-large.out", "w", stdout);

    int c[26];
    int p[10];
    char line[3000];

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        for (int j = 0;  j < 3000; j++)
            line[j] = 0;
        for (int j = 0; j < 26; j++)
            c[j] = 0;
        for (int j = 0; j < 10; j++)
            p[j] = 0;
        cin >> line;

        for (int j = 0; j < 3000; j++)
            if (line[j] >= 'A' && line[j] <= 'Z') {
                c[line[j]-'A'] ++;
            }

        p[0] = c['Z' - 'A'];
        c['Z' - 'A'] -= p[0];
        c['E' - 'A'] -= p[0];
        c['R' - 'A'] -= p[0];
        c['O' - 'A'] -= p[0];

        p[2] = c['W' - 'A'];
        c['T' - 'A'] -= p[2];
        c['W' - 'A'] -= p[2];
        c['O' - 'A'] -= p[2];

        p[6] = c['X' - 'A'];
        c['S' - 'A'] -= p[6];
        c['I' - 'A'] -= p[6];
        c['X' - 'A'] -= p[6];

        p[8] = c['G' - 'A'];
        c['E' - 'A'] -= p[8];
        c['I' - 'A'] -= p[8];
        c['G' - 'A'] -= p[8];
        c['H' - 'A'] -= p[8];
        c['T' - 'A'] -= p[8];

        p[7] = c['S' - 'A'];
        c['S' - 'A'] -= p[7];
        c['E' - 'A'] -= p[7] * 2;
        c['V' - 'A'] -= p[7];
        c['N' - 'A'] -= p[7];

        p[9] = c['S' - 'A'];
        c['S' - 'A'] -= p[9];
        c['E' - 'A'] -= p[9] * 2;
        c['V' - 'A'] -= p[9];
        c['N' - 'A'] -= p[9];

        p[3] = c['T' - 'A'];
        c['T' - 'A'] -= p[3];
        c['H' - 'A'] -= p[3];
        c['R' - 'A'] -= p[3];
        c['E' - 'A'] -= p[3] * 2;

        p[4] = c['R' - 'A'];
        c['F' - 'A'] -= p[4];
        c['O' - 'A'] -= p[4];
        c['U' - 'A'] -= p[4];
        c['R' - 'A'] -= p[4];

        p[5] = c['F' - 'A'];
        c['F' - 'A'] -= p[5];
        c['I' - 'A'] -= p[5];
        c['V' - 'A'] -= p[5];
        c['E' - 'A'] -= p[5];

        p[1] = c['O' - 'A'];
        c['O' - 'A'] -= p[1];
        c['N' - 'A'] -= p[1];
        c['E' - 'A'] -= p[1];

        p[9] = c['I' - 'A'];

        cout << "Case #" << (i + 1) << ": ";
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < p[j]; k++)
                cout << j;
        }
        cout << endl;

    }

    return 0;
}