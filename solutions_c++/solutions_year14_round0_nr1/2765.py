#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {
    freopen("D:\\A-small-attempt1.in", "r", stdin);
    freopen("D:\\A-small-attempt1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        int n, m;
        int a[6][6], temp[6];
        bool hash[40];
        memset(a, 0, sizeof(a));
        memset(hash, false, sizeof(hash));
        scanf("%d", &n);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &a[i][j]);
            }
        }
        for (int i = 1; i <= 4; i++) {
            hash[a[n][i]] = true;
        }
        int cnt = 0;
        scanf("%d", &m);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &a[i][j]);
            }
        }
        for (int i = 1; i <= 4; i++) {
            temp[i] = a[m][i];
        }
        int num;
        for (int i = 1; i <= 4; i++) {
            if (hash[temp[i]] == true) {
                cnt++;
                num = temp[i];
            }
        }
        printf("Case #%d: ", z);
        if (cnt == 1) {
            printf("%d\n", num);
        } else if(cnt > 1) {
            printf("Bad magician!\n");
        } else {
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
