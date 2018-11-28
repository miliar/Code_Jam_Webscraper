#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
typedef long long LL;

void mark(int *seen, long long n)
{
    while (n > 0)
    {
        seen[n % 10] = 1;
        n /= 10;
    }
}

bool covered(int *seen)
{
    for (int i = 0; i < 10; i++)
        if (seen[i] == 0) return false;
    return true;
}

void solve()
{
    long long n, m;
    int seen[10];
    memset(seen, 0, sizeof(int) * 10);

    scanf("%lld ", &n);

    if (n == 0) printf("INSOMNIA\n");
    else
    {
        m = n;
        while (true)
        {
            mark(seen, m);
            if (covered(seen))
            {
                if (m < 0) exit(0);
                printf("%lld\n", m);
                return;
            }
            m += n;
        }
    }
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

    int cases;
    scanf("%d\n", &cases);

    for(int i = 1; i <= cases; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
	return 0;

}
