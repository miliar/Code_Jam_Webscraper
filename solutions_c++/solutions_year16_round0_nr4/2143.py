#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("D.in","r",stdin);
    freopen("1.txt","w",stdout);
    int T,K,C,S;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d%d%d",&K,&C,&S);
        printf("Case #%d: ",i);
        for(int j=1;j<=K;j++)
            printf("%d%c",j,j==K?'\n':' ');
    }
    return 0;
}
