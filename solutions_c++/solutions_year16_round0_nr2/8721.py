#include <stdio.h>
#include <string.h>

char s[103];

void solve()
{
    int i, j, k, l, ans;
    scanf("%s", s);
    l = strlen(s);
    ans = 0;

    for(i=0; i<l;)
    {
        for(j=i; (j<l) && (s[i]==s[j]); ++j);
        if( (j==l) && (s[i]=='+'))
            break;
        for(k=0; k<j; ++k)
            if(s[k]=='-')
                s[k] = '+';
            else
                s[k] = '-';

        //printf("%s i=%d j=%d\n", s, i, j);
        i = j;
        ++ans;
    }
    if(s[0]=='-')
        ++ans;
    printf("%d\n", ans);
}
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int i, t;

    scanf("%d", &t);
    for(i=1; i<=t; ++i)
    {
        printf("CASE #%d: ", i);
        solve();
    }
    return 0;
}
