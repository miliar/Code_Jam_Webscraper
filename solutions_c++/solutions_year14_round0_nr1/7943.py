#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int cnt[17];

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int _, p, q;
    cin >> _;
    for (int __ = 1; __ <= _; ++ __){
        printf("Case #%d: ", __);
        memset(cnt, 0, sizeof(cnt));
        scanf("%d", &p);
        for (int i = 1; i <= 4; ++i){
            for (int j = 1; j <= 4; ++j){
                scanf("%d", &q);
                if (p == i){
                    cnt[q]++;
                }
            }
        }
        scanf("%d", &p);
        for (int i = 1; i <= 4; ++i){
            for (int j = 1; j <= 4; ++j){
                scanf("%d", &q);
                if (p == i){
                    cnt[q]++;
                }
            }
        }
        int flag = 0;
        int ans = 0;
        for (int i = 1; i <= 16; ++i){
            if (cnt[i] > 1){
                flag++;
                ans = i;
            }
        }
        if (flag == 0){
            puts("Volunteer cheated!");
        }else if (flag == 1){
            printf("%d\n", ans);
        }else {
            puts("Bad magician!");
        }
    }
    return 0;
}
