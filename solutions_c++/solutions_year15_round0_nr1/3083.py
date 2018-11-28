#include <stdio.h>

int n;
char s[1024];

int main()
{
    int T;
    int ca = 1;
    scanf("%d",&T);
    while(T--)
    {
        int now = 0,ans = 0;
        scanf("%d%s",&n,s);
        for(int i=0;i<=n;i++)
        {
            int need = (now>=i) ? 0 : (i-now);
            ans += need;
            now += need;
            now += s[i] - '0';
        }
        printf("Case #%d: %d\n",(ca++),ans);
    }
    return 0;
}

