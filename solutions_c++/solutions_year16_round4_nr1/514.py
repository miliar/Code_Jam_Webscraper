#include <iostream>
using namespace std;
string x = "RPS";
int dat[13][(1<<12)+1];
int op[3] = {2, 0, 1};
int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        int kr, kp, ks;
        string ans;
        bool find = false;
        // r
        kr = 0; kp = 0; ks = 0;
        dat[0][0] = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < (1<<(i-1)); ++j) {
                dat[i][j*2] = dat[i-1][j];
                dat[i][j*2+1] = op[dat[i-1][j]];
                if (x[dat[i][j*2]] > x[dat[i][j*2+1]]) {
                    swap(dat[i][j*2], dat[i][j*2+1]);
                }
            }
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < (1<<(n-i)); ++j) {
                string a, b;
                int step = (1<<i);
                for (int k = j*step; k < j*step+(step/2); ++k) {
                    // cout << "adding-a " << k << endl;
                    a += x[dat[n][k]];
                }
                for (int k = j*step+(step/2); k < (j+1)*step; ++k) {
                    // cout << "adding-a " << k << endl;
                    b += x[dat[n][k]];
                }
                // cout << "DIFF " << a << " " << b << endl;
                if (a > b) {
                    for (int k = j*step; k < j*step+(step/2); ++k) {
                        swap(dat[n][k], dat[n][k+(step/2)]);
                    }
                }
            }
        }
        string now = "";
        // cout << (1 << n) << endl;
        for (int i = 0; i < (1<<n); ++i) {
            now += x[dat[n][i]];
            kr += (dat[n][i] == 0);
            kp += (dat[n][i] == 1);
            ks += (dat[n][i] == 2);
            // cout << i << " " << kr << " " << kp << " " << ks << " " << now << endl;

        }
        // cout << "EY" << kr << " " << kp << " " << ks << " " << now << endl;
        if (kr == r && kp == p && ks == s) {
            if (!find) {
                ans = now;
                find = true;
            } else {
                ans = min(ans, now);
            }
        }
        // p
        kr = 0; kp = 0; ks = 0;
        dat[0][0] = 1;
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < (1<<(i-1)); ++j) {
                dat[i][j*2] = dat[i-1][j];
                dat[i][j*2+1] = op[dat[i-1][j]];
                if (x[dat[i][j*2]] > x[dat[i][j*2+1]]) {
                    swap(dat[i][j*2], dat[i][j*2+1]);
                }
            }
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < (1<<(n-i)); ++j) {
                string a, b;
                int step = (1<<i);
                for (int k = j*step; k < j*step+(step/2); ++k) {
                    // cout << "adding-a " << k << endl;
                    a += x[dat[n][k]];
                }
                for (int k = j*step+(step/2); k < (j+1)*step; ++k) {
                    // cout << "adding-a " << k << endl;
                    b += x[dat[n][k]];
                }
                // cout << "DIFF " << a << " " << b << endl;
                if (a > b) {
                    for (int k = j*step; k < j*step+(step/2); ++k) {
                        swap(dat[n][k], dat[n][k+(step/2)]);
                    }
                }
            }
        }
        now = "";
        for (int i = 0; i < (1<<n); ++i) {
            now += x[dat[n][i]];
            kr += (dat[n][i] == 0);
            kp += (dat[n][i] == 1);
            ks += (dat[n][i] == 2);
            // cout << i << " " << kr << " " << kp << " " << ks << " " << now << endl;

        }
        // cout << "EY" << kr << " " << kp << " " << ks << " " << now << endl;

        if (kr == r && kp == p && ks == s) {
            if (!find) {
                ans = now;
                find = true;
            } else {
                ans = min(ans, now);
            }
        }
        // s
        kr = 0; kp = 0; ks = 0;
        dat[0][0] = 2;
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < (1<<(i-1)); ++j) {
                dat[i][j*2] = dat[i-1][j];
                dat[i][j*2+1] = op[dat[i-1][j]];
                if (x[dat[i][j*2]] > x[dat[i][j*2+1]]) {
                    swap(dat[i][j*2], dat[i][j*2+1]);
                }
            }
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < (1<<(n-i)); ++j) {
                string a, b;
                int step = (1<<i);
                for (int k = j*step; k < j*step+(step/2); ++k) {
                    a += x[dat[n][k]];
                }
                for (int k = j*step+(step/2); k < (j+1)*step; ++k) {
                    b += x[dat[n][k]];
                }
                // cout << "DIFF " << a << " " << b << endl;
                if (a > b) {
                    for (int k = j*step; k < j*step+(step/2); ++k) {
                        swap(dat[n][k], dat[n][k+(step/2)]);
                    }
                }
            }
        }
        now = "";
        for (int i = 0; i < (1<<n); ++i) {
            now += x[dat[n][i]];
            kr += (dat[n][i] == 0);
            kp += (dat[n][i] == 1);
            ks += (dat[n][i] == 2);
            // cout << i << " " << kr << " " << kp << " " << ks << " " << now << endl;

        }
        // cout << "EY" << kr << " " << kp << " " << ks << " " << now << endl;

        if (kr == r && kp == p && ks == s) {
            if (!find) {
                ans = now;
                find = true;
            } else {
                ans = min(ans, now);
            }
        }
        printf("Case #%d: ", ca);
        if (!find) {
            puts("IMPOSSIBLE");
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}
