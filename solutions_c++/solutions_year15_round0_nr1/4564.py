#include <iostream>
#include <cstdio>
#include <cstdlib>
int main(int argc, char *argv[]) {
    int T;
    scanf("%d", &T);
    for (int tat = 1; tat <= T; tat++) {
        int sumOfP = 0, sumOfO = 0;
        int n;
        char arr[2000];
        scanf("%d%s", &n, arr);
        for (int i = 0; i <= n; i++) {
            if (arr[i] == 0) continue;
            sumOfP += arr[i] - '0';
            if (sumOfO < i) {
                sumOfO = i;
            }
            sumOfO += arr[i] - '0';
        }
        printf("Case #%d: %d\n", tat, sumOfO - sumOfP);
    }
    return 0;
}
