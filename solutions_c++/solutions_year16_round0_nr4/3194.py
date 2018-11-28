#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int k,c,s;

        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",t);
        for(int i=1;i<=k;i++)
            printf("%d ",i);
        printf("\n");
    }
    return 0;
}
