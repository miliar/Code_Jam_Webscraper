#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cctype>

using namespace std;

#define MAXN 1024

int n, m;
int h[MAXN][MAXN];

int main () {
    int casos;
    scanf ("%d", &casos);

    for (int caso = 1; caso <= casos; ++caso) {
        scanf ("%d %d", &n, &m);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                scanf ("%d", &h[i][j]);
            }
        }

        bool ok = true;
        for (int i = 0; i < n && ok; ++i) {
            for (int j = 0; j < m && ok; ++j) {
                bool vertical = true;
                bool horizontal = true;
                for (int k = 0; k < n && vertical; ++k) {
                    if (h[k][j] > h[i][j]) {
                        vertical = false;
                    }
                }

                for (int k = 0; k < m && horizontal; ++k) {
                    if (h[i][k] > h[i][j]) {
                        horizontal = false;
                    }
                }

                ok = ok && (vertical || horizontal);
            }
        }

        printf ("Case #%d: ", caso);
        if (ok) printf ("YES\n");
        else printf ("NO\n");
    }

    return 0;
}

