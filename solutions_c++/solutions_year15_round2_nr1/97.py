#include <iostream>
#include <cstdio>
#define f cin
#define g cout

using namespace std;

long long N;

long long pow (int p)
{
    long long ret = 1;
    for (int i=1; i<=p; i++)
        ret *= 10LL;
    return ret;
}

long long rev (long long x)
{
    long long y = 0;
    while (x)
    {
        y = y*10LL + (x%10);
        x/=10LL;
    }
    return y;
}

int dig (long long x)
{
    int cnt = 0;
    while (x)
    {
        cnt++;
        x/=10;
    }

    return cnt;
}

int main ()
{
    #ifndef ONLINE_JUDGE
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    #endif

    int T;
    f >> T;
    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";

        f >> N;
        long long x = 1;
        long long ans = 1;

        while (dig(x) < dig(N))
        {
            long long target = pow(dig(x));
            if (x==1)
            {
                //g << x << ' ' << target << '\n';
                ans += target - x;
                x = target;
                continue;
            }

            long long steps = pow((dig(x)+1)/2) - 1;
            ans += steps;

            //g << x << ' ';
            x += steps;
            //g << x << ' ';
            if (target - x > 1 + target - rev(x))
            {
                ans++;
                x = rev(x);
                //g << "rev " << x << ' ';
            }

            ans += target - x;
            x = target;
            //g << x << '\n';
        }

        if (x == N)
        {
            g << ans << '\n';
            continue;
        }

        if (N%10==0)
        {
            N--;
            ans++;
        }

        long long target = pow(dig(N)/2);
        target = rev((N / target) - (N%10==0));

        ans += target;
        x += target;

        target = N;
        if (target - x > 1 + target - rev(x))
        {
            ans++;
            x = rev(x);
            //g << "rev " << x << ' ';
        }

        ans += target - x;
        x = target;

        g << ans << '\n';
    }

    return 0;
}

