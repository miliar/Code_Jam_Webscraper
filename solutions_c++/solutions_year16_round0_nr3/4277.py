#include <bits/stdc++.h>

#define sd(x)       scanf("%d", &x)
#define slld(x)     scanf("%lld", &x)
#define sc(x)       scanf("%c", &x)
#define pd(x)       printf("%d", x)
#define plld(x)     printf("%lld\n", x)
#define pc(x)       printf("%c", x)
#define pdln(x)     printf("%d\n", x)
#define prl(x)      cout << x << endl
#define LL          long long
#define forn(i, n)  for(int i = 0; i < (int)n; i++)
#define fori(i, n)  for(int i = 1; i <= (int)n; i++)
#define revn(i, n)  for(int i = (int)(n - 1); i >= 0; i--)
#define pb          push_back
#define pii         pair <int, int>

#define mem(x, y)   memset(x, y, sizeof(x))
#define MAX         100002
#define MOD         1000000007

using namespace std;

char str[100];

LL getDiv(LL n)
{
    if(n % 2 == 0)
    {
        return 2;
    }
    for(LL i = 3; i <= sqrt(n); i = i + 2)
    {
        if(n % i == 0)
        {
            return i;
            n = n / i;
        }
    }
    if(n > 2) return n;
}

void store(int d, int n)
{
    str[0] = '1';
    int i = 1;
    int m = 1 << (d - 1);
    for(i = 1; i <= d; i++)
    {
        if(n & m) str[i] = '1';
        else str[i] = '0';
        m = m >> 1;
    }
    str[i] = '1';
    str[i + 1] = '\0';
}

LL conv(int base)
{
    LL ret = 0;
    char *c = str;
    while(*c)
    {
        ret *= base;
        ret += (LL)(*c - '0');
        c++;
    }
    return ret;
}

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("C-small.out", "w", stdout);
    int test, caseno;
    int n, j;
    LL arr[10];
    sd(test);
    for(caseno = 1; caseno <= test; caseno++)
    {
        printf("Case #%d:\n", caseno);
        int cnt = 0;
        sd(n); sd(j);
        int m = (1 << (n - 2)) - 1;
        for(int i = 0; i <= m && cnt < j; i++)
        {
            store((n - 2), i);
            for(int b = 2; b <= 10; b++)
            {
                LL val = conv(b);
                LL p = getDiv(val);
                if(p == val) goto lab;
                arr[b - 2] = p;
            }
            printf("%s", str);
            for(int j = 0; j < 9; j++)
            {
                printf(" %lld", arr[j]);
            }
            printf("\n");
            cnt++;
            lab:;
        }
    }
    return 0;
}


