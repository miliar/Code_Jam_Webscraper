#include <cstdio>

using namespace std;

int main() {
    int T, i, j, ans, op1, op2, op3, op4, tmp, card;
    scanf("%d", &T);
    for(i = 0; i < T; ++i) {
        scanf("%d", &ans);
        --ans;
        for(j = 0; j < ans; ++j) {
            scanf("%*d %*d %*d %*d");
        }
        scanf("%d %d %d %d", &op1, &op2, &op3, &op4);
        for(j = ans+1; j < 4; ++j) {
            scanf("%*d %*d %*d %*d");
        }
        scanf("%d", &ans);
        ans--;
        for(j = 0; j < ans; ++j) {
            scanf("%*d %*d %*d %*d");
        }
        card = -1;
        scanf("%d", &tmp);
        if(tmp == op1 || tmp == op2 || tmp == op3 || tmp == op4) {
            card = tmp;
        }
        scanf("%d", &tmp);
        if(tmp == op1 || tmp == op2 || tmp == op3 || tmp == op4) {
            if(card == -1) {
                card = tmp;
            } else {
                card = -2;
            }
        }
        scanf("%d", &tmp);
        if(tmp == op1 || tmp == op2 || tmp == op3 || tmp == op4) {
            if(card == -1) {
                card = tmp;
            } else {
                card = -2;
            }
        }
        scanf("%d", &tmp);
        if(tmp == op1 || tmp == op2 || tmp == op3 || tmp == op4) {
            if(card == -1) {
                card = tmp;
            } else {
                card = -2;
            }
        }
        for(j = ans+1; j < 4; ++j) {
            scanf("%*d %*d %*d %*d");
        }
        if(card > 0) {
            printf("Case #%d: %d\n", i+1, card);
        } else if(card == -1) {
            printf("Case #%d: Volunteer cheated!\n", i+1);
        } else {
            printf("Case #%d: Bad magician!\n", i+1);
        }
    }
    scanf("%d");
    return 0;
}
