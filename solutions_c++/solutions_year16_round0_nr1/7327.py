/**
  * URL: https://code.google.com/codejam/contest/6254486/dashboard#s=p0
  * Task: Google Code Jam / Problem A. Counting Sheep
  * Solution:
  **/

#include <array>
#include <cstdio>

const int MAXN = 1e6;
const int DIGITS = 10;
const unsigned long long FULL = (1 << 10) - 1;

std::array<int, MAXN> solution;
void precompute();
void solve();

int main()
{
    precompute();
    solve();

    return 0;
}

void precompute()
{
    for ( int i = 1; i <= MAXN; ++i )
    {
        std::array<bool, DIGITS> used;
        for ( bool& x : used )
            x = false;

        unsigned long long full = 0;
        for ( int k = 1; ; ++k )
        {
            int x = i * k;
            while ( x )
            {
                int d = x % 10;
                used[d] = true;
                full |= (1 << d);

                x /= 10;
            }

            if ( full == FULL )
            {
                solution[i] = i * k;
                break;
            }
        }
    }
}

void solve()
{
    int t;
    scanf("%d", &t);
    for ( int i = 1; i <= t; ++i )
    {
        int n;
        scanf("%d", &n);

        printf("Case #%d: ", i);
        if ( n == 0 )   printf("INSOMNIA\n");
        else            printf("%d\n", solution[n]);
    }
}
