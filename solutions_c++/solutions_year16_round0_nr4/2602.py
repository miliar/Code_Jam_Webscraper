#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("codejam.txt","w",stdout);
    int T,I=1;
    scanf("%d",&T);
    while(T--)
    {
        int K,C,S;
        printf("Case #%d:",I++);
        scanf("%d %d %d",&K,&C,&S);
        if(K==S)
            for(int i=1;i<=K;i++)
                printf(" %d",i);
        printf("\n");
    }
    return 0;
}
