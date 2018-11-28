#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define SIZE 7
#define INF 2147483647

struct TableInfo
{
    int C[10];

    TableInfo()
    {
        memset(C, 0, sizeof C);
    }
};

int A[SIZE];

int backtrack(TableInfo t)
{
    int c, i, j;

    for(i = 9; i && !t.C[i]; --i);

    if(!i)
        return 0;

    TableInfo temp = t;
    c = i;
    for(j = 1; j<i; ++j)
    {
        temp.C[j] += t.C[i], temp.C[i-j] += t.C[i], temp.C[i] = 0;

        c = min(c, t.C[i]+backtrack(temp));

        temp.C[j] -= t.C[i], temp.C[i-j] -= t.C[i], temp.C[i] = t.C[i];
    }

    return c;
}

int solve(int n)
{
    int i;
    TableInfo t;

    for(i = 0; i<n; ++i)
        t.C[A[i]]++;

    return backtrack(t);
}

int main()
{
    int test, t = 1, n, i;

    for(scanf("%d", &test); t<=test; ++t)
    {
        scanf("%d", &n);

        for(i = 0; i<n; ++i)
            scanf("%d", A+i);

        printf("Case #%d: %d\n", t, solve(n));
    }

    return 0;
}
