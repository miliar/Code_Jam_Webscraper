#include <stdio.h>

typedef long long ll;

bool cl[10];

void solve(int test)
{
    printf("CASE #%d: ", test);
    ll n, c, m;
    int i, num;
    scanf("%lld", &n);
    if(n==0)
    {
        printf("INSOMNIA\n");
        return;
    }

    for(i=0; i<10; ++i)
        cl[i] = false;
    num = 10;
    m = n;
    while(num)
    {
        c = m;
        while(c)
        {
            if(!cl[c%10])
            {
                cl[c%10] = true;
                --num;
            }
            c /= 10;
        }
        m += n;
    }
    m -= n;
    printf("%lld\n", m);

}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.out", "w", stdout);

    int i, t;
    scanf("%d", &t);
    for(i=1; i<=t; ++i)
        solve(i);
    return 0;
}
