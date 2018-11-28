#include <cstdio>
#include <cstring>
int main()
{
    char s[110];
    int T,l,ans=0;
    scanf("%d",&T);
    for(int c=1; c<=T; c++)
    {
        scanf(" %s",s);
        int l=strlen(s)-1;
        while(l>=0&&s[l]=='+') l--;
        if(l<0) printf("Case #%d: 0\n",c);
        else
        {
            ans=0;
            for( ; l>=0; l--)
            {
                if(s[l]!=s[l+1])
                    ans++;
            }
            printf("Case #%d: %d\n",c,ans);
        }
    }
    return 0;
}
