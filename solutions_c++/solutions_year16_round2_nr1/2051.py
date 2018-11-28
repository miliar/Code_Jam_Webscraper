#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <bits/stl_set.h>

using namespace std;
int T, N;

int occur[26];
int res[10];

int main () {

    cin >> T;

    for (int t = 0; t < T; t++) {

        string s;
        cin >> s;

        for (int i = 0; i < 26; i++)
            occur[i] = 0;
        for (int i = 0; i < s.length(); i++)
            occur[s[i] - 'A']++;

        int z = occur[25];
        res[0] = z;
        occur[25] = 0;
        occur[4] -= z;
        occur[17] -= z;
        occur[14] -= z;

        z = occur[22];
        res[2] = z;
        occur[22] = 0;
        occur[19] -= z;
        occur[14] -= z;

        z = occur[20];
        res[4] = z;
        occur[20] = 0;
        occur[5] -= z;
        occur[14] -= z;
        occur[17] -= z;

        z = occur[23];
        res[6] = z;
        occur[23] = 0;
        occur[18] -= z;
        occur[8] -= z;

        z = occur[6];
        res[8] = z;
        occur[6] = 0;
        occur[4] -= z;
        occur[19] -= z;

        z = occur[18];
        res[7] = z;
        occur[18] = 0;
        occur[4] -= 2*z;
        occur[21] -= z;

        z = occur[21];
        res[5] = z;
        occur[4] -= z;

        z = occur[19];
        res[3] = z;
        occur[4] -= 2*z;

        z = occur[14];
        res[1] = z;
        occur[4] -= z;

        z = occur[4];
        res[9] = z;

        printf("Case #%d: ", t+1);
        for (int i = 0; i <= 9; i++) {
            for (int j = 0; j < res[i]; j++)
                cout << i;
        }

        cout << "\n";

    }
}