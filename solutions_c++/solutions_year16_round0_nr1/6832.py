#include <bits/stdc++.h>
using namespace std;
int func(int n)
{
    int hash = 0;
    for (int i = 1;i <= 80; i++)
    {
        int x, ans;
        ans = x = i * n;
        if (x == 0)
            hash |= 1<<x;
        while (x)
        {
            hash |= 1<<(x%10);
            x /= 10;           
        }
        if (hash == 1023)
        {
            return ans;
        }
    }
    return -1;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, n, cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &n);
        if (n == 0)
            printf("Case #%d: INSOMNIA\n", cas++);
        else
            printf("Case #%d: %d\n", cas++, func(n));

    }
	return 0;
}