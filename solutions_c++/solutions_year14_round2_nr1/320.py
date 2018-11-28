#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 110;

int n;
int l[MAXN];
string s[MAXN];

int sz;
char c[MAXN];
int d[MAXN][MAXN];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(testNum, T) {
        printf("Case #%d: ", testNum + 1);
        cin >> n;
        forn(i, n) {
            cin >> s[i];
            l[i] = s[i].length();
        }

        memset(d, 0, sizeof(d));
        sz = 1;
        c[0] = s[0][0];
        d[0][0] = 1;
        forab(i, 1, l[0]) {
            if (s[0][i] != s[0][i - 1]) {
                c[sz++] = s[0][i];
            }
            d[sz - 1][0]++;
        }

        bool good = 1;

        forab(i, 1, n) {
            if (!good)
                break;
            int k = 0;
            forn(j, l[i]) {
                if (j == 0 || s[i][j] != s[i][j - 1]) {
                    if (k >= sz || c[k] != s[i][j]) {
                        good = 0;
                        break;
                    }
                    k++;
                }
                d[k - 1][i]++;
            }
            if (k != sz) {
                good = 0;
                break;
            }
        }

        if (!good) {
            printf("Fegla Won\n");
            //cerr << s[0] << '\n' << s[1] << "\n\n";
            continue;
        }

        int ans = 0;

        forn(i, sz) {
            int cur = 100500;
            forab(j, 1, MAXN + 1) {
                int curcur = 0;
                forn(q, n)
                    curcur += abs(d[i][q] - j);
                cur = min(cur, curcur);
            }
            ans += cur;
        }

        printf("%d\n", ans);

    }
    return 0;
}
