#include <bits/stdc++.h>

using namespace std;


int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);

    int T,K,C,S;
    scanf("%d",&T);
    for(int tst = 1; tst <= T; ++tst)
    {
        scanf("%d%d%d",&K,&C,&S);
        printf("Case #%d: ",tst);
        for(int i = 1; i <= S; ++i)
            printf("%d ",i);
        printf("\n");
    }
    return 0;
}
