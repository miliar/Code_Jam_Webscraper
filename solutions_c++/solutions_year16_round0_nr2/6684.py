#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>

using namespace std;

int T;
string S, SS;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> S;


        int ans = 0;
        while (S.size()) {
            while (S.size() > 0 && S.back() == '+') {
                S.pop_back();
            }

            if (!S.size()) {
                break;
            }

            for (int i = 0; i < S.size(); ++i) {
                S[i] = (S[i] == '+' ? S[i] = '-' : S[i] = '+');
            }
            ++ans;
        }


        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}