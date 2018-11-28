#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cmath>
using namespace std;
typedef long long LL;
const int N = 100005;
LL p[1000000], dig[16];
int cnt;
   LL num[10000][2], mi = 1000000000000000LL, ma = 1;
void ds( LL n, int d, int pos );
bool ck ( LL n )
{
    long long k = sqrt (n * 1.0) + 1e-6;
    if (k * k != n)
        return 0;


    int ld = 0, de[15];
    while (k) de[ld ++] = k % 10, k /= 10;

    for (int j = 0; j << 1 < ld; j ++)
        if (de[j] != de[ld - 1 - j])
               return 0;
    return 1;
}

int main()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    dig[0] = 1;
    for (int i = 1; i < 16; i ++) dig[i] = dig[i - 1] * 10;
    for (int cas = 0; cas < T; cas ++)
    {
        cin>> num[cas][0] >> num[cas][1];
        if (num[cas][1] >  ma )
            ma = num[cas][1];

        if (num[cas][0] <  mi)
            mi = num[cas][0];
    }

    int ld = 0, rd = 0;
    while (mi) ld ++, mi /= 10;
    while (ma) rd ++, ma /= 10;
    for (int i = ld; i <= rd; i ++)
        ds (0, i, 0);

    sort( p, p + cnt );
    //printf ("%d\n", cnt);
    for(int cas = 0; cas < T; cas ++)
    {
        int ans = 0;
        for (int i = 0; i < cnt; i ++)
            if (num[cas][0] <= p[i] && p[i] <= num[cas][1])
                ans ++;

        printf("Case #%d: %d\n", cas + 1, ans);
    }
}
void ds( LL n, int d, int pos )
{
    if ( pos << 1 >= d )
    {
        if ( n && ck(n))
            p[cnt ++] = n;
        return;
    }
    for (int i = 0; i <= 9; i ++)
    {
        if (d == (pos << 1 | 1))
            ds(n + dig[pos] * i, d, pos + 1);
        else
            ds(n + (dig[pos] + dig[d - 1 - pos]) * i, d, pos + 1);
    }
}
