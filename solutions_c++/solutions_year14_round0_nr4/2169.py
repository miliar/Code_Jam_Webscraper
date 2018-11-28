#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int M = 1010;
double N[M], K[M];
bool v[M], x[M];
int t, n;

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int ic = 1;
    scanf("%d", &t);
    while ( t-- )
    {
        memset(v, 0, sizeof(v));
        memset(x, 0, sizeof(x));
        scanf("%d", &n);
        int ans1 = n;
        for ( int i = 0; i < n; ++i ) scanf("%lf", &N[i]);
        for ( int i = 0; i < n; ++i ) scanf("%lf", &K[i]);
        sort(N, N+n);
        sort(K, K+n);
        for ( int i = 0; i < n; ++i ) {
            for ( int j = 0; j < n; ++j ) {
                if ( !v[j] && N[i] < K[j] )
                {
                    v[j] = true;
                    ans1--;
                    //printf("i = %d  j = %d ans1 = %d\n", i, j, ans1);
                    break;
                }
            }
        }
        int nb = 0, ne = n-1, kb = 0, ke = n-1, ans = 0;
        while ( nb <= ne )
        {
            if ( N[nb] > K[kb] ) {
                ans++;
                nb++;
                kb++;
            }
            else if ( N[nb] == K[kb] ) {
                nb++;
                kb++;
            }
            else if ( N[ne] > K[ke] ) {
                ne--;
                ke--;
                ans++;
            }
            else if ( N[ne] == K[ke] ) {
                ne--;
                ke--;
            }
            if ( N[nb] < K[kb] )
            {
                nb++;
                ke--;
            }
        }
        printf("Case #%d: %d %d\n", ic++, ans, ans1);
    }
}
