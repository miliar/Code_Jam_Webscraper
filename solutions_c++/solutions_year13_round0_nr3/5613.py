#include <iostream>
#include <cstdio>
using namespace std;

int palindrome(int n) {
    int m = 0, nn = n;
    while (n) {
        m = m * 10 + (n%10);
        n /= 10;
    }
    return m == nn;
}

int main() {
    int T, A, B;

    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);

        scanf("%d %d\n", &A, &B);

        int res = 0;
        for (int n, i = 1; i <= B; i++) {
            if (!palindrome(i)) continue ;
            n = i * i;
            if (n > B) break;
            if (!palindrome(n)) continue ;

            if (A <= n && n <= B) res++;
        }
        printf("%d\n", res);
    }

    return 0;
}
