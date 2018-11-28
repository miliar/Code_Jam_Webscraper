#include<stdio.h>
#include<cstring>

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T, cases, len, i, j, k, an;
    char S[1003];
    scanf("%d", &T);
    for(cases = 1; cases <= T; cases++){
        scanf("%s%d", S+1, &k);
        len = strlen(S+1);
        an = 0;
        for(i=1;i<=len-k+1;i++){
            if(S[i]!='+'){
                an++;
                for(j=i;j<=i+k-1;j++){
                    if(S[j]=='+')S[j]='-';
                    else S[j]='+';
                }
            }
        }
        for(i=1;i<=len;i++)if(S[i]!='+')an=-1;
        if(an==-1)printf("Case #%d: IMPOSSIBLE\n", cases);
        else printf("Case #%d: %d\n", cases, an);
    }

    return 0;
}
