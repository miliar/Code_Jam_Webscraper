#include <cstdio>

int solve(int* s, int sMax) {
    int friendToBring = 0;
    int totalClapping = 0;
    for (int i = 0; i < sMax; ++i) {
        if (totalClapping < i) {
            int extraNeeded = i - totalClapping;
            friendToBring += extraNeeded;
            totalClapping += extraNeeded;
        }
        totalClapping += *s;
        ++s;
    }
    return friendToBring;
}

int main(){
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        int sMax;
        scanf("%d", &sMax);
        int* s = new int[++sMax];
        for (int* j = s; j < s + sMax; ++j) {
            scanf("%1d", j);
        }

        int answer = solve(s, sMax);

        // Print answer
        printf("Case #%d: %d\n", i, answer);
    }
    return 0;
}
