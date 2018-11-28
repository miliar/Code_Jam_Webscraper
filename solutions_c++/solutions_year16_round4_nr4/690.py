#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>

using namespace std;

#define y1 ym37s62rw
#define x1 xm2ash4ad
#define pb push_back
#define mp make_pair
#define F first
#define S second

const int INF = 1000000007;
const long long INFll = 1000000007000000007ll;
const int MOD = 1000000007;

char a[10][10];
char b[10][10];

int main() {

    ios_base::sync_with_stdio(0);

#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
#endif
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cout << "Case #" << i + 1 << ": ";
        int n;
        cin >> n;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> a[i][j];
            }
        }

        int N = (1 << (n * n));
        int ans = n * n;

        for (int mask = 0; mask < N; ++mask) {
            for (int l = 0; l < n * n; ++l) {
                if (((1 << l) & mask) > 0) {
                    b[l / n][l % n] = '1';
                }
                else
                    b[l / n][l % n] = '0';
            }
            bool bad = 0;
            int cost = 0;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (a[i][j] == '1' && b[i][j] == '0') {
                        bad = 1;
                        break;
                    }
                    if (a[i][j] != b[i][j])
                        cost++;
                }
            }
            if (bad || cost > ans)
                continue;

            int g = 0;
            for (int i = 0; i < n; ++i) {
                int w = 0;
                int q = 0;
                for (int j = 0; j < n; ++j) {
                    if (b[i][j] == '0')
                        continue;
                    w++;
                    for (int k = 0; k < n; ++k) {
                        if (b[k][j] == '1' && k != i) {
                            q++;
                            for (int h = 0; h < n; ++h) {
                                if (b[k][h] == '0' && b[i][h] == '1') {
                                    bad = 1;
                                    break;
                                }
                            }
                        }
                        if (bad)
                            break;
                    }
                    if (bad)
                        break;
                }
                //cerr << bad << endl;
                if (w > 0)
                    g++;
                if (bad)
                    break;
            }
            if (g != n)
                bad = 1;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (b[i][j] == '0')
                        continue;
                    int e = 0;
                    for (int k = 0; k < n; ++k) {
                        if (b[k][j] == '1')
                            e++;
                    }
                    for (int k = 0; k < n; ++k)
                        if (b[i][k] == '1')
                        e--;
                    if (e > 0) {
                        bad = 1;
                        break;
                    }
                }
            }
            if (!bad) {
                ans = min(ans, cost);
                /*for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    cerr << b[i][j] << " ";
                }
                cerr << endl;
            }
            cerr << cost << endl;
            */
            }
        }
        cout << ans << endl;
    }

    return 0;
}
