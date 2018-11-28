#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

const long long MOD = 1000000007;
int R, C;
long long ans;

/*
A
2

B
221
221

C
222112
112222

D
2212
1212
1222
*/

void solve() {
    for (int a = 0; a <= (R+2) / 3; a++) {
        for (int b = 0; b <= (R+2) / 4; b++) {
            if (C % 3 != 0 && b > 0) {
                break;
            }
            for (int c = 0; c <= (R+2) / 4; c++) {
                if (C % 6 != 0 && c > 0) {
                    break;
                }
                for (int d = 0; d <= (R+2) / 5; d++) {
                    if (C % 4 != 0 && d > 0) {
                        break;
                    }
                    int rows = a*3 + b*4 + c*4 + d*5;
                    if (rows != R && rows != R - 2 && rows != R + 2) {
                        continue;
                    }
                    int extra = (R + 2 - rows) / 2;

                    long long perm = 1;
                    for (int i = 1; i <= b; i++) {
                        perm *= i+a;
                        perm /= i;
                    }
                    for (int i = 1; i <= c; i++) {
                        perm *= i+a+b;
                        perm /= i;
                    }
                    for (int i = 1; i <= d; i++) {
                        perm *= i+a+b+c;
                        perm /= i;
                    }

                    for (int i = 0; i < b-1; i++) {
                        perm *= 3;
                        perm %= MOD;
                    }
                    for (int i = 0; i < c-1; i++) {
                        perm *= 6;
                        perm %= MOD;
                    }
                    for (int i = 0; i < d-1; i++) {
                        perm *= 4;
                        perm %= MOD;
                    }
                    if (b > 0 && c > 0) {
                        perm *= 3;
                        perm %= MOD;
                    }
                    if (c > 0 && d > 0) {
                        perm *= 2;
                        perm %= MOD;
                    }
                    if (extra == 1) {
                        perm *= 2;
                        perm %= MOD;
                    }

                    ans += perm;
                    ans %= MOD;
                }
            }
        }
    }
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cin >> R >> C;

        ans = 0;
        solve();


        cout << "Case #" << testcase << ": ";
        cout << ans;
        cout << endl;
    }
    return 0;
}
