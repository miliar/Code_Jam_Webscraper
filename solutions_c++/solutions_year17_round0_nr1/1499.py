#include<stdio.h>
#include<string.h>
int n, k;
char str[100010];
int main()
{
    int T, tt, i, cnt;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%s", str);
        scanf("%d", &k);
        n = strlen(str);
        cnt=0;
        for(i=0; i<=n-k; ++i)
        {
            if(str[i] == '-')
            {
                ++cnt;
                for(int j=0; j<k; ++j) str[i+j] = '+' + '-' - str[i+j];
            }
        }
        for(i=n-k+1; i<n; ++i)
            if(str[i] == '-') cnt = -1;
        printf("Case #%d: ", tt);
        if(cnt==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n", cnt);
    }
}
