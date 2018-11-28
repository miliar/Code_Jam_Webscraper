#include<stdio.h>

char s[1000+5];

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int c=1; c<=T; ++c)
    {
        int Smax;
        scanf("%d", &Smax);
        scanf("%s", s);
        int n = 0;
        int extra = 0;
        for(int i=0; i<=Smax; ++i)
        {
            if(n >= i)
            {
                n += s[i] - '0';
            }
            else
            {
                extra += i - n;
                n = i + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n", c, extra);
    }
    return 0;
}
