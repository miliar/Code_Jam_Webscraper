#include <stdio.h>
using namespace std;

int T, N;

bool number[10];

bool check(int digit)
{
    int temp = digit;
    int idx = 0;
    int n = 1;
    while (temp)
    {
        temp /= 10;
        idx++;
        n *= 10;
    }
    n /= 10;
    temp = digit;
    for (int i = 0; i < idx; ++i)
    {
        int a = temp / n;
        number[a] = true;
        temp %= n;
        n /= 10;
    }
    bool ret = true;
    for (int i = 0; i < 10; ++i)
    {
        if (number[i] == false)
            return false;
    }
    return ret;
}

int solve()
{
    if (N == 0) return -1;
    int num = N;
    int i = 1;
    while (num < 2147483647)
    {
        num = N * i;
        if (check(num)) return num;
        i++;
    }
    return -1;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        for (int i = 0; i < 10; ++i) number[i] = false;
        scanf("%d", &N);
        int ans = solve();
        if(ans == -1) printf("Case #%d: INSOMNIA\n", t);
        else printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}