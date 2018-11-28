#include <cstdio>
#include <cmath>

bool palindrome(long long x)
{
    long long int nx = 0;
    long long int n = x;
    while (x)
    {
        int m = x % 10;
        x /= 10;
        nx = nx * 10 + m;
    }
    // printf("P %lld %lld\n", n, nx);
    return nx == n;
}

int T;
long long int A, B;

int main()
{
    // palindrome(12345677654321);
    // palindrome(12345678912345);
    freopen("fair.in", "r", stdin);
    freopen("fair.out", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        int count = 0;
        scanf("%lld %lld", &A, &B);
        int sA = sqrt(A);
        int sB = sqrt(B);
        for (int i = sA; i <= sB; i++)
        {
            if (palindrome(i) && palindrome(i * i) && (i * i >= A) && (i * i <= B))
            {
                // printf("%d\n", i);
                count++;
            }
        }
        printf("Case #%d: %d\n", t, count);
    }
    return 0;
}
