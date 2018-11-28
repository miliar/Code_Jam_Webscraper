#include <stdio.h>
#include <string.h>

char s[110];

int main()
{
    int i,l,t,ans,T;
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        scanf("%s",s);
        l=strlen(s); ans=0;
        for (i=1;i<l;i++)
            if (s[i-1]!=s[i])
                ans++;
        if (s[l-1]=='-')
            ans++;
        printf("%d\n",ans);
    }
}
