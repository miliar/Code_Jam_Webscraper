#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const int N = 110;

char s[N][N];
int t[N][N];
bool b[N][N][4];

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
//    ios::sync_with_stdio(false);
//    cin.tie(nullptr);
    int tn;
    scanf("%d", &tn);
    for (int ti = 1; ti <= tn; ++ti) {
        int r, c;
        scanf("%d %d", &r, &c);
        for (int i = 1; i <= r; ++i) {
            scanf("%s", s[i] + 1);
            for (int j = 1; j <= c; ++j) {
                if (s[i][j] == '>') {
                    t[i][j] = 0;
                } else if (s[i][j] == '^') {
                    t[i][j] = 1;
                } else if (s[i][j] == '<') {
                    t[i][j] = 2;
                } else if (s[i][j] == 'v') {
                    t[i][j] = 3;
                }
            }
        }        
        memset(b, 0, sizeof(b));
        for (int i = 1; i <= r; ++i) {
            for (int j = 1; j <= c; ++j)
                if (s[i][j] != '.') {
                    b[i][j][2] = true;
                    break;
                }
            for (int j = c; j >= 1; --j)
                if (s[i][j] != '.') {
                    b[i][j][0] = true;
                    break;
                }
        }
        for (int j = 1; j <= c; ++j) {
            for (int i = 1; i <= r; ++i)
                if (s[i][j] != '.') {
                    b[i][j][1] = true;
                    break;
                }
            for (int i = r; i >= 1; --i)
                if (s[i][j] != '.') {
                    b[i][j][3] = true;
                    break;
                }
        }
        int answer = 0;
        bool possible = true;
        for (int i = 1; i <= r && possible; ++i)
            for (int j = 1; j <= c && possible; ++j)
                if (s[i][j] != '.') {
                    if (b[i][j][t[i][j]]) {
                        bool found = false;
                        for (int k = 0; k < 4; ++k)
                            if (b[i][j][k] == false) {
                                found = true;
                            }
                        if (found) {
                            answer++;
                        } else {
                            possible = false;
                        }
                    }
                }
        printf("Case #%d: ", ti);
        if (possible) {
            printf("%d\n", answer);
        } else {
            puts("IMPOSSIBLE");
        }
    }    
}
