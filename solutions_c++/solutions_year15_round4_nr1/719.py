#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <vector>

using namespace std;

bool in[111][111];
int n, m, ctx[111], cty[111];
char a[111][111];


void work(int testcase) {
    scanf("%d%d", &n, &m);
    for(int i = 0; i < n; ++i) {
        scanf("%s", a[i]);
    }
    memset(in, 0, sizeof(in));
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j)
            if(a[i][j] != '.') {
                if(a[i][j] == '>') {
                    for(int k = j + 1; k < m; ++k)
                        if(a[i][k] != '.') {
                            in[i][j] = true;
                        }
                } else if(a[i][j] == '<') {
                    for(int k = j - 1; k >= 0; --k)
                        if(a[i][k] != '.') {
                            in[i][j] = true;
                        }
                } else if(a[i][j] == 'v') {
                    for(int k = i + 1; k < n; ++k)
                        if(a[k][j] != '.') {
                            in[i][j] = true;
                        }
                } else if(a[i][j] == '^') {
                    for(int k = i - 1; k >= 0; --k)
                        if(a[k][j] != '.') {
                            in[i][j] = true;
                        }
                }
            }
    int ans = 0;
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j)
            if(a[i][j] != '.' && !in[i][j]) {
                ans++;
            }
    memset(ctx, 0, sizeof(ctx));
    memset(cty, 0, sizeof(cty));
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j) {
            if(a[i][j] != '.') {
                ctx[i]++, cty[j]++;
            }
        }
    bool flag = true;
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j)
            if(a[i][j] != '.') {
                if(ctx[i] == 1 && cty[j] == 1) {
                    flag = false;
                    break;
                }
            }
    printf("Case #%d: ", testcase);
    if(flag) {
        printf("%d\n", ans);
    } else {
        printf("IMPOSSIBLE\n");
    }
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int TC;
    scanf("%d", &TC);
    for(int i = 1; i <= TC; ++i) {
        work(i);
    }
    return 0;
}