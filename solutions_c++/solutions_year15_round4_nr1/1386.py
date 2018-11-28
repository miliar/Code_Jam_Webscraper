/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

const int maxsz = 100;
char a[maxsz][maxsz];
int l[maxsz], r[maxsz], t[maxsz], b[maxsz];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    cin >> skipws;
    for (int T = 1; T <= TN; T++) {
        int w, h;
        cin >> h >> w;
        for (int i = 0; i < w; ++i) {
            t[i] = -1;
        }
        for (int i = 0; i < h; ++i) {
            l[i] = -1;
            for (int j = 0; j < w; ++j) {
                cin >> a[i][j];
                if (a[i][j] != '.') {
                    if (l[i] < 0) {
                        l[i] = j;
                    }
                    if (t[j] < 0) {
                        t[j] = i;
                    }
                    r[i] = j;
                    b[j] = i;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                switch (a[i][j]) {
                case '<':
                    if (l[i] < j) {
                        continue;
                    }
                    break;
                case '>':
                    if (r[i] > j) {
                        continue;
                    }
                    break;
                case '^':
                    if (t[j] < i) {
                        continue;
                    }
                    break;
                case 'v':
                    if (b[j] > i) {
                        continue;
                    }
                    break;
                default:
                    continue;
                }
                if (l[i] < r[i] || t[j] < b[j]) {
                    ans++;
                } else {
                    ans = -1;
                    break;
                }
            }
            if (ans < 0) {
                break;
            }
        }
        cout << "Case #" << T << ": ";
        if (ans < 0) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }
    return 0;
}
