#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
bool digital[10];
bool check(long long n)
{
    while(n)
    {
        digital[n % 10LL] = true;
        n /= 10LL;
    }
    for (int i = 0; i < 10; ++i)
    {
        if (!digital[i]) return false;
    }
    return true;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt","w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        long long n;
        memset(digital, false, sizeof(digital));
        cin >> n;
        if (n == 0)
            printf("INSOMNIA\n");
        else
        {
            int t = n;
            while(1)
            {
                bool can = check(n);
                if (can) break;
                else n += t;
            }
            printf("%I64d\n", n);
        }

    }
    return 0;
}
