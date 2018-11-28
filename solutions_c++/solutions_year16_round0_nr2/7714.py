#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
#define mem(a) memset( a, 0, sizeof(a) )
using namespace std;
typedef long long ll;

char s[105];

int main()
{
    int T, i, j, ans, n, cas = 1;
    freopen("B-large.in", "r", stdin );
    freopen("out.txt", "w", stdout );
    scanf("%d", &T);
    while( T -- ){
        scanf("%s", s);
        n = strlen(s);
        int st;
        ans = 0;
        if( s[0] == '+' )st = 0;
        else{
            ans = 1;
            st = 0;
            while( s[st] == '-' ) st++;
        }
        int fl = 0;
        for( i = st; i < n; i ++ ){
            if( s[i] == '-' ){
                if( fl )
                    ans += 2;
                fl = 0;
            }
            else{
                fl = 1;
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
}
