#include <stdio.h>

int main()
{
    int T, t, smax, ans, aud, i;
    char s[1001];
    scanf("%d",&T);

    t = T;
    while(t--) 
    {
        scanf("%d %s",&smax,s);
        ans = 0;
        aud = 0;
        for(i=0; i<=smax; i++)
        {
            if(aud < i)
            {
                ans += i - aud;
                aud = i;
            }
            aud += s[i] - '0';
            if(aud > smax)
                break;
        }
        printf("Case #%d: %d\n",T-t, ans);
    }

    return 0;
}
