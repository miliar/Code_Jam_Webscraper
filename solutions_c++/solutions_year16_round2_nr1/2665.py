#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UI;
int main(int argc, char **argv)
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    ULL T;
    cin >> T;
    for (ULL t = 1; t <= T; ++t) {
        string S;
        cin >> S;
        // sort (S.begin(), S.end());
        ULL c0 = 0, c1 = 0, c2 = 0, c3 = 0, c4 = 0, c5 = 0, c6 = 0, c7 = 0, c8 = 0, c9 = 0;
        vector<UI> a(26, 0);
        for (ULL i = 0; i < S.size(); ++i) {
            ++a[S[i] - 'A'];
        }
        {
            if (a[6] > 0) { // g => 8
                for (UI j = 0; j < a[6]; ++j) {
                    ++c8;
                    --a[4]; --a[8]; --a[7]; --a[19];
                }
                a[6] = 0;
            }
            if (a[23] > 0) { // X => 6
                for (UI j = 0; j < a[23]; ++j) {
                    ++c6;
                    --a[18]; --a[8];
                }
                a[23] = 0;
            }
            if (a[25] > 0) { // Z => 0
                for (UI j = 0; j < a[25]; ++j) {
                    ++c0;
                    --a[4]; --a[17], --a[14];
                }
                a[25] = 0;
            }
            if (a[22] > 0) { // W => 2
                for (UI j = 0; j < a[22]; ++j) {
                    ++c2;
                    --a[19]; --a[14];
                }
                a[22] = 0;
            }
            if (a[20] > 0) { // U => 4
                for (UI j = 0; j < a[20]; ++j) {
                    ++c4;
                    --a[5]; --a[14], --a[17];
                }
                a[20] = 0;
            }
            if (a[14] > 0) { // O => 1
                for (UI j = 0; j < a[14]; ++j) {
                    ++c1;
                    --a[13]; --a[4];
                }
                a[14] = 0;
            }
            if (a[17] > 0) { // R => 3
                for (UI j = 0; j < a[17]; ++j) {
                    ++c3;
                    --a[19]; --a[7], --a[4]; --a[4];
                }
                a[17] = 0;
            }
            if (a[18] > 0) { // S => 7
                for (UI j = 0; j < a[18]; ++j) {
                    ++c7;
                    --a[4]; --a[4], --a[21]; --a[13];
                }
                a[18] = 0;
            }
            if (a[21] > 0) { // V => 5
                for (UI j = 0; j < a[21]; ++j) {
                     ++c5;
                     --a[5]; --a[8], --a[4];
                }
                a[21] = 0;
            }
            if (a[8] > 0) { // I => 9
                for (UI j = 0; j < a[8]; ++j) {
                    ++c9;
                    --a[13]; --a[13], --a[4];
                }
                a[8] = 0;
            }
        }
        string ans;
        for (UI i = 0; i < c0; ++i)
            ans += "0";
        for (UI i = 0; i < c1; ++i)
            ans += "1";
        for (UI i = 0; i < c2; ++i)
            ans += "2";
        for (UI i = 0; i < c3; ++i)
            ans += "3";
        for (UI i = 0; i < c4; ++i)
            ans += "4";
        for (UI i = 0; i < c5; ++i)
            ans += "5";
        for (UI i = 0; i < c6; ++i)
            ans += "6";
        for (UI i = 0; i < c7; ++i)
            ans += "7";
        for (UI i = 0; i < c8; ++i)
            ans += "8";
        for (UI i = 0; i < c9; ++i)
            ans += "9";
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
