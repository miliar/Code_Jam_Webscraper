#include<stdio.h>
#include<string.h>
int main()
{
    int i, j, T, tt, n, cnt;
    char str[110];
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%s", &str);
        n=strlen(str); cnt=1;
        for(i=1; i<n; ++i)
        {
            if(str[i]!=str[i-1]) ++cnt;
        }
        if(cnt==1)
        {
            if(str[0]=='-') printf("Case #%d: 1\n", tt);
            else printf("Case #%d: 0\n", tt);
        }
        else
        {
            if(str[n-1]=='+') --cnt;
            printf("Case #%d: %d\n", tt, cnt);
        }
    }
}
