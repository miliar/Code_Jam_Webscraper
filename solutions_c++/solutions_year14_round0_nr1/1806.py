#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
using namespace std;

int cnt[20];
int main() {    
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < 2; i++) {
            int cr;
            scanf("%d", &cr);
            for (int x = 1; x <= 4; x++)
                for (int y = 1; y <= 4; y++) {
                    int val;
                    scanf("%d", &val);
                    if (x == cr) {
                        cnt[val]++;
                    }
                }
        }
        int ans = -1;
        for (int i = 1; i <= 16; i++)
            if (cnt[i] == 2) {
                if (ans < 0) {
                    ans = i;
                } else {
                    ans = -2;
                    break;
                }
            }
        printf("Case #%d: ", t);
        if (ans == -1) 
            printf("Volunteer cheated!");
        else if (ans == -2)
            printf("Bad magician!");
        else printf("%d", ans);
        printf("\n");
    }
}

