#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int cas=1; cas<=T; ++cas) {
        int r, vis[17] = {0};
        for (int k=0; k<2; ++k) {
            scanf("%d", &r);
            for (int i=1; i<=4; ++i) {
                for (int j=0; j<4; ++j) {
                    int num;
                    scanf("%d", &num);
                    if (r == i)
                        vis[num]++;
                }
            }
        }

        int ans = 0, cnt = 0;
        for (int i=1; i<=16; ++i)
            if (vis[i] == 2) {
                ans = i;
                cnt ++;
            }
        
        printf("Case #%d: ", cas);
        if (cnt == 0)
            printf("Volunteer cheated!\n");
        else if (cnt > 1)
            printf("Bad magician!\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}
