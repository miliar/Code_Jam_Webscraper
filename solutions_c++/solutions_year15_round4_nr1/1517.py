#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
const int NMAX = 201;
const int LN = 21;
using namespace std;

int rowMove[] = {0, 0, 1, -1};
int colMove[] = {1, -1, 0, 0};
char arr[] = {'>', '<', 'v', '^'};

char s[NMAX][NMAX];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int r, c;
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; i++) scanf("%s", s[i]);
        int res = 0;
        for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            if (s[i][j] == '.') continue;
            if (res == -1) break;
            bool ok = false;
            bool ok2 = false;
            for (int k = 0; k < 4; k++) {
                bool ok3 = false;
                int ii = i + rowMove[k], jj = j + colMove[k];
                while (ii >= 0 && ii < r && jj >= 0 && jj < c) {
                    if (s[ii][jj] != '.') {
                        ok3 = true;
                        break;
                    }
                    ii += rowMove[k];
                    jj += colMove[k];
                }
                if (ok3) {
                    ok2 = true;
                    if (arr[k] == s[i][j]) ok = true;
                }
            }
            if (ok2 and !ok) res++;
            else if(!ok2) res = -1;
        }
        printf("Case #%d: ", t);
        if (res == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", res);
    }
    return 0;
}