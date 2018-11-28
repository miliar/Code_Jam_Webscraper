#include<iostream>
#include<cstdio>
#include<cstring>
#define LL long long
using namespace std;

LL N, J, cnt, Base;
LL prime[10] = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
LL d16[15], p[505][15], ans[505], s[100];

void init_d16()
{
    int i, j;
    for (i = 2; i <= 10; i++)
    {
        d16[i] = 1;
        for (j = 1; j <= 16; j++)
            d16[i] *= i;
    }
}

LL change(LL x, LL d)
{
    LL ret = 0;
    LL y = 1;
    while (x > 0)
    {
        ret += (x & 1) * y;
        x = (x >> 1LL);
        y *= d;
    }
    return ret;
}

LL check(LL x, LL d)
{
    LL x2 = x % (1LL << 16);
    LL x1 = (x >> 16);
    x1 = change(x1, d);
    x2 = change(x2, d);
    for (LL i = 0; i < 10; i++)
    {
        LL r1 = x1 % prime[i];
        LL r2 = (r1 * d16[d] + x2) % prime[i];
        if (r2 == 0) return prime[i];
    }
    return -1;
}

void outpt()
{
    printf("Case #1:\n");
    for (LL k = 0; k < cnt; k++)
    {
        for (LL i = 1; i <= N; i++)
        {
            s[i] = (ans[k] & 1);
            ans[k] = (ans[k] >> 1);
        }
        for (LL i = N; i >= 1; i--)
            printf("%d", s[i]);
        for (LL i = 2; i <= 10; i++)
            printf(" %d", p[k][i]);
        printf("\n");
    }
}

int main()
{
 //   freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);

    N = 16;
    J = 50;

    init_d16;
    Base = (1LL << (N - 1)) + 1;
    cnt = 0;

    for (LL i = 0; i < (1LL << (N - 2)); i++)
    {
        bool flag = true;
        LL x = Base + (i << 1LL);
        for (LL j = 2; j <= 10; j++)
        {
            p[cnt][j] = check(x, j);
            if (p[cnt][j] == -1)
            {
                flag = false;
                break;
            }
        }
        if (flag)
        {
            ans[cnt] = x;
            cnt++;
        }
        if (cnt == J) break;
    }
  //  cout << cnt << endl;
    outpt();
    return 0;
  //  fclose(stdin);
    fclose(stdout);
}
