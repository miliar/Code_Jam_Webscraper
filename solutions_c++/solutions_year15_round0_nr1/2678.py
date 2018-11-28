#include <cstdio>

int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;++i)
    {
        int res=0;
        int q;
        scanf("%d",&q);
        char S[q+2];
        scanf("%s",S);
        int prefs = S[0] - '0';
        for(int j=1;j<=q;++j)
        {
            if (prefs < j)
            {
                res += j-prefs;
                prefs = j;
            }
            prefs += S[j] - '0';
        }
        printf("Case #%d: %d\n",i,res);
    }
    return 0;
}
