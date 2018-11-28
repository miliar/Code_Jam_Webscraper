#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
#define maxn ( 100000 + 10 )
#define maxe ( 20000 + 10 )
#define LL long long
#define inf 0x3f3f3f3f
#define lson id << 1, l, m
#define rson id << 1 | 1, m + 1, r
#define mod 9973

char s[1111];
int main ()
{
    freopen( "A-large.txt", "r", stdin );
    freopen( "out.txt","w", stdout);
    int T;
    scanf("%d", &T );

    int cas = 1;

    while( T-- ) {
        int n;
        scanf("%d", &n );
        scanf("%s", s );
        int cur = 0;
        int ans = 0;
        for( int i = 0; i <= n; ++i ) {
            if( cur >= i )
                cur += s[i] - '0';
            else {
                ans += i - cur;
                cur = i;
                cur += s[i] - '0';
            }
        }

        printf("Case #%d: %d\n", cas++, ans );
    }
}
