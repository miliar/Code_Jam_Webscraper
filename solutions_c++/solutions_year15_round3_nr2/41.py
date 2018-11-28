#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

const int MAXC = 50;
const int MAXN = 111;
const double EPS = 1e-11;

int c[MAXC];
bool ff[MAXC];

int m, sL, n;
string L;

double f[MAXN][MAXN][MAXN];
int Z[MAXN];

double qwe() {
    for (int i = 0; i < L.length(); i++)
        if (c[L[i] - 'A'] == 0)
            return 0;

    int R = 0;
    Z[0] = -1;
    for (int i = 1; i <= L.length(); i++) {
        for (int j = i - 1; j >= 0; j--) {
            if (L.substr(0, j) == L.substr(i - j, j)) {
                Z[i] = j;
                break;
            }
        }
    }

    f[0][0][0] = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < L.size(); j++)
            for (int k = 0; k <= n; k++)
                if (f[i][j][k] > 0) {
                    int d = 0;
                    for (int o = 0; o < MAXC; o++)
                        ff[o] = false;

                    int z = j;
                    int M = m;
                    while (z >= 0) {
                        int C = L[z] - 'A';
                        if (!ff[C]) {
                            double r = f[i][j][k] * (double)c[C] / (double)m;
                            if (z + 1 == L.length()) {
                                f[i + 1][Z[z + 1]][k + 1] += r;
                                R = max(R, k + 1);
                            } else {
                                f[i + 1][z + 1][k] += r;
                            }
                            ff[C] = true;
                            M -= c[C];
                        }
                        z = Z[z];
                    }

                    double r = f[i][j][k] * (double)M / (double)m;
                    f[i + 1][0][k] += r;
                }

    double ans = 0;

//    cout << R << endl;
    for (int j = 0; j < L.size(); j++)
    for (int k = 0; k <= n; k++) {
            ans += ((double)(R - k) * f[n][j][k]);
//            printf("(%d %d %d) = %.6lf\n", n, j, k, f[n][j][k]);
    }
    return ans;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        for (int i = 0; i < MAXC; i++)
            c[i] = 0;
        for (int i = 0; i < MAXN; i++)
            for (int j = 0; j < MAXN; j++)
                for (int k = 0; k < MAXN; k++)
                    f[i][j][k] = 0;
        cin >> m >> sL >> n;

        string s;
        cin >> s;
        for (int i = 0; i < s.length(); i++)
            c[s[i] - 'A']++;

        cin >> L;

        printf("%.6lf\n", qwe());
    }

    return 0;
}
