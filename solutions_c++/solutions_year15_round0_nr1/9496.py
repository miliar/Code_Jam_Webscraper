#include <stdio.h>

int main()
{
    int T, n;
    char s[1005];
    scanf("%d", &T);
    for( int t=1; t<=T; t++ )
    {
        scanf("%d %s", &n, s);
        int aud = s[0] - '0';
        int extra = 0;
        for( int i=1; i<=n; i++ )
        {
            if ( s[i] == '0' ) continue;
            if ( extra + aud < i )
                extra = i - aud;
            aud += s[i] - '0';
        }
        printf("Case #%d: %d\n", t, extra);

    }
    return 0;
}

