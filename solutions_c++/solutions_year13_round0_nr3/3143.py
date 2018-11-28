#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

const double EPS = 1e-6;

bool check_palindrome(int x) {
    int len = 0;
    static int d[10];
    while (x) d[len++] = x % 10, x /= 10;
    for (int i = 0, j = len - 1; i <= j; i++, j--)
        if (d[i] != d[j]) return false;
    return true;
}

bool check(int x) {
    int xx = sqrt(x + EPS);
    if (xx * xx != x) return false;
    return check_palindrome(x) && check_palindrome(xx);
}

int main() {

    int T, A, B;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        scanf("%d %d", &A, &B);
        int ans = 0;
        for (int x = A; x <= B; x++)
            ans += check(x);
        printf("Case #%d: %d\n", i + 1, ans);
    }

    return 0;
}
