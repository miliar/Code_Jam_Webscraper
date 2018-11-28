#include<cstdio>
#include<cmath>
#include<map>
using namespace std;
#define N 16
#define M 100000000
#define J 50
typedef long long LL;

LL check(LL n);
void addOne(int* binary);
int main()
{
    freopen("CS.out", "w", stdout);
    puts("Case #1:");

    LL  sum[11] = {}, div[11] = {};
    int i, j;
    int set = 0;

    int ans[N] = { 1 };
    ans[N - 1] = 1;
    while (set < J)
    {
        for (i = 2; i <= 10; i++)
        {
            sum[i] = 0;
            for (j = 0; j < N; j++)
                sum[i] = sum[i] * i + ans[j];

            if (!(div[i] = check(sum[i])))
            {

                addOne(ans);
                i = 1;
                continue;
            }
        }

        for (i = 0; i < N; i++)
            printf("%d", ans[i]);

        for (i = 2; i <= 10; i++)
            printf(" %d", div[i]);
        putchar('\n');

        addOne(ans);
        set++;
    }


    return 0;
}
void addOne(int* binary)
{
    binary[1]++;
    for (int i = 1; i < N - 1; i++)
        if (binary[i]>1)
            binary[i] = 0, binary[i + 1]++;
}
LL check(LL n)
{
    LL ans = 0;
    int _sqrt = sqrt(n);
    for (LL i = 2; i <= _sqrt; i++)
        if (!(n%i))
            ans = i;
    return ans;
}