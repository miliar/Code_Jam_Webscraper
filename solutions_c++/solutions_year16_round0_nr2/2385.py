#include <cstdio>
#include <cstring>
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        char S[109];
        scanf("%s",&S);
        int sz=strlen(S),ans=0;
        for(int j=1;j<sz;j++)
        {
            if(S[j]!=S[j-1])ans++;
        }
        if(S[sz-1]=='-')ans++;
        printf("%d\n",ans);
    }
}
