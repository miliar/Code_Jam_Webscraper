/*
 g++ --std=c++11 -Wl,--stack=0x1000000 C.cc
*/

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>
#include <gmpxx.h>

using namespace std;

int T, N;

int main()
{
    ios::sync_with_stdio(false);
    cout.precision(8);

    cin >> T;
    for (int t = 1; t <= T; t++) {
        string S;
        cin >> S;

        char c = S[0];
        int cnt = 0;

        for (int i = 1; i < S.length(); i++) {
            if (S[i] == c) continue;
            cnt++;
            c = S[i];
        }
        if (c == '-') cnt++;

        cout << "Case #" << t << ": " << cnt << endl;
    }
}
