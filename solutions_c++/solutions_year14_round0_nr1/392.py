#include<iostream>
#include<algorithm>
#include<cstring>
#include<ctime>
#include<cmath>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;

int a[4][4], b[4][4];

int main() {
    int t, x, y;
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &t);
    for(int cas = 1; cas <= t; ++cas) {
        scanf("%d", &x);
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j) scanf("%d", &a[i][j]);

        scanf("%d", &y);
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j) scanf("%d", &b[i][j]);

        int num  = 0, m;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                if(a[x-1][i] == b[y-1][j]) {
                    num++;
                    m = a[x-1][i];
                    break;
                }
            }
        }

        if(num == 0) {
            printf("Case #%d: Volunteer cheated!\n", cas);
        }
        else if(num == 1) {
            printf("Case #%d: %d\n", cas, m);
        }
        else {
            printf("Case #%d: Bad magician!\n", cas);
        }

    }
    return 0;
}
