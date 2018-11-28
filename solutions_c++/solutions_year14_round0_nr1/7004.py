//  test
//  File.cpp
/*
    ID: Firwaless
    LANG: C++
    TASK: 
*/

#include <cstdio>

int main()
{
    //freopen("/Users/firwaless/Downloads/A-small-attempt0.in.txt", "r", stdin);
    //freopen("/Users/firwaless/Downloads/A-small-attempt0.out.txt", "w", stdout);
    
    int T, t, n, m, i, j, same, ans;
    int a[4][4], b[4][4];
    
    scanf("%i", &T);
    for (t = 1; t <= T; ++t) {
        same = 0;
        scanf("%i", &n);
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                scanf("%i", &a[i][j]);
            }
        }
        scanf("%i", &m);
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                scanf("%i", &b[i][j]);
            }
        }
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                if (a[n - 1][i] == b[m - 1][j]) {
                    ++same;
                    ans = a[n - 1][i];
                }
            }
        }
        printf("Case #%i: ", t);
        if (same == 0) {
            puts("Volunteer cheated!");
        } else if (same == 1) {
            printf("%i\n", ans);
        } else {
            puts("Bad magician!");
        }
    }
    return 0;
}