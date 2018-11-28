#include <cstdio>
#include <cstring>

char audience[1005];
int T, S;
int main(void) {
    scanf("%d", &T); 
    for (int t = 1; t <= T; t++) {
        int friends = 0, stand_up = 0;
        scanf("%d", &S);
        scanf("%s", audience);
        for (int i = 0; i <= S; i++) {
            int y = audience[i] - '0';
            if (stand_up + friends < i) friends += (i - stand_up - friends);
            stand_up += y;
        }
        printf("Case #%d: %d\n", t, friends);
    }
    return 0;
}
