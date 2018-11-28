#include <cstdio>

int main()
{
    int T;
    freopen("A0L.in","r",stdin);
    freopen("resL.out","w",stdout);
    scanf("%d", &T);
    for( int t = 1 ; t <= T ; t++ )
    {
        int A, Sum = 0, Smax, ans = 0;
        scanf("%d", &Smax);
        for(int i = 0 ; i <= Smax ; i++ )
        {
            scanf("%1d", &A);
            if( A && Sum < i ) ans += i-Sum, Sum+=(i-Sum);
            Sum += A;
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
