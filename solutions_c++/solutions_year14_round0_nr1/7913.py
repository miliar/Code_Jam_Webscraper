#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

int t, r1;
int a[20];
int b[5][5];

int main() {
    freopen("/Users/dong/Downloads/A-small-attempt0.in", "r", stdin);
    freopen("/Users/dong/Downloads/out.txt", "w", stdout);
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        memset(a, 0, sizeof(a));
        
        scanf("%d", &r1);
        for (int i1 = 0; i1 < 4; i1++)
            for (int i2 = 0; i2 < 4; i2++)
                scanf("%d", &b[i1][i2]);
        for (int i1 = 0; i1 < 4; i1++)
            a[b[r1 - 1][i1]]++;
        
        scanf("%d", &r1);
        for (int i1 = 0; i1 < 4; i1++)
            for (int i2 = 0; i2 < 4; i2++)
                scanf("%d", &b[i1][i2]);
        for (int i1 = 0; i1 < 4; i1++)
            a[b[r1 - 1][i1]]++;
        
        int cnt = 0;
        for (int i1 = 0; i1 < 20; ++i1) {
            if (a[i1] == 2) cnt++;
        }
        if (cnt == 0)
            printf("Case #%d: Volunteer cheated!\n", i + 1);
        if (cnt > 1)
            printf("Case #%d: Bad magician!\n", i + 1);
        if (cnt == 1)
            for (int i1 = 0; i1 < 20; ++i1)
                if (a[i1] == 2)
                    printf("Case #%d: %d\n", i + 1, i1);
    }
    return 0;
}
