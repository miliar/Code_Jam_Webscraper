#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen ("output.txt","w",stdout);
    int Test,k=0;
    scanf("%d",&Test);
    while(Test--)
    {
        int K,C,S,i;
        int cnt=0;
        scanf("%d%d%d",&K,&C,&S);
        printf("Case #%d: ",++k);
        if(S>=K)
        {
            for(i=1;i<=S;++i)
                printf("%d ",i);
            printf("\n");
        }
        else
        {
            if(C==1)
                printf("IMPOSSIBLE\n");
            else
            {
                for(i=1;i<=K*K;i+=K+1)
                    cnt++;
                if(k==2)
                    cnt=2;
                if(cnt>S)
                    printf("IMPOSSIBLE\n");
                else
                {
                    for(i=1;i<=K*K;i+=K+1)
                        printf("%d ",i);
                    printf("\n");
                }
            }
        }
    }
    fclose(stdout);
    return 0;
}
