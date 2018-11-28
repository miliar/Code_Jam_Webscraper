#include <stdio.h>
char in [100010];
int main()
{
    int nt = 0;
    scanf(" %d",&nt);
    for(int T = 1; T <= nt; T++)
    {
        int np = 0;
        int sz;
        int ans = 0;
        scanf("%d %s",&sz,&in);
        for(int i = 1; i <= sz; i++)
        {
            int v = in[i - 1] - '0';
            np += v;
            if(i > np)
            {
                ans += (i - np);
                np = i;
            }
        }
        printf("Case #%d: %d\n", T, ans);
    }
}
