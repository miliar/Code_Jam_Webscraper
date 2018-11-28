#include<cstdio>
using namespace std;

#define SIZE 1003

int A[SIZE];

int solve(int n)
{
    int c = 0, sum = A[0], i;

    for(i = 1; i<=n; ++i)
    {
        if(A[i] && sum<i)
            c += i-sum, sum = i;

        sum += A[i];
    }

    return c;
}

int main()
{
    int test, t = 1, n, i;

    for(scanf("%d", &test); t<=test; ++t)
    {
        scanf("%d", &n);
        for(i = 0; i<=n; ++i)
            scanf("%1d", A+i);

        printf("Case #%d: %d\n", t, solve(n));
    }

    return 0;
}
