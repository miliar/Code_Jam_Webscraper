#include <cstdio>
#include <cmath>

bool isPalindrome(int n)
{
    int temp = n;
    int rev = 0;
    while (temp > 0) {
        int dig = temp % 10;
        rev = rev * 10 + dig;
        temp /= 10;
    }
    return (n == rev);
}

bool isSquare(int n)
{
    double s = sqrt((double)n);
    int si = floor(s + 0.5);
    return (si*si == n && isPalindrome(si));
}

int main()
{
    int t;
    scanf("%d", &t);
    FILE *pFile = fopen("out.txt", "w");
    for (int i = 1; i <= t; ++i) {
        int a, b, k;
        scanf("%d %d", &a, &b);
        k = 0;
        for (int j = a; j <= b; ++j) {
            if (isSquare(j) && isPalindrome(j))
                ++k;
        }
        fprintf(pFile, "Case #%d: %d\n", i, k);
    }
    fclose(pFile);
    return 0;
}